import pytest
import osf.timeutils


def test_seconds_to_hhmmss():
    result = osf.timeutils.seconds_to_hhmmss(56011.123)
    assert result == '15:33:31.123'


def test_hhmmss_to_seconds():
    result = osf.timeutils.hhmmss_to_seconds(3, 31, 50, 123)
    assert result == 12710.123
