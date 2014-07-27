import math


def seconds_to_hhmmss(time):
    seconds = str(time % 60).zfill(2)
    minutes = str(math.floor((time / 60) % 60)).zfill(2)
    hours = str(math.floor((time / 60 / 60) % 60)).zfill(2)

    return hours + ":" + minutes + ":" + seconds


def hhmmss_to_seconds(hh, mm, ss, hundredths):
    val = int(ss) + int(mm) * 60 + int(hh) * 60 * 60
    if hundredths: val += int(hundredths) / 1000
    return val
