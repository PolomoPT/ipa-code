import re
import classes

def vogais(seleção):
    seleção = monotongos_nasais(seleção)
    seleção = ditongos_nasais(seleção)
    seleção = vogais_acentuadas(seleção)
    seleção = finais(seleção)
    return seleção

def finais(seleção):
    seleção = re.sub(r"e(?=\s|$)", "i", seleção)   
    seleção = re.sub(r"o(?=\s|$])", "u", seleção)
    seleção = re.sub(r"a(?=\s|$)", "ɐ", seleção)
    return seleção

def vogais_acentuadas(seleção):
    seleção = re.sub("á", "a", seleção)
    seleção = re.sub("é", "ɛ", seleção)
   #seleção = re.sub("ê", "e", seleção)
   #seleção = re.sub("í", "i", seleção)
    seleção = re.sub("ó", "ɔ", seleção)
    seleção = re.sub("ô", "o", seleção)
   #seleção = re.sub("ú", "u", seleção)
    return seleção

def monotongos_nasais(seleção):
    seleção = re.sub("ã(?![o|e])", "ɐ̃", seleção)
    seleção = re.sub("[a|â](?=j̃)", "ɐ̃", seleção)
    seleção = re.sub("[a|â](?=[m|n]["+classes.vogais+"])", "ɐ̃", seleção)
    seleção = re.sub("[a|â][m|n]"+"(?=["+classes.consoantes+"|$])", "ɐ̃", seleção)

    seleção = re.sub("[e|ê](?=j̃)", "ẽ", seleção)
    seleção = re.sub("[e|ê](?=[m|n]["+classes.vogais+"])", "ẽ", seleção)
    seleção = re.sub("[e|ê|é][m|n]"+"(?=["+classes.consoantes+"|$])", "ẽ", seleção)

    seleção = re.sub("[i|í](?=j̃)", "ĩ", seleção)
    seleção = re.sub("[i|í](?=[m|n]["+classes.vogais+"])", "ĩ", seleção)
    seleção = re.sub("[i|í][m|n]"+"(?=["+classes.consoantes+"|$])", "ĩ", seleção)

    seleção = re.sub("õ(?!e)", "õ", seleção)
    seleção = re.sub("[o|ô](?=j̃)", "õ", seleção)
    seleção = re.sub("[o|ô](?=[m|n]["+classes.vogais+"])", "õ", seleção)
    seleção = re.sub("[o|ô][m|n]"+"(?=["+classes.consoantes+"|$])", "õ", seleção)

    seleção = re.sub("[u|ú](?=j̃)", "ũ", seleção)
    seleção = re.sub("[u|ú](?=[m|n]["+classes.vogais+"])", "ũ", seleção)
    seleção = re.sub("[u|ú][m|n]"+"(?=["+classes.consoantes+"|$])", "ũ", seleção)
    return seleção

def ditongos_nasais(seleção):
    seleção = re.sub("ãe", "ɐ̃j̃", seleção) ## âim para câimbra
    seleção = re.sub("ão", "ɐ̃w̃", seleção)
    seleção = re.sub("õe", "õj̃", seleção)
    seleção = re.sub("ẽ$", "ẽj̃", seleção)
    return seleção