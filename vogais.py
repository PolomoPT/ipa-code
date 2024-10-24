import re
import classes

def vogais(seleção):
    seleção = monotongos_nasais(seleção)
    seleção = ditongos_nasais(seleção)
    seleção = vogais_acentuadas
    seleção = finais(seleção)
    return seleção

def finais(seleção):
    seleção = re.sub(r"e(?=\s|$)", "i", seleção)   
    seleção = re.sub(r"o(?=\s|$)", "u", seleção)
    return seleção

def vogais_acentuadas(seleção):
    seleção = re.sub("á", "a", seleção)
    seleção = re.sub("é", "ɛ", seleção)
   #seleção = re.sub("ê", "e", seleção)
   #seleção = re.sub("í", "i", seleção)
    seleção = re.sub("ó", "ɔ", seleção)
    seleção = re.sub("ô", "o", seleção)
   #seleção = re.sub("ú", "u", seleção)

def monotongos_nasais(seleção):
    seleção = re.sub("ã(?![o|e])", "ɐ̃", seleção)
    seleção = re.sub("[a|â](?="+classes.c_nasais+classes.c_vogais+")", "ɐ̃", seleção)
    seleção = re.sub("[a|â]"+classes.c_nasais+"(?="+classes.c_consoantes+")", "ɐ̃", seleção)
    seleção = re.sub("[e|ê](?="+classes.c_nasais+classes.c_vogais+")", "ẽ", seleção)
    seleção = re.sub("[e|ê]"+classes.c_nasais+"(?="+classes.c_consoantes+")", "ẽ", seleção)
    seleção = re.sub("[i|í](?="+classes.c_nasais+classes.c_vogais+")", "ĩ", seleção)
    seleção = re.sub("[i|í]"+classes.c_nasais+"(?="+classes.c_consoantes+")", "ĩ", seleção)
   #seleção = re.sub("õ(?!e)", "õ", seleção)
    seleção = re.sub("[o|ô](?="+classes.c_nasais+classes.c_vogais+")", "õ", seleção)
    seleção = re.sub("[o|ô]"+classes.c_nasais+"(?="+classes.c_consoantes+")", "õ", seleção)
    seleção = re.sub("[u|ú](?="+classes.c_nasais+classes.c_vogais+")", "ũ", seleção)
    seleção = re.sub("[u|ú]so"+classes.c_nasais+"(?="+classes.c_consoantes+")", "ũ", seleção)
    return seleção

def ditongos_nasais(seleção):
    seleção = re.sub("[ãe|âim]", "ɐ̃j̃", seleção) ## âim para câimbra
    seleção = re.sub("ão", "ɐ̃w̃", seleção)
    seleção = re.sub("õe", "õj̃", seleção)
    return seleção