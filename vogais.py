import re
import classes

def vogais(foo):
    foo = nasais(foo)
    return foo

def nasais(foo):
    if(re.search("a(?=" + classes.c_nasais + classes.c_vogais + ")", foo)):
        foo = re.sub("a(?=" + classes.c_nasais + classes.c_vogais + ")", "ɐ̃", foo)
    if(re.search("a(?=" + classes.c_nasais + ")(?=" + classes.c_consoantes + ")", foo)):
        foo = re.sub("a" + classes.c_nasais + "(?=" + classes.c_consoantes + ")", "ɐ̃", foo)
    if(re.search("e(?=" + classes.c_nasais + classes.c_vogais + ")", foo)):
        foo = re.sub("e(?=" + classes.c_nasais + classes.c_vogais + ")", "ẽ", foo)
    if(re.search("e(?=" + classes.c_nasais + ")(?=" + classes.c_consoantes + ")", foo)):
        foo = re.sub("e" + classes.c_nasais + "(?=" + classes.c_consoantes + ")", "ẽ", foo)
    if(re.search("i(?=" + classes.c_nasais + classes.c_vogais + ")", foo)):
        foo = re.sub("i(?=" + classes.c_nasais + classes.c_vogais + ")", "ĩ", foo)
    if(re.search("i(?=" + classes.c_nasais + ")(?=" + classes.c_consoantes + ")", foo)):
        foo = re.sub("i" + classes.c_nasais + "(?=" + classes.c_consoantes + ")", "ĩ", foo)
    if(re.search("o(?=" + classes.c_nasais + classes.c_vogais + ")", foo)):
        foo = re.sub("o(?=" + classes.c_nasais + classes.c_vogais + ")", "õ", foo)
    if(re.search("o(?=" + classes.c_nasais + ")(?=" + classes.c_consoantes + ")", foo)):
        foo = re.sub("o" + classes.c_nasais + "(?=" + classes.c_consoantes + ")", "õ", foo)
    if(re.search("u(?=" + classes.c_nasais + classes.c_vogais + ")", foo)):
        foo = re.sub("u(?=" + classes.c_nasais + classes.c_vogais + ")", "ũ", foo)
    if(re.search("u(?=" + classes.c_nasais + ")(?=" + classes.c_consoantes + ")", foo)):
        foo = re.sub("u" + classes.c_nasais + "(?=" + classes.c_consoantes + ")", "ũ", foo)
    return foo