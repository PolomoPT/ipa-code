import re
import classes
##CARALHO TROQUEI O ŋ PELO j̃ EM TUDO E A TRADUÇÃO DO NH PAROU DE FUNCIONAR. PQP PQ TUDO Q EU PROGRAMO DA ERRADO, SFD
def consoante(seleção):
    seleção = re.sub("qu","k",seleção)
    seleção = re.sub("j", "ʒ", seleção)
    seleção = re.sub("lh", "ʎ", seleção) 
    seleção = re.sub("nh", "j̃", seleção)
    seleção = re.sub(r"(?<=[\s|^])r", "ʁ", seleção)
    seleção = re.sub(r"r(?=[\s|$"+classes.consoantes+"])", "ʁ", seleção)
    seleção = re.sub("rr", "ʁ", seleção)
    seleção = re.sub("r(?=["+classes.l_vogais+"])", "ɾ", seleção)
    ## seleção re.sub ("b", "b", seleção)
    seleção = re.sub("c(?=[e|é|ê|i|í])", "s", seleção)
    ## seleção = re.sub("c(?=[a|á|ã|â|o|ó|ô|õ|u|ú])", "k", seleção) não funciona, mas não há problemas.
    ## E o seleção re.sub para o Ç?
    ## seleção re.sub ("d", "d", seleção)
    ## seleção re.sub ("f", "f", seleção)
    ##seleção = re.sub("g(?=[e|é|ê|i|í])", "ʒ", seleção) não funciona, mas não há problemas.
    ##seleção = re.sub("g(?=[a|á|ã|â|o|ó|ô|õ|u|ú])", "g", seleção) não funciona, mas não há problemas.
    return seleção
