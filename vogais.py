import re
import classes

def vogais(palavra_selecionada):
    palavra_selecionada = finais(palavra_selecionada)
    palavra_selecionada = nasais(palavra_selecionada)
    return palavra_selecionada

def finais(palavra_selecionada):
    palavra_selecionada = re.sub(r"e(?=\s|$)", "i", palavra_selecionada)   
    palavra_selecionada = re.sub(r"o(?=\s|$)", "u", palavra_selecionada)
    return palavra_selecionada

def nasais(palavra_selecionada):
    palavra_selecionada = re.sub("a(?=" + classes.c_nasais + classes.c_vogais + ")", "ɐ̃", palavra_selecionada)
    palavra_selecionada = re.sub("a" + classes.c_nasais + "(?=" + classes.c_consoantes + ")", "ɐ̃", palavra_selecionada)
    palavra_selecionada = re.sub("e(?=" + classes.c_nasais + classes.c_vogais + ")", "ẽ", palavra_selecionada)
    palavra_selecionada = re.sub("e" + classes.c_nasais + "(?=" + classes.c_consoantes + ")", "ẽ", palavra_selecionada)
    palavra_selecionada = re.sub("i(?=" + classes.c_nasais + classes.c_vogais + ")", "ĩ", palavra_selecionada)
    palavra_selecionada = re.sub("i" + classes.c_nasais + "(?=" + classes.c_consoantes + ")", "ĩ", palavra_selecionada)
    palavra_selecionada = re.sub("o(?=" + classes.c_nasais + classes.c_vogais + ")", "õ", palavra_selecionada)
    palavra_selecionada = re.sub("o" + classes.c_nasais + "(?=" + classes.c_consoantes + ")", "õ", palavra_selecionada)
    palavra_selecionada = re.sub("u(?=" + classes.c_nasais + classes.c_vogais + ")", "ũ", palavra_selecionada)
    palavra_selecionada = re.sub("u" + classes.c_nasais + "(?=" + classes.c_consoantes + ")", "ũ", palavra_selecionada)
    return palavra_selecionada