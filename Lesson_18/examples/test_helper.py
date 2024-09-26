import sys


def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    msg = (
        f"Test at line {linenum} ok." if did_pass else f"Test at line {linenum} FAILED."
    )
    print(msg)
