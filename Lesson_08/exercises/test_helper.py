import sys


def test(did_pass):
    line_num = sys._getframe(1).f_lineno  #
    if did_pass:
        msg = f"Test at line {line_num} ok."
    else:
        msg = f"Test at line {line_num} FAILED."
    print(msg)