import pytest
from typing import ClassVar, Union, Optional, List, Dict, Any
from vldt import BaseModel

# Helper class for nested models
class Address(BaseModel):
    street: str
    zipcode: Union[int, str]
    country: str = "USA"

class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True

# Complex base model
class ComplexModel(BaseModel):
    MAX_ITEMS: ClassVar[int] = 100
    TIMEOUT: ClassVar[float] = 5.0
    
    id: Union[int, str]
    metadata: Dict[str, Any]
    products: List[Product]
    address: Optional[Address] = None
    history: List[Union[int, Dict[str, float]]] = []


def test_basic_valid_instantiation():
    """Test basic valid model creation"""
    class SimpleModel(BaseModel):
        name: str
        age: int
    
    obj = SimpleModel(name="Alice", age=30)
    assert obj.name == "Alice"
    assert obj.age == 30

def test_invalid_type_instantiation():
    """Test invalid type during initialization"""
    class SimpleModel(BaseModel):
        count: int
    
    with pytest.raises(TypeError) as exc:
        SimpleModel(count="five")
    
    assert "Field 'count': Expected type int, got str" in str(exc.value)

def test_optional_fields():
    """Test optional fields with defaults"""
    class OptionalModel(BaseModel):
        name: str
        age: Optional[int] = None
    
    # Valid cases
    obj1 = OptionalModel(name="Alice")
    assert obj1.age is None
    
    obj2 = OptionalModel(name="Bob", age=30)
    assert obj2.age == 30
    
    # Invalid optional value
    with pytest.raises(TypeError):
        OptionalModel(name="Charlie", age="thirty")

def test_union_types():
    """Test union type validation"""
    class UnionModel(BaseModel):
        identifier: Union[int, str]
    
    # Valid cases
    UnionModel(identifier=42)
    UnionModel(identifier="42")
    
    # Invalid case
    with pytest.raises(TypeError) as exc:
        UnionModel(identifier=42.0)
    assert "Field 'identifier': Union type" in str(exc.value)

def test_nested_models():
    """Test validation of nested BaseModel instances"""
    address = Address(street="123 Main St", zipcode=90210)
    product = Product(id=1, name="Widget", price=9.99)
    
    obj = ComplexModel(
        id="abc123",
        metadata={"version": 1.0},
        products=[product],
        address=address
    )
    
    assert obj.address.zipcode == 90210
    
    # Invalid nested model
    with pytest.raises(TypeError):
        ComplexModel(
            id=123,
            metadata={},
            products=[{"id": "1", "name": "Widget", "price": 9.99}]  # Invalid product
        )

def test_list_type_validation():
    """Test list type parameter validation"""
    class ListModel(BaseModel):
        values: List[int]
    
    # Valid
    ListModel(values=[1, 2, 3])
    
    # Invalid element type
    with pytest.raises(TypeError) as exc:
        ListModel(values=[1, "2", 3])
    assert "Field 'values': List index 1: Expected type int" in str(exc.value)

def test_dict_type_validation():
    """Test dictionary type validation"""
    class DictModel(BaseModel):
        mapping: Dict[str, int]
    
    # Valid
    DictModel(mapping={"a": 1, "b": 2})
    
    # Invalid key type
    with pytest.raises(TypeError):
        DictModel(mapping={1: 1, 2: 2})
    
    # Invalid value type
    with pytest.raises(TypeError):
        DictModel(mapping={"a": "1", "b": "2"})

def test_class_variable_validation():
    """Test class variable validation"""
    # Valid class vars
    class ValidClassVars(BaseModel):
        MAX_SIZE: ClassVar[int] = 100
        name: str
    
    # Invalid class var type
    with pytest.raises(TypeError) as exc:
        class InvalidClassVars(BaseModel):
            MAX_SIZE: ClassVar[int] = "100"
            name: str
    
    assert "Class attribute MAX_SIZE must be <class 'int'>" in str(exc.value)

def test_deeply_nested_structures():
    """Test multi-level nested structures"""
    class DeepModel(BaseModel):
        matrix: List[List[Union[int, float]]]
        nested: Dict[str, Dict[int, List[Address]]]
    
    valid_data = {
        "matrix": [[1, 2.0], [3.5, 4]],
        "nested": {
            "cities": {
                1: [Address(street="Main St", zipcode=12345)],
                2: [Address(street="Oak St", zipcode="67890")]
            }
        }
    }
    
    obj = DeepModel(**valid_data)
    assert len(obj.nested["cities"][2][0].street) > 0
    
def test_post_init_validation():
    """Test validation when setting attributes after initialization"""
    class UpdateModel(BaseModel):
        value: int
    
    obj = UpdateModel(value=42)
    
    # Valid update
    obj.value = 100
    assert obj.value == 100
    
    # Invalid update
    with pytest.raises(TypeError):
        obj.value = "invalid"

def test_missing_required_fields():
    """Test missing required fields"""
    class RequiredModel(BaseModel):
        name: str
        age: int
    
    with pytest.raises(TypeError) as exc:
        RequiredModel(name="Alice")
    
    assert "Field 'age': Missing required field" in str(exc.value)

def test_any_type_handling():
    """Test Any type validation"""
    class AnyModel(BaseModel):
        data: Any
    
    # Should accept any type
    AnyModel(data=42)
    AnyModel(data="string")
    AnyModel(data={"complex": object()})

@pytest.mark.skip(reason="Not implemented yet")
def test_forward_references():
    """Test forward references in type hints"""
    class Node(BaseModel):
        value: int
        next: Optional["Node"] = None
    
    node1 = Node(value=1)
    node2 = Node(value=2, next=node1)
    
    assert node2.next.value == 1
    
    # Invalid forward reference
    with pytest.raises(TypeError):
        Node(value=3, next="invalid")

def test_large_complex_model():
    """Test very large and complex model"""
    class BigModel(BaseModel):
        id: Union[int, str]
        metadata: Dict[str, Any]
        items: List[Dict[str, Union[int, float, str]]]
        nested: Optional[List[List[Dict[str, Address]]]]
        counter: ClassVar[int] = 0
    
    valid_data = {
        "id": "123e4567-e89b-12d3-a456-426614174000",
        "metadata": {"version": 1.0, "active": True},
        "items": [
            {"a": 1, "b": 2.5},
            {"c": "three", "d": 4}
        ],
        "nested": [
            [{"main": Address(street="123 Main", zipcode=12345)}],
            [{"secondary": Address(street="456 Oak", zipcode="67890")}]
        ]
    }
    
    obj = BigModel(**valid_data)
    assert len(obj.items) == 2
    assert obj.nested[1][0]["secondary"].zipcode == "67890"

def test_error_messages():
    """Test quality of error messages"""
    class ErrorModel(BaseModel):
        age: int
        address: Address
    
    with pytest.raises(TypeError) as exc:
        ErrorModel(age="thirty", address={"street": 123, "zipcode": 456})
    
    error_msg = str(exc.value)
    assert "Expected type int, got str" in error_msg
    assert "Expected type Address, got dict" in error_msg

def test_inheritance_behavior():
    """Test model inheritance and annotation merging"""
    class ParentModel(BaseModel):
        base_field: int
        optional_field: str = "default"
    
    class ChildModel(ParentModel):
        child_field: float
        optional_field: str  # Override parent
    
    # Test valid instantiation
    obj = ChildModel(base_field=42, child_field=3.14, optional_field="custom")
    assert obj.optional_field == "custom"
    
    # Test missing parent field
    with pytest.raises(TypeError):
        ChildModel(child_field=1.618)

@pytest.mark.skip(reason="Not implemented yet")
def test_cyclic_structures():
    """Test cyclic data structures"""
    class TreeNode(BaseModel):
        value: int
        children: List["TreeNode"] = []
    
    root = TreeNode(value=0)
    child1 = TreeNode(value=1)
    child2 = TreeNode(value=2)
    root.children = [child1, child2]
    
    assert len(root.children) == 2
    assert root.children[0].value == 1

def test_generic_containers():
    """Test various generic container types"""
    from typing import Tuple, Set
    
    class ContainerModel(BaseModel):
        tuple_data: Tuple[int, str]
        set_data: Set[float]
    
    # Valid case
    ContainerModel(
        tuple_data=(42, "answer"),
        set_data={3.14, 2.718}
    )
    
    # Invalid container types
    with pytest.raises(TypeError):
        ContainerModel(
            tuple_data=("answer", 42),  # Wrong order
            set_data={1, 2, 3}
        )

def test_validation_performance(capsys):
    """Test performance with large datasets"""
    class BigDataModel(BaseModel):
        matrix: List[List[int]]
    
    # 1000x1000 matrix
    data = [[i * 1000 + j for j in range(1000)] for i in range(1000)]
    
    with capsys.disabled():
        obj = BigDataModel(matrix=data)
        assert len(obj.matrix) == 1000
        assert obj.matrix[999][999] == 999999