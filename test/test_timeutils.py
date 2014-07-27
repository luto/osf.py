import pytest
import osf.timeutils


def test_seconds_to_hhmmss_1():
    result = osf.timeutils.seconds_to_hhmmss(56011.123)
    assert result == '15:33:31.123'


def test_seconds_to_hhmmss_sec_zero_fill():
    result = osf.timeutils.seconds_to_hhmmss(55981.123)
    assert result == '15:33:01.123'


def test_seconds_to_hhmmss_min_zero_fill():
    result = osf.timeutils.seconds_to_hhmmss(54211.123)
    assert result == '15:03:31.123'


def test_seconds_to_hhmmss_hr_zero_fill():
    result = osf.timeutils.seconds_to_hhmmss(18211.123)
    assert result == '05:03:31.123'


def test_seconds_to_hhmmss_hun_zero_fill():
    result = osf.timeutils.seconds_to_hhmmss(18211.011)
    assert result == '05:03:31.011'


def test_seconds_to_hhmmss_no_hundredths():
    result = osf.timeutils.seconds_to_hhmmss(18211)
    assert result == '05:03:31.000'


def test_hhmmss_to_seconds():
    result = osf.timeutils.hhmmss_to_seconds(3, 31, 50, 123)
    assert result == 12710.123
