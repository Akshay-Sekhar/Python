from collections.abc import Iterable
from typing import Any


def number(n):
    if n%2==0:
        return"Even"
    else:
        return "odd"
    
result = number(6)
print(result)        
