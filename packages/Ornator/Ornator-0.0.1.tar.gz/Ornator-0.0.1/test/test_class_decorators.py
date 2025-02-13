import pytest
from datetime import datetime

from ornator.class_decorator import AfterClassDecorator, BaseClassDecorator, BeforeClassDecorator, DualClassDecorator, EmptyClassDecorator
from ornator.decorator import AfterDecorator, BeforeDecorator


def test_base_class_decorator():
    decorator = BaseClassDecorator()
    
    # Test pre property
    with pytest.raises(TypeError):
        decorator.pre = "not callable"
    
    def valid_func(): pass
    decorator.pre = valid_func
    assert decorator.pre == valid_func
    
    # Test pos property 
    with pytest.raises(TypeError):
        decorator.pos = "not callable"
    decorator.pos = valid_func
    assert decorator.pos == valid_func

def test_before_class_decorator():
    decorator = BeforeClassDecorator()
    
    def pre_handler(cls, *args, **kwargs):
        return f"pre_value_{kwargs.get('extra', '')}"
    
    decorator.pre = pre_handler
    
    @decorator.before(extra="test")
    class Target:
        def __init__(self):
            self.value = self._pre_value
    
    instance = Target()
    assert instance.value == "pre_value_test"
    
    # Test missing pre handler
    decorator2 = BeforeClassDecorator()
    @decorator2.before()
    class Target2:
        def __init__(self): pass
    
    with pytest.raises(ValueError, match="Missing pre function"):
        Target2()

def test_after_class_decorator():
    decorator = AfterClassDecorator()
    
    def pos_handler(cls, **kwargs):
        class Modified(cls):
            def get_value(self):
                return f"modified_{kwargs.get('extra', '')}"
        return Modified
    
    decorator.pos = pos_handler
    
    @decorator.after(extra="test")
    class Target:
        pass
    
    instance = Target()
    assert instance.get_value() == "modified_test"
    
    # Test missing pos handler
    decorator2 = AfterClassDecorator()
    with pytest.raises(ValueError, match="Missing pos function"):
        @decorator2.after()
        class Target2:
            pass

def test_dual_class_decorator():
    decorator = DualClassDecorator()
    
    def pre_handler(cls, *args, **kwargs):
        return f"pre_value_{kwargs.get('extra', '')}"
    
    def pos_handler(cls, **kwargs):
        class Modified(cls):
            def get_value(self):
                return f"{self._pre_value}_modified_{kwargs.get('extra', '')}"
        return Modified
    
    decorator.pre = pre_handler
    decorator.pos = pos_handler
    
    @decorator.dual(extra="test")
    class Target:
        pass
    
    instance = Target()
    assert instance.get_value() == "pre_value_test_modified_test"
    
    # Test missing handlers
    decorator2 = DualClassDecorator()
    with pytest.raises(ValueError, match="Missing pre or pos functions"):
        @decorator2.dual()
        class Target2:
            pass

def test_empty_class_decorator():
    decorator = EmptyClassDecorator()
    
    def custom_handler(cls, **kwargs):
        class Modified(cls):
            def get_value(self):
                return f"custom_{kwargs.get('extra', '')}"
        return Modified
    
    @decorator.empty(handler=custom_handler, extra="test")
    class Target:
        pass
    
    instance = Target()
    assert instance.get_value() == "custom_test"
    
    # Test invalid handler
    with pytest.raises(TypeError):
        @decorator.empty(handler="not callable")
        class Target2:
            pass
    
    # Test without handler
    @decorator.empty()
    class Target3:
        def get_value(self):
            return "plain_value"
    
    instance = Target3()
    assert instance.get_value() == "plain_value"

# Integration tests
def test_function_decorator_integration():
    # Ejemplo de uso combinado de decoradores
    before_dec = BeforeDecorator()
    after_dec = AfterDecorator()
    
    def pre_handler(*args, **kwargs):
        return datetime.now()
    
    def pos_handler(result, **kwargs):
        return f"Processed at {result}"
    
    before_dec.pre = pre_handler
    after_dec.pos = pos_handler
    
    @after_dec.after()
    @before_dec.before()
    def process_data(pre, data):
        return f"{data} at {pre}"
    
    result = process_data("test_data")
    assert "test_data" in result
    assert "Processed at" in result

def test_class_decorator_integration():
    before_dec = BeforeClassDecorator()
    after_dec = AfterClassDecorator()
    
    def pre_handler(cls, *args, **kwargs):
        return datetime.now()
    
    def pos_handler(cls, **kwargs):
        class Modified(cls):
            def get_info(self):
                return f"Created at {self._pre_value}"
        return Modified
    
    before_dec.pre = pre_handler
    after_dec.pos = pos_handler
    
    @after_dec.after()
    @before_dec.before()
    class DataProcessor:
        def __init__(self, data):
            self.data = data
    
    processor = DataProcessor("test_data")
    assert "Created at" in processor.get_info()
    assert isinstance(processor._pre_value, datetime)