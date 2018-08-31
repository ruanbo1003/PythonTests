
import sys

print(sys.path)

from obj_file import val
from usr_val import use_val_func


if __name__ == "__main__":
    val.show()
    use_val_func()

    print(globals())

    pass
