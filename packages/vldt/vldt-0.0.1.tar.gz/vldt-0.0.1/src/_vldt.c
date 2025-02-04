#include <Python.h>
#include <structmember.h>

/* Forward declaration of BaseModelType defined in base_model.c */
extern PyTypeObject BaseModelType;

/* -- Validation logic (remains in _vldt.c) -- */

/* Global variable used by validate(). Note that ClassVarType is not static
   so that it is visible to base_model.c (via an extern declaration there). */
static PyObject *UnionType = NULL;
PyObject *ClassVarType = NULL;

/* The validate function implementation */
int validate(PyObject *value, PyObject *expected_type, PyObject *error_messages) {
    PyObject *origin = PyObject_GetAttrString(expected_type, "__origin__");

    if (origin) {
        PyObject *args = NULL;
        int result = -1;

        if (UnionType == NULL) {
            PyObject *typing_module = PyImport_ImportModule("typing");
            if (typing_module == NULL) {
                Py_DECREF(origin);
                return -1;
            }
            UnionType = PyObject_GetAttrString(typing_module, "Union");
            Py_DECREF(typing_module);
            if (UnionType == NULL) {
                Py_DECREF(origin);
                return -1;
            }
        }

        args = PyObject_GetAttrString(expected_type, "__args__");
        if (!args || !PyTuple_Check(args)) {
            PyObject *err_msg = PyUnicode_FromString("Invalid generic arguments");
            PyList_Append(error_messages, err_msg);
            Py_DECREF(err_msg);
            Py_XDECREF(args);
            Py_DECREF(origin);
            return -1;
        }

        if (origin == UnionType) {
            Py_ssize_t num_args = PyTuple_Size(args);
            PyObject *union_errors = PyList_New(0);
            result = -1;

            for (Py_ssize_t i = 0; i < num_args; ++i) {
                PyObject *arg_type = PyTuple_GetItem(args, i);
                PyObject *type_errors = PyList_New(0);
                if (validate(value, arg_type, type_errors) == 0) {
                    result = 0;
                    Py_DECREF(type_errors);
                    break;
                } else {
                    Py_ssize_t num_errors = PyList_Size(type_errors);
                    for (Py_ssize_t j = 0; j < num_errors; ++j) {
                        PyObject *error = PyList_GetItem(type_errors, j);
                        PyObject *formatted = PyUnicode_FromFormat("Union type %R: %U", arg_type, error);
                        PyList_Append(union_errors, formatted);
                        Py_DECREF(formatted);
                    }
                }
                Py_DECREF(type_errors);
            }

            if (result != 0) {
                Py_ssize_t num_errors = PyList_Size(union_errors);
                for (Py_ssize_t i = 0; i < num_errors; ++i) {
                    PyObject *error = PyList_GetItem(union_errors, i);
                    PyList_Append(error_messages, error);
                }
                if (num_errors == 0) {
                    PyObject *err_msg = PyUnicode_FromFormat("Value doesn't match any type in Union %R", expected_type);
                    PyList_Append(error_messages, err_msg);
                    Py_DECREF(err_msg);
                }
            }
            Py_DECREF(union_errors);
        }
        else if (origin == (PyObject *)&PyList_Type) {
            PyObject *item_type = PyTuple_GetItem(args, 0);
            Py_ssize_t len = PyList_Size(value);
            result = 0;
            PyObject *list_errors = PyList_New(0);

            for (Py_ssize_t i = 0; i < len; ++i) {
                PyObject *item = PyList_GetItem(value, i);
                PyObject *item_errors = PyList_New(0);
                if (validate(item, item_type, item_errors) != 0) {
                    result = -1;
                    Py_ssize_t num_errors = PyList_Size(item_errors);
                    for (Py_ssize_t j = 0; j < num_errors; ++j) {
                        PyObject *error = PyList_GetItem(item_errors, j);
                        PyObject *formatted = PyUnicode_FromFormat("List index %zd: %U", i, error);
                        PyList_Append(list_errors, formatted);
                        Py_DECREF(formatted);
                    }
                }
                Py_DECREF(item_errors);
            }

            if (result == -1) {
                Py_ssize_t num_errors = PyList_Size(list_errors);
                for (Py_ssize_t i = 0; i < num_errors; ++i) {
                    PyObject *error = PyList_GetItem(list_errors, i);
                    PyList_Append(error_messages, error);
                }
            }
            Py_DECREF(list_errors);
        }
        else if (origin == (PyObject *)&PyDict_Type) {
            PyObject *key_type = PyTuple_GetItem(args, 0);
            PyObject *value_type = PyTuple_GetItem(args, 1);
            PyObject *key, *val;
            Py_ssize_t pos = 0;
            result = 0;
            PyObject *dict_errors = PyList_New(0);

            while (PyDict_Next(value, &pos, &key, &val)) {
                PyObject *key_errors = PyList_New(0);
                if (validate(key, key_type, key_errors) != 0) {
                    result = -1;
                    Py_ssize_t num_errors = PyList_Size(key_errors);
                    for (Py_ssize_t j = 0; j < num_errors; ++j) {
                        PyObject *error = PyList_GetItem(key_errors, j);
                        PyObject *key_repr = PyObject_Repr(key);
                        PyObject *formatted = PyUnicode_FromFormat("Dict key %S: %U", key_repr, error);
                        PyList_Append(dict_errors, formatted);
                        Py_DECREF(formatted);
                        Py_DECREF(key_repr);
                    }
                }
                Py_DECREF(key_errors);

                PyObject *val_errors = PyList_New(0);
                if (validate(val, value_type, val_errors) != 0) {
                    result = -1;
                    Py_ssize_t num_errors = PyList_Size(val_errors);
                    for (Py_ssize_t j = 0; j < num_errors; ++j) {
                        PyObject *error = PyList_GetItem(val_errors, j);
                        PyObject *key_repr = PyObject_Repr(key);
                        PyObject *formatted = PyUnicode_FromFormat("Dict value for key %S: %U", key_repr, error);
                        PyList_Append(dict_errors, formatted);
                        Py_DECREF(formatted);
                        Py_DECREF(key_repr);
                    }
                }
                Py_DECREF(val_errors);
            }

            if (result == -1) {
                Py_ssize_t num_errors = PyList_Size(dict_errors);
                for (Py_ssize_t i = 0; i < num_errors; ++i) {
                    PyObject *error = PyList_GetItem(dict_errors, i);
                    PyList_Append(error_messages, error);
                }
            }
            Py_DECREF(dict_errors);
        }
        else if (origin == (PyObject *)&PyTuple_Type) {
            Py_ssize_t tuple_size = PyTuple_Size(value);
            Py_ssize_t num_args = PyTuple_Size(args);
            result = 0;
            PyObject *tuple_errors = PyList_New(0);

            if (num_args != tuple_size) {
                PyObject *err_msg = PyUnicode_FromFormat("Expected tuple of length %zd, got %zd", num_args, tuple_size);
                PyList_Append(tuple_errors, err_msg);
                Py_DECREF(err_msg);
                result = -1;
            }

            for (Py_ssize_t i = 0; i < num_args && i < tuple_size; ++i) {
                PyObject *item = PyTuple_GET_ITEM(value, i);
                PyObject *arg_type = PyTuple_GET_ITEM(args, i);
                PyObject *item_errors = PyList_New(0);
                if (validate(item, arg_type, item_errors) != 0) {
                    result = -1;
                    Py_ssize_t num_errors = PyList_Size(item_errors);
                    for (Py_ssize_t j = 0; j < num_errors; ++j) {
                        PyObject *error = PyList_GetItem(item_errors, j);
                        PyObject *formatted = PyUnicode_FromFormat("Tuple index %zd: %U", i, error);
                        PyList_Append(tuple_errors, formatted);
                        Py_DECREF(formatted);
                    }
                }
                Py_DECREF(item_errors);
            }

            if (result == -1) {
                Py_ssize_t num_errors = PyList_Size(tuple_errors);
                for (Py_ssize_t i = 0; i < num_errors; ++i) {
                    PyObject *error = PyList_GetItem(tuple_errors, i);
                    PyList_Append(error_messages, error);
                }
            }
            Py_DECREF(tuple_errors);
        }
        else if (origin == (PyObject *)&PySet_Type) {
            Py_ssize_t num_args = PyTuple_Size(args);
            if (num_args != 1) {
                PyObject *err_msg = PyUnicode_FromString("Set requires exactly one type argument");
                PyList_Append(error_messages, err_msg);
                Py_DECREF(err_msg);
                result = -1;
            } else {
                PyObject *item_type = PyTuple_GetItem(args, 0);
                PyObject *iterator = PyObject_GetIter(value);
                result = 0;
                PyObject *set_errors = PyList_New(0);

                if (iterator == NULL) {
                    result = -1;
                } else {
                    PyObject *item;
                    Py_ssize_t index = 0;
                    while ((item = PyIter_Next(iterator)) != NULL) {
                        PyObject *item_errors = PyList_New(0);
                        if (validate(item, item_type, item_errors) != 0) {
                            result = -1;
                            Py_ssize_t num_errors = PyList_Size(item_errors);
                            for (Py_ssize_t j = 0; j < num_errors; ++j) {
                                PyObject *error = PyList_GetItem(item_errors, j);
                                PyObject *formatted = PyUnicode_FromFormat("Set element %zd: %U", index, error);
                                PyList_Append(set_errors, formatted);
                                Py_DECREF(formatted);
                            }
                        }
                        Py_DECREF(item_errors);
                        Py_DECREF(item);
                        index++;
                    }
                    Py_DECREF(iterator);
                }

                if (result == -1) {
                    Py_ssize_t num_errors = PyList_Size(set_errors);
                    for (Py_ssize_t i = 0; i < num_errors; ++i) {
                        PyObject *error = PyList_GetItem(set_errors, i);
                        PyList_Append(error_messages, error);
                    }
                }
                Py_DECREF(set_errors);
            }
        }
        else {
            PyObject *err_msg = PyUnicode_FromFormat("Unhandled generic type: %R", origin);
            PyList_Append(error_messages, err_msg);
            Py_DECREF(err_msg);
            result = -1;
        }

        Py_DECREF(args);
        Py_DECREF(origin);
        return result;
    } else {
        PyErr_Clear();

        int is_instance = PyObject_IsInstance(value, expected_type);
        if (!is_instance) {
            PyObject *type_name = PyObject_GetAttrString(PyObject_Type(value), "__name__");
            PyObject *expected_name = PyObject_GetAttrString(expected_type, "__name__");
            PyObject *err_msg = PyUnicode_FromFormat("Expected type %S, got %S", expected_name, type_name);
            PyList_Append(error_messages, err_msg);
            Py_DECREF(err_msg);
            Py_XDECREF(type_name);
            Py_XDECREF(expected_name);
            return -1;
        }
    }

    return 0;
}

/* -- Module initialization -- */

static PyModuleDef _vldtmodule = {
    PyModuleDef_HEAD_INIT,
    .m_name = "vldt._vldt",
    .m_size = -1,
};

PyMODINIT_FUNC PyInit__vldt(void) {
    PyObject *m;
    if (PyType_Ready(&BaseModelType) < 0)
        return NULL;

    m = PyModule_Create(&_vldtmodule);
    if (m == NULL)
        return NULL;

    Py_INCREF(&BaseModelType);
    if (PyModule_AddObject(m, "BaseModel", (PyObject *)&BaseModelType) < 0) {
        Py_DECREF(&BaseModelType);
        Py_DECREF(m);
        return NULL;
    }
    return m;
}
