import pytest
import osf
import osf.grammar

def test_nsfw_88():
    f = open('./test/data/nsfw-88.txt')
    lines = f.readlines()
    f.close()

    result = osf.objectify_lines(osf.parse_lines(lines))
    #print("\n".join([str(line) for line in result]))
