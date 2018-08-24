import sys
sys.path.append('..')
sys.path.append('.')
from message_transform import mtransform  # noqa: E402


def test_simple_left_array_substitution_single():
    message = {'a': 'b', 'c': ['d']}
    mtransform(message, {' specials/$message->{c}': 'x'})
    assert message['d'] == 'x'


def test_simple_left_array_substitution():
    message = {'a': 'b', 'c': ['d', 'e']}
    mtransform(message, {' specials/$message->{c}': 'x'})
    assert message['d'] == 'x'
    assert message['e'] == 'x'


def test_left_array_substitution():
    message = {'a': 'b', 'c': ['d', 'e']}
    mtransform(message, {' specials/x$message->{c}y': 'x'})
    assert message['xdy'] == 'x'
    assert message['xey'] == 'x'
