import sys
sys.path.append('..')
sys.path.append('.')
from message_transform import mtransform  # noqa: E402


def test_no_over_write():
    message = {'a': 'b'}
    mtransform(message, {'.transform_control': {'no_over_write': True}, 'a': 'c'})  # noqa: E501
    assert message['a'] == 'b'
