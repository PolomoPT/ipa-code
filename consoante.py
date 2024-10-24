import re

def consoante(seleção):
    seleção = re.sub("qu","k",seleção)
    seleção = re.sub("j", "ʒ", seleção)
    seleção = re.sub("lh", "ʎ", seleção) 
    seleção = re.sub("nh", "ɲ", seleção)
    return seleção
