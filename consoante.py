import re
import classes

def consoante(seleção):
    seleção = re.sub("qu","k",seleção)
    seleção = re.sub("j", "ʒ", seleção)
    seleção = re.sub("lh", "ʎ", seleção) 
    seleção = re.sub("nh", "ɲ", seleção)
    seleção = re.sub(r"(?<=[\s|^])r", "ʁ", seleção)
    seleção = re.sub(r"r(?=[\s|$"+classes.consoantes+"])", "ʁ", seleção)
    seleção = re.sub("rr", "ʁ", seleção)
    seleção = re.sub("r(?=["+classes.l_vogais+"])", "ɾ", seleção)
    return seleção
