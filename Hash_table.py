import math
import os
import random
import re
import sys
from collections import Counter
def checkMagazine(magazine, note):
    a = Counter(magazine)
    b = Counter(note)
    if a&b==b:
        print("Yes")
    else:
        print("No")    
