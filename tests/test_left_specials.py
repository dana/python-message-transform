import sys
sys.path.append('..')
sys.path.append('.')
from message_transform import mtransform  # noqa: E402


def test_left_simple_substitution():
    message = {'a': 'b'}
    mtransform(message, {' specials/$message->{a}': 'x'})
    assert message['b'] == 'x'


def test_left_less_simple_substitution():
    message = {'a': 'b'}
    mtransform(message, {' specials/X$message->{a}fOO': 'x'})
    assert message['XbfOO'] == 'x'
