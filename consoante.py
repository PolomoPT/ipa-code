import re

def consoante(foo):
    foo = re.sub("qu","k",foo)
    foo = re.sub ("j", "ʒ", foo)
    return foo

## for i in range(0 ,len(seleção), 2):
        