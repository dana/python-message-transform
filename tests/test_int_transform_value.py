import sys
sys.path.append('..')
sys.path.append('.')
from message_transform import mtransform  # noqa: E402


def test_simplest_transform():
    message = {}
    transform = {'x': 'y', 'foo': 123}

    mtransform(message, transform)
    assert message['x'] == 'y'
    assert message['foo'] == 123
