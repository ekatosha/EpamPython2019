from property_timer import Message
import time
import pytest


def test_msg():
    m = Message()
    assert m.msg


def test_property():
    m = Message()
    _test = m.msg
    time.sleep(6)
    _test2 = m.msg
    assert _test is not _test2


def test_test_property_timer():
    m = Message()
    _test = m.msg
    time.sleep(2)
    _test2 = m.msg
    assert _test is _test2


def test_property_param():
    m = Message()
    m.msg = 'Ahoi'
    _test = m.msg
    assert _test == 'Ahoi'


def test_property_param2():
    m = Message()
    m.msg = 'Ahoi'
    time.sleep(6)
    _test = m.msg
    assert _test != 'Ahoi'



