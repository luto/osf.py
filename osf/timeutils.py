import math


def seconds_to_hhmmss(time):
    hundredths = str(round(time % 1, 3))[2:].zfill(3)
    seconds = str(math.floor(time % 60)).zfill(2)
    minutes = str(math.floor((time / 60) % 60)).zfill(2)
    hours = str(math.floor((time / 60 / 60) % 60)).zfill(2)

    return hours + ":" + minutes + ":" + seconds + "." + hundredths


def hhmmss_to_seconds(hh, mm, ss, hundredths):
    val = int(ss) + int(mm) * 60 + int(hh) * 60 * 60
    if hundredths: val += round(int(hundredths) / 1000, 3)
    return val
