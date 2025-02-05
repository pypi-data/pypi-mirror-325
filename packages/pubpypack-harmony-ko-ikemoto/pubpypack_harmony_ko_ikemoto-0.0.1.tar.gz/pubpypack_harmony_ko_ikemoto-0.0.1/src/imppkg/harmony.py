# handler function
import sys
from imppkg.harmonic_mean import harmonic_mean_1
import termcolor

def main():
    result = 0.0
    try:
        nums = [float(i) for i in sys.argv[1:]]
    except ValueError:
        nums = []

    try:
        result = harmonic_mean_1(nums)
    except ZeroDivisionError:
        pass

    termcolor.cprint(result, 'red', 'on_cyan', attrs=['bold'])
