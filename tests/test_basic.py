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


@pytest.mark.xfail(strict=True)
def test_simple_substitution():
    message = {'a': 'b'}
    mtransform(message, {'x': ' specials/$message->{a}'})
    assert message['x'] == 'b'
