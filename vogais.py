import re
import classes

def vogais(foo):
    foo = finais(foo)
    foo = nasais(foo)
    return foo

def finais(foo):
    foo = re.sub(r"e(?=\s|$)", "i", foo)   
    foo = re.sub(r"o(?=\s|$)", "u", foo)
    return foo

def nasais(foo):
    foo = re.sub("a(?=" + classes.c_nasais + classes.c_vogais + ")", "ɐ̃", foo)
    foo = re.sub("a" + classes.c_nasais + "(?=" + classes.c_consoantes + ")", "ɐ̃", foo)
    foo = re.sub("e(?=" + classes.c_nasais + classes.c_vogais + ")", "ẽ", foo)
    foo = re.sub("e" + classes.c_nasais + "(?=" + classes.c_consoantes + ")", "ẽ", foo)
    foo = re.sub("i(?=" + classes.c_nasais + classes.c_vogais + ")", "ĩ", foo)
    foo = re.sub("i" + classes.c_nasais + "(?=" + classes.c_consoantes + ")", "ĩ", foo)
    foo = re.sub("o(?=" + classes.c_nasais + classes.c_vogais + ")", "õ", foo)
    foo = re.sub("o" + classes.c_nasais + "(?=" + classes.c_consoantes + ")", "õ", foo)
    foo = re.sub("u(?=" + classes.c_nasais + classes.c_vogais + ")", "ũ", foo)
    foo = re.sub("u" + classes.c_nasais + "(?=" + classes.c_consoantes + ")", "ũ", foo)
    return foo