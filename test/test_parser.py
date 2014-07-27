import pytest
import osf
import osf.grammar


def test_time_hhmmss():
    result = osf.grammar.Time.parser().parse_string('01:02:03.123')

    assert result.find(osf.grammar.HHMMSSTimeHourComponent).string == '01'
    assert result.find(osf.grammar.HHMMSSTimeMinuteComponent).string == '02'
    assert result.find(osf.grammar.HHMMSSSecondComponent).string == '03'
    assert result.find(osf.grammar.HHMMSSHundredthsComponent).string == '123'


def test_time_hhmmss_no_hundredths():
    result = osf.grammar.Time.parser().parse_string('01:02:03')

    assert result.find(osf.grammar.HHMMSSTimeHourComponent).string == '01'
    assert result.find(osf.grammar.HHMMSSTimeMinuteComponent).string == '02'
    assert result.find(osf.grammar.HHMMSSSecondComponent).string == '03'


def test_time_unix():
    result = osf.grammar.Time.parser().parse_string('1406359385')

    assert result.find(osf.grammar.UnixTime).string == '1406359385'


def test_line_basic():
    result = osf.parse_line("01:02:03   asd bla      <foo>   #bla     #foo")

    assert result.find(osf.grammar.HHMMSSTime).string == '01:02:03'
    assert result.find(osf.grammar.Text).string == 'asd bla'
    assert result.find(osf.grammar.Link)[1].string == 'foo'

    tags = result.find_all(osf.grammar.Tag)
    assert len(tags) == 2
    assert tags[0][1].string == 'bla'
    assert tags[1][1].string == 'foo'


def test_line_real():
    result = osf.parse_line("- 02:24:20  The Computer (How It Works)  <http://www.amazon.com/dp/072140619X/>   #shopping")

    assert len(result.find_all(osf.grammar.Indentation)) == 1

    assert result.find(osf.grammar.HHMMSSTime).string == '02:24:20'
    assert result.find(osf.grammar.Text).string == 'The Computer (How It Works)'
    assert result.find(osf.grammar.Link)[1].string == 'http://www.amazon.com/dp/072140619X/'

    tags = result.find_all(osf.grammar.Tag)
    assert len(tags) == 1
    assert tags[0][1].string == 'shopping'


def test_line_no_tags():
    result = osf.parse_line("01:02:03 asd bla <foo>")

    assert result.find(osf.grammar.HHMMSSTime).string == '01:02:03'
    assert result.find(osf.grammar.Text).string == 'asd bla'
    assert result.find(osf.grammar.Link)[1].string == 'foo'


def test_line_indentation():
    result = osf.parse_line("-- a")

    assert len(result.find_all(osf.grammar.Indentation)) == 2


def test_line_link_no_space():
    result = osf.parse_line("01:02:03 asd bla<foo>")

    assert result.find(osf.grammar.HHMMSSTime).string == '01:02:03'
    assert result.find(osf.grammar.Text).string == 'asd bla'
    assert result.find(osf.grammar.Link)[1].string == 'foo'

def test_line_no_link():
    result = osf.parse_line("01:02:03 asd bla")

    assert result.find(osf.grammar.HHMMSSTime).string == '01:02:03'
    assert result.find(osf.grammar.Text).string == 'asd bla'


def test_line_no_link_tag():
    result = osf.parse_line("01:02:03 asd bla #tag1 #tag2")

    tags = result.find_all(osf.grammar.Tag)
    assert len(tags) == 2
    assert tags[0][1].string == 'tag1'
    assert tags[1][1].string == 'tag2'


def test_line_tag_escape():
    result = osf.parse_line(r"01:02:03 asd \#bla")

    assert result.find(osf.grammar.HHMMSSTime).string == '01:02:03'
    assert result.find(osf.grammar.Text).string == r'asd \#bla'


def test_lines():
    result = list(osf.parse_lines(['A', '   ', 'B']))

    assert len(result) == 2
    assert result[0].find(osf.grammar.Text).string == 'A'
    assert result[1].find(osf.grammar.Text).string == 'B'
