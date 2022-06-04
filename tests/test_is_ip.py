import pytest
from flask.helpers import is_ip


def test_FTF():
    """
    if ip is in valid format
    if ip is in valid ipv4 format
    if ip is not in valid ipv6 format
    """
    assert is_ip("127.0.0.1") == True


def test_FFT():
    """
    if ip is in valid format
    if ip is not in valid ipv4 format
    if ip is in valid ipv6 format
    """
    assert is_ip("2001:db8:3333:4444:5555:6666:7777:8888") == True


def test_TFF():
    """
    if ip is in invalid format
    if ip is not in valid ipv4 format
    if ip is not in valid ipv6 format
    """
    assert is_ip("256.0.0.0") == False
    assert is_ip("56FE::2159:5BBC::6594") == False
    assert is_ip("123:0.1:500") == False
