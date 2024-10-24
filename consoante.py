import re

def consoante(palavra_selecionada):
    palavra_selecionada = re.sub("qu","k",palavra_selecionada)
    palavra_selecionada = re.sub("j", "ʒ", palavra_selecionada)
    palavra_selecionada = re.sub("lh", "ʎ", palavra_selecionada) 
    palavra_selecionada = re.sub("nh", "ɲ", palavra_selecionada)
    return palavra_selecionada
