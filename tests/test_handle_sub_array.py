import sys
sys.path.append('..')
sys.path.append('.')
from message_transform import mtransform  # noqa: E402


def test_basic_array():
    message = {'a': 'b'}
    mtransform(message, {'x': ['a', {'key': ' specials/foo$message->{a}bar'}]})
    assert message['x'][0] == 'a'
    assert message['x'][1]['key'] == 'foobbar'
