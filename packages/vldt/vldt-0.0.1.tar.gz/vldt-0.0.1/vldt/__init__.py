from typing import ClassVar, get_type_hints, get_origin, get_args
from typing_extensions import get_origin
from vldt._vldt import BaseModel as _BaseModel

class BaseModelMeta(type):
    def __new__(cls, name, bases, namespace):
        new_cls = super().__new__(cls, name, bases, namespace)
        annotations = get_type_hints(new_cls, include_extras=True)
        
        # Ensure __annotations__ includes all merged annotations
        new_cls.__annotations__ = annotations
        
        class_annotations = {}
        instance_annotations = {}
        
        for attr_name, attr_type in annotations.items():
            if get_origin(attr_type) is ClassVar:
                class_annotations[attr_name] = get_args(attr_type)[0]
            else:
                instance_annotations[attr_name] = attr_type

        new_cls.__class_annotations__ = class_annotations or {}
        new_cls.__instance_annotations__ = instance_annotations or {}

        # Validate class attributes
        for name, ann_type in class_annotations.items():
            value = getattr(new_cls, name, None)
            if value is None:
                raise TypeError(f"Missing required class attribute: {name}")
            if not isinstance(value, ann_type):
                raise TypeError(f"Class attribute {name} must be {ann_type}, got {type(value)}")

        return new_cls

class BaseModel(_BaseModel, metaclass=BaseModelMeta):
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        # Ensure subclasses inherit annotations correctly
        cls.__class_annotations__ = getattr(cls, '__class_annotations__', {})
        cls.__instance_annotations__ = getattr(cls, '__instance_annotations__', {})

__all__ = ['BaseModel']