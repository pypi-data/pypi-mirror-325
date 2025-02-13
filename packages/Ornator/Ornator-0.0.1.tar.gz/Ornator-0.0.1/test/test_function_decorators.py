import pytest
from datetime import datetime

from ornator.decorator import AfterDecorator, BaseDecorator, BeforeDecorator, DualDecorator, EmptyDecorator

def test_base_decorator():
    decorator = BaseDecorator()
    
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

def test_before_decorator():
    decorator = BeforeDecorator()
    
    def pre_handler(*args, **kwargs):
        return f"pre_value_{kwargs.get('extra', '')}"
    
    decorator.pre = pre_handler
    
    @decorator.before(extra="test")
    def target(pre, *args, **kwargs):
        return f"target_{pre}"
    
    result = target()
    assert result == "target_pre_value_test"
    
    # Test missing pre handler
    decorator2 = BeforeDecorator()
    @decorator2.before()
    def target2(pre, *args, **kwargs): pass
    
    with pytest.raises(ValueError, match="Missing pre function"):
        target2()

def test_after_decorator():
    decorator = AfterDecorator()
    
    def pos_handler(result, **kwargs):
        return f"{result}_{kwargs.get('extra', '')}"
    
    decorator.pos = pos_handler
    
    @decorator.after(extra="test")
    def target(*args, **kwargs):
        return "target_value"
    
    result = target()
    assert result == "target_value_test"
    
    # Test missing pos handler
    decorator2 = AfterDecorator()
    @decorator2.after()
    def target2(*args, **kwargs): pass
    
    with pytest.raises(ValueError, match="Missing pos function"):
        target2()

def test_dual_decorator():
    decorator = DualDecorator()
    
    def pre_handler(*args, **kwargs):
        return f"pre_value_{kwargs.get('extra', '')}"
    
    def pos_handler(result, **kwargs):
        return f"{result}_{kwargs.get('extra', '')}"
    
    decorator.pre = pre_handler
    decorator.pos = pos_handler
    
    @decorator.dual(extra="test")
    def target(pre, *args, **kwargs):
        return f"target_{pre}"
    
    result = target()
    assert result == "target_pre_value_test_test"
    
    # Test missing handlers
    decorator2 = DualDecorator()
    @decorator2.dual()
    def target2(pre, *args, **kwargs): pass
    
    with pytest.raises(ValueError, match="Missing pre or pos functions"):
        target2()

def test_empty_decorator():
    decorator = EmptyDecorator()
    
    def custom_handler(func, *args, **kwargs):
        return f"custom_{func(*args, **kwargs)}_{kwargs.get('extra', '')}"
    
    @decorator.empty(handler=custom_handler, extra="test")
    def target(*args, **kwargs):
        return "target_value"
    
    result = target()
    assert result == "custom_target_value_test"
    
    # Test invalid handler
    with pytest.raises(TypeError):
        @decorator.empty(handler="not callable")
        def target2(*args, **kwargs): pass
    
    # Test without handler
    @decorator.empty()
    def target3(*args, **kwargs):
        return "plain_value"
    
    result = target3()
    assert result == "plain_value"
