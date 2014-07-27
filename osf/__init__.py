from .grammar import *
from .classes import *

LineParser = Line.parser()


def parse_line(line):
    line = line.strip()
    if not line: return None
    return LineParser.parse_string(line)


def parse_lines(lines):
    for line in lines:
        lline = parse_line(line)
        if lline:
            yield lline


def hhmmss_to_seconds(hh, mm, ss, hundredths):
    val = int(ss) + int(mm) * 60 + int(hh) * 60 * 60
    if hundredths: val += int(hundredths) / 1000
    return val


def objectify_line_time(line, osf_line, time_offset=0):
    time_hhmmss = line.find(HHMMSSTime)
    time_unix = line.find(UnixTime)

    if time_hhmmss:
        hun = time_hhmmss.find(HHMMSSHundredthsComponent)
        hun_val = 0
        if hun:
            hun_val = hun.string

        osf_line.time = hhmmss_to_seconds(time_hhmmss.find(HHMMSSTimeHourComponent).string,
                                          time_hhmmss.find(HHMMSSTimeMinuteComponent).string,
                                          time_hhmmss.find(HHMMSSSecondComponent).string,
                                          hun_val)
    elif time_unix:
        osf_line.time = int(time_unix.string) - time_offset
    else:
        osf_line.time = None


def objectify_line_text(line, osf_line):
    osf_line.text = line.find(Text).string


def objectify_line_link(line, osf_line):
    link = line.find(Link)
    if link:
        osf_line.link = link[1].string


def f7(seq):
    seen = set()
    seen_add = seen.add
    return [ x for x in seq if not (x in seen or seen_add(x))]


def objectify_line_tags(line, osf_line):
    tags = line.find_all(Tag)
    osf_line.tags = f7([tag[1].string for tag in tags])


def objectify_line_indentation(line, osf_line):
    osf_line.indentation = len(line.find_all(Indentation))


def objectify_line(line, time_offset=0):
    osf_line = OSFLine()

    objectify_line_time(line, osf_line, time_offset)
    objectify_line_text(line, osf_line)
    objectify_line_link(line, osf_line)
    objectify_line_tags(line, osf_line)
    objectify_line_indentation(line, osf_line)

    return osf_line


def objectify_lines(lines):
    if not lines:
        return []

    time_offset = 0

    unix_time = lines[0].find(UnixTime)

    if unix_time:
        time_offset = int(unix_time.string)

    return [objectify_line(line, time_offset) for line in lines]
