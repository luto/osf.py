import math


def seconds_to_hhmmss(time):
    seconds = str(time % 60).zfill(2)
    minutes = str(math.floor((time / 60) % 60)).zfill(2)
    hours = str(math.floor((time / 60 / 60) % 60)).zfill(2)

    return hours + ":" + minutes + ":" + seconds


class OSFLine():
    def __init__(self):
        self.time = None
        self.text = ""
        self.link = None
        self.tags = []
        self.indentation = 0

    def __str__(self):
        parts = []
        if self.indentation:
            parts.append('-' * self.indentation)
        if self.time is not None:
            parts.append(seconds_to_hhmmss(self.time))
        parts.append(self.text)
        if self.link:
            parts.append("<" + self.link + ">")
        parts.extend(["#" + tag for tag in self.tags])
        return " ".join(parts)
