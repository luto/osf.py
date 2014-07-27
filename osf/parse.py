from .grammar import Line
from modgrammar import ParseError

LineParser = Line.parser()


def parse_line(line):
    line = line.strip()
    if not line: return None
    return LineParser.parse_string(line)


def parse_lines(lines):
    num = -1

    for line in lines:
        num += 1

        lline = None

        try:
            lline = parse_line(line)
        except ParseError as e:
            e.line = num
            yield e

        if lline:
            yield lline
