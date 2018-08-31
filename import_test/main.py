
import os
import sys

from sub.sub_1 import sub1_show


if __name__ == "__main__":
    sub1_show()

    dirs = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(dirs)

    print(sys.path)

