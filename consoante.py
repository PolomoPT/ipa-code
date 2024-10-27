import re
import classes
## Consonants that doesn't change in IPA (e.x. b = /b/) are not included in the code.
def consoante(seleção):
    seleção = re.sub("qu(?=[e|é|ê|i|í])","k",seleção)
    seleção = re.sub("qu(?=[a|á|ã|â|o|ó|ô|õ|u|ú])","kʷ",seleção)
    seleção = re.sub("j", "ʒ", seleção)
    seleção = re.sub("lh", "ʎ", seleção) 
    seleção = re.sub("nh", "j̃", seleção)
    seleção = re.sub(r"(?<=[\s|^])r", "ʁ", seleção)
    seleção = re.sub(r"r(?=[\s|$"+classes.consoantes+"])", "ʁ", seleção)
    seleção = re.sub("rr", "ʁ", seleção)
    seleção = re.sub("r(?=["+classes.l_vogais+"])", "ɾ", seleção)
    seleção = re.sub("c(?=[e|é|ê|i|í])", "s", seleção)
    seleção = re.sub("sh", "ʃ", seleção) 
    seleção = re.sub("c(?=[a|á|ã|â|o|ó|ô|õ|u|ú])", "k", seleção)
    seleção = re.sub("ç", "s", seleção)
    seleção = re.sub("ch", "ʃ", seleção)
    seleção = re.sub("g(?=[e|é|ê|i|í])", "ʒ", seleção)
    seleção = re.sub("g(?=[a|á|ã|â|o|ó|ô|õ|u|ú])", "g", seleção)
    seleção = re.sub("gu(?=[e|é|ê|i|í])","g",seleção)
    seleção = re.sub("gu(?=[a|á|ã|â|o|ó|ô|õ|u|ú])","gʷ",seleção)
    ## seleção = re.sub ("s(?="+classes.l_vogais+")(?=<"+classes.l_vogais+")", "z", seleção) não funciona.
    seleção = re.sub("s(?=\\s|^)", "s", seleção)
    seleção = re.sub("s(?=<"+classes.consoantes+")", "s", seleção)
    seleção = re.sub("sc", "s", seleção)
    seleção = re.sub("sç", "s", seleção)
    seleção = re.sub("ss", "s", seleção)
    ## Como será o código para o X entre vogais, com som de  /ʃ/, /s/, /ks/ ou /z/?
    seleção = re.sub("x(?=\\s|^)", "ʃ", seleção)
    seleção = re.sub("x(?=\\s|$)", "ks", seleção)
    seleção = re.sub("x(?="+classes.consoantes+")", "s", seleção)
    seleção = re.sub("xc(?=[e|é|ê|i|í])", "s", seleção)
    return seleção