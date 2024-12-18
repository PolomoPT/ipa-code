import re
import classes
## Consonants that don't change in IPA (e.g. b = /b/) are not included in this code.
def consoante(seleção):
    seleção = re.sub("^h", "", seleção)
    seleção = re.sub("(?<=["+classes.l_vogais+"])r(?=["+classes.l_vogais+"])", "ɾ", seleção)
    seleção = re.sub("(?<=["+classes.l_ataque+"])r(?=["+classes.l_vogais+"])", "ɾ", seleção)
    seleção = re.sub("(?<="+classes.l_vogais+")s(?="+classes.l_vogais+")", "z", seleção)
    seleção = re.sub("ss", "s", seleção)
    seleção = re.sub("sc(?=["+classes.l_sj+"])", "s", seleção)
    seleção = re.sub("sç", "s", seleção)
    seleção = re.sub("xc(?=["+classes.l_sj+"])", "s", seleção)
    seleção = re.sub("c(?=["+classes.l_sj+"])", "s", seleção)
    seleção = re.sub("ç", "s", seleção)
    seleção = re.sub("^s", "s", seleção)
    seleção = re.sub("s$", "s", seleção)
    seleção = re.sub("s(?=<"+classes.consoantes+classes.l_consoantes+")", "s", seleção)
    seleção = re.sub("x$", "ks", seleção)
    seleção = re.sub("x(?="+classes.consoantes+classes.l_consoantes+")", "s", seleção)
    seleção = re.sub("t(?=[i|í])", "tʃ", seleção)
    seleção = re.sub("t(?=e$)", "tʃ", seleção)
    seleção = re.sub("d(?=[i|í])", "dʒ", seleção)
    seleção = re.sub("d(?=e$)", "dʒ", seleção)
    seleção = re.sub("ch", "ʃ", seleção)
    seleção = re.sub("^x", "ʃ", seleção)
    seleção = re.sub("g(?=["+classes.l_sj+"])", "ʒ", seleção)
    seleção = re.sub("j", "ʒ", seleção)
    seleção = re.sub("nh", "j̃", seleção)
    seleção = re.sub("lh", "ʎ", seleção)
    seleção = re.sub("c(?=["+classes.l_kg+"])", "k", seleção)
    seleção = re.sub("qu(?=["+classes.l_sj+"])","k", seleção)
    seleção = re.sub("qu(?=["+classes.l_kg+"])","kʷ", seleção)
    seleção = re.sub("g(?=["+classes.l_kg+"])", "g", seleção)
    seleção = re.sub("gu(?=["+classes.l_sj+"])","g", seleção)
    seleção = re.sub("gu(?=["+classes.l_kg+"])","gʷ", seleção)
    seleção = re.sub("l$", "w", seleção)
    seleção = re.sub("l(?=["+classes.consoantes+classes.l_consoantes+"])", "w", seleção)
    seleção = re.sub("rr", "h", seleção)
    seleção = re.sub("^r", "h", seleção)
    seleção = re.sub("r(?=[$|"+classes.l_consoantes+classes.consoantes+"])", "h", seleção)
    seleção = re.sub("r$", "h", seleção)

    ##handling especial para s antes de fones sonoros
    seleção = re.sub("s(?="+classes.sonoras+")", "z", seleção)
    return seleção