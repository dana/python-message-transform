import pytest
import sys
sys.path.append('..')
sys.path.append('.')
from message_transform import mtransform  # noqa: E402


def test_simplest_transform():
    message = {'a': 'b'}
    mtransform(message, {'x': 'y'})
    assert message['x'] == 'y'


def test_nested_transform():
    message = {'a': 'b'}
    mtransform(message, {'x': 'y', 'c': {'d': 'e'}})
    assert message['x'] == 'y'
    assert message['c']['d'] == 'e'


def test_simple_substitution():
    message = {'a': 'b'}
    mtransform(message, {'x': ' specials/$message->{a}'})
    assert message['x'] == 'b'


def test_undefined_special():
    message = {'a': 'b'}
    mtransform(message, {'x': ' specialundefined$message->{a}'})
    assert message['x'] == ' specialundefined$message->{a}'


def test_multi_level_special():
    message = {'a': {'b': 'c'}}
    mtransform(message, {'x': ' specials/A$message->{a}{b}foo'})
    assert message['x'] == 'Acfoo'


@pytest.mark.xfail(strict=True)
def test_definitely_fail():
    assert 'x' == 'y'
