import sys
sys.path.append('..')
sys.path.append('.')
from message_transform import mtransform  # noqa: E402


def test_simple_key_transform():
    message = {'a': 'b'}
    mtransform(message, {' specials/$message->{a}': ' specials/$message->{a}'})
    assert message['b'] == 'b'
