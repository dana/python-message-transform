import sys
sys.path.append('..')
sys.path.append('.')
from message_transform import mtransform  # noqa: E402


def test_complex_special_substitute():
    message = {'a': 'b'}
    mtransform(message, {'x': ' specials/foo$message->{a}bar'})
    assert message['x'] == 'foobbar'


def test_deep_special_substitute():
    message = {'a': 'b'}
    mtransform(message, {'x': {'z': ' specials/$message->{a}'}})
    assert message['x']['z'] == 'b'


def test_deep_complex_special_substitute():
    message = {'a': 'a1', 'b': 'b1', 'c': 'c1', 'd': {'foo': 'd1'}}
    mtransform(message, {'x': {'z': ' specials/HEAD$message->{a}.$message->{b}.$message->{c}.$message->{d}{foo}TAIL'}})  # noqa: E501
    assert message['x']['z'] == 'HEADa1.b1.c1.d1TAIL'
    mtransform(message, {'x': {'z': ' specials/HEAD$message->{a}$message->{b}tail'}})  # noqa: E501
    assert message['x']['z'] == 'HEADa1b1tail'
    mtransform(message, {'x': {'z': ' specials/HEAD$message->{a}.$message->{d}{foo}tail'}})  # noqa: E501
    assert message['x']['z'] == 'HEADa1.d1tail'
    mtransform(message, {'x': {'z': ' specials/HEAD$message->{a}.$message->{b}.$message->{d}{foo}tail'}})  # noqa: E501
    assert message['x']['z'] == 'HEADa1.b1.d1tail'
    mtransform(message, {'x': {'z': ' specials/HEAD$message->{d}{foo}tail'}})  # noqa: E501
    assert message['x']['z'] == 'HEADd1tail'
    mtransform(message, {'x': {'z': ' specials/HEAD$message->{a}tail'}})  # noqa: E501
    assert message['x']['z'] == 'HEADa1tail'
