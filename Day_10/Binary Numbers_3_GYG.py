![10](https://user-images.githubusercontent.com/56713634/72675457-bb177100-3ac7-11ea-97bf-45d313c7856c.jpg)
import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input())
    binary = format(n,'b')
    max_consecutive = 0;
    consecutive = 0;
    for number in binary:
        consecutive = consecutive + 1 if int(number) else 0
        max_consecutive = consecutive if max_consecutive < consecutive else max_consecutive
    print(max_consecutive)
