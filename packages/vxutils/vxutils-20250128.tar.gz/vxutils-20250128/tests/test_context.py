import pytest
from vxutils.context import VXContext


# 测试初始化
def test_vxcontext_initialization():
    context = VXContext()
    assert context == {}


# 测试添加键值对
def test_vxcontext_add_item():
    context = VXContext()
    context["key"] = "value"
    assert context["key"] == "value"


# 测试有序性
def test_vxcontext_order():
    context = VXContext()
    context["key1"] = "value1"
    context["key2"] = "value2"
    assert list(context.keys()) == ["key1", "key2"]


# 测试 to_json 方法
def test_vxcontext_to_json():
    context = VXContext()
    context["key"] = "value"
    json_str = to_json(context)
    assert json_str == '{"key": "value"}'
