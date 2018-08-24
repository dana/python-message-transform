import sys
sys.path.append('..')
sys.path.append('.')
from message_transform import mtransform  # noqa: E402


def test_simple_array_append():
    message = {'a': ['b', 'c']}
    mtransform(message, {'a': 'd'})
    assert 'b' in message['a']
    assert 'd' in message['a']


def test_array_array_append():
    message = {'a': ['b', 'c']}
    mtransform(message, {'a': ['d', 'e']})
    assert 'b' in message['a']
    assert 'd' in message['a']
    assert 'e' in message['a']
