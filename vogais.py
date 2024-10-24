import re
import classes

def vogais(seleção):
    seleção = finais(seleção)
    seleção = nasais(seleção)
    return seleção

def finais(seleção):
    seleção = re.sub(r"e(?=\s|$)", "i", seleção)   
    seleção = re.sub(r"o(?=\s|$)", "u", seleção)
    return seleção

def nasais(seleção):
    seleção = re.sub("a(?=" + classes.c_nasais + classes.c_vogais + ")", "ɐ̃", seleção)
    seleção = re.sub("a" + classes.c_nasais + "(?=" + classes.c_consoantes + ")", "ɐ̃", seleção)
    seleção = re.sub("e(?=" + classes.c_nasais + classes.c_vogais + ")", "ẽ", seleção)
    seleção = re.sub("e" + classes.c_nasais + "(?=" + classes.c_consoantes + ")", "ẽ", seleção)
    seleção = re.sub("i(?=" + classes.c_nasais + classes.c_vogais + ")", "ĩ", seleção)
    seleção = re.sub("i" + classes.c_nasais + "(?=" + classes.c_consoantes + ")", "ĩ", seleção)
    seleção = re.sub("o(?=" + classes.c_nasais + classes.c_vogais + ")", "õ", seleção)
    seleção = re.sub("o" + classes.c_nasais + "(?=" + classes.c_consoantes + ")", "õ", seleção)
    seleção = re.sub("u(?=" + classes.c_nasais + classes.c_vogais + ")", "ũ", seleção)
    seleção = re.sub("u" + classes.c_nasais + "(?=" + classes.c_consoantes + ")", "ũ", seleção)
    return seleção