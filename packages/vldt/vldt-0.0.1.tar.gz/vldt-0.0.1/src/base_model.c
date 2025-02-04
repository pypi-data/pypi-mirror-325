#include <Python.h>
#include <structmember.h>

/* Declare external symbols defined in _vldt.c */
extern int validate(PyObject *value, PyObject *expected_type, PyObject *error_messages);
extern PyObject *ClassVarType;

typedef struct {
    PyObject_HEAD
} BaseModel;

/* BaseModel.__init__ implementation */
static int BaseModel_init(PyObject *self, PyObject *args, PyObject *kwds) {
    if (PyTuple_Size(args) > 0) {
        PyErr_SetString(PyExc_TypeError, "Positional arguments are not allowed");
        return -1;
    }

    PyObject *cls = PyObject_GetAttrString(self, "__class__");
    PyObject *annotations = PyObject_GetAttrString(cls, "__annotations__");
    if (!annotations) {
        PyErr_SetString(PyExc_TypeError, "Class must have type annotations");
        Py_DECREF(cls);
        return -1;
    }

    if (ClassVarType == NULL) {
        PyObject *typing_module = PyImport_ImportModule("typing");
        if (typing_module == NULL) {
            Py_DECREF(annotations);
            Py_DECREF(cls);
            return -1;
        }
        ClassVarType = PyObject_GetAttrString(typing_module, "ClassVar");
        Py_DECREF(typing_module);
        if (ClassVarType == NULL) {
            Py_DECREF(annotations);
            Py_DECREF(cls);
            return -1;
        }
    }

    PyObject *all_errors = PyList_New(0);
    int validation_failed = 0;

    Py_ssize_t pos = 0;
    PyObject *key, *expected_type;
    while (PyDict_Next(annotations, &pos, &key, &expected_type)) {
        PyObject *origin = PyObject_GetAttrString(expected_type, "__origin__");
        if (origin) {
            if (origin == ClassVarType) {
                Py_DECREF(origin);
                continue;
            }
            Py_DECREF(origin);
        } else {
            PyErr_Clear();
        }

        const char *key_str = PyUnicode_AsUTF8(key);
        PyObject *value = kwds ? PyDict_GetItem(kwds, key) : NULL;

        if (!value) {
            value = PyObject_GetAttr(cls, key);
            if (!value) {
                PyObject *err_msg = PyUnicode_FromFormat("Field '%s': Missing required field", key_str);
                PyList_Append(all_errors, err_msg);
                Py_DECREF(err_msg);
                validation_failed = 1;
                continue;
            }
        }

        PyObject *field_errors = PyList_New(0);
        if (validate(value, expected_type, field_errors) != 0) {
            Py_ssize_t num_errors = PyList_Size(field_errors);
            for (Py_ssize_t i = 0; i < num_errors; ++i) {
                PyObject *error = PyList_GetItem(field_errors, i);
                PyObject *formatted = PyUnicode_FromFormat("Field '%s': %U", key_str, error);
                PyList_Append(all_errors, formatted);
                Py_DECREF(formatted);
            }
            validation_failed = 1;
        }
        Py_DECREF(field_errors);

        if (PyObject_SetAttr(self, key, value) < 0) {
            PyObject *err_msg = PyUnicode_FromFormat("Field '%s': Failed to set attribute", key_str);
            PyList_Append(all_errors, err_msg);
            Py_DECREF(err_msg);
            PyErr_Clear();
            validation_failed = 1;
        }
    }

    Py_DECREF(annotations);
    Py_DECREF(cls);

    if (validation_failed) {
        PyObject *sep = PyUnicode_FromString("\n");
        PyObject *joined = PyUnicode_Join(sep, all_errors);
        PyErr_SetObject(PyExc_TypeError, joined);
        Py_DECREF(joined);
        Py_DECREF(sep);
        Py_DECREF(all_errors);
        return -1;
    }

    Py_DECREF(all_errors);
    return 0;
}

/* BaseModel.__setattr__ implementation */
static int BaseModel_setattro(PyObject *self, PyObject *name, PyObject *value) {
    PyObject *annotations = PyObject_GetAttrString((PyObject *)Py_TYPE(self), "__annotations__");
    if (!annotations)
        return -1;

    if (ClassVarType == NULL) {
        PyObject *typing_module = PyImport_ImportModule("typing");
        if (typing_module == NULL) {
            Py_DECREF(annotations);
            return -1;
        }
        ClassVarType = PyObject_GetAttrString(typing_module, "ClassVar");
        Py_DECREF(typing_module);
        if (ClassVarType == NULL) {
            Py_DECREF(annotations);
            return -1;
        }
    }

    int result = 0;
    if (PyDict_Contains(annotations, name)) {
        PyObject *expected_type = PyDict_GetItem(annotations, name);
        PyObject *origin = PyObject_GetAttrString(expected_type, "__origin__");
        if (origin) {
            if (origin == ClassVarType) {
                Py_DECREF(origin);
                Py_DECREF(annotations);
                PyErr_SetString(PyExc_AttributeError, "Cannot set ClassVar attribute");
                return -1;
            }
            Py_DECREF(origin);
        } else {
            PyErr_Clear();
        }

        PyObject *error_messages = PyList_New(0);
        if (validate(value, expected_type, error_messages) != 0) {
            const char *field_name = PyUnicode_AsUTF8(name);
            PyObject *all_errors = PyList_New(0);
            
            Py_ssize_t num_errors = PyList_Size(error_messages);
            for (Py_ssize_t i = 0; i < num_errors; ++i) {
                PyObject *error = PyList_GetItem(error_messages, i);
                PyObject *formatted = PyUnicode_FromFormat("Field '%s': %U", field_name, error);
                PyList_Append(all_errors, formatted);
                Py_DECREF(formatted);
            }
            
            PyObject *sep = PyUnicode_FromString("\n");
            PyObject *joined = PyUnicode_Join(sep, all_errors);
            PyErr_SetObject(PyExc_TypeError, joined);
            Py_DECREF(joined);
            Py_DECREF(sep);
            Py_DECREF(all_errors);
            result = -1;
        }
        Py_DECREF(error_messages);
        
        if (result == 0) {
            result = PyObject_GenericSetAttr(self, name, value);
        }
    } else {
        result = PyObject_GenericSetAttr(self, name, value);
    }

    Py_DECREF(annotations);
    return result;
}

/* BaseModel type definition */
PyTypeObject BaseModelType = {
    PyVarObject_HEAD_INIT(NULL, 0)
    .tp_name = "vldt._vldt.BaseModel",
    .tp_basicsize = sizeof(BaseModel),
    .tp_flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE,
    .tp_init = BaseModel_init,
    .tp_setattro = BaseModel_setattro,
    .tp_new = PyType_GenericNew,
};
