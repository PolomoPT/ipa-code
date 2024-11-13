import re
import classes

def vogais(seleção):
    seleção = monotongos_nasais(seleção)
    seleção = ditongos_nasais(seleção)
    seleção = vogais_acentuadas(seleção)
    seleção = finais(seleção)
    return seleção

def finais(seleção):
    seleção = re.sub("e$", "i", seleção)   
    seleção = re.sub("o$", "u", seleção)
    seleção = re.sub("a$", "ɐ", seleção)
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
    seleção = re.sub("[a|â][m|n]$", "ɐ̃", seleção)

    seleção = re.sub("[e|ê](?=j̃)", "ẽj̃", seleção)
    seleção = re.sub("[e|ê](?=[m|n]["+classes.vogais+"])", "ẽj̃", seleção)
    seleção = re.sub("[e|ê|é][m|n]"+"(?=["+classes.consoantes+"])", "ẽj̃", seleção)
    seleção = re.sub("[e|ê|é][m|n]$", "ẽj̃", seleção)

    seleção = re.sub("[i|í](?=j̃)", "ĩj̃", seleção)
    seleção = re.sub("[i|í](?=[m|n]["+classes.vogais+"])", "ĩj̃", seleção)
    seleção = re.sub("[i|í][m|n]"+"(?=["+classes.consoantes+"])", "ĩj̃", seleção)
    seleção = re.sub("[i|í][m|n]$", "ĩj̃", seleção)

    seleção = re.sub("õ(?!e)", "õw̃", seleção)
    seleção = re.sub("[o|ô](?=j̃)", "õw̃", seleção)
    seleção = re.sub("[o|ô](?=[m|n]["+classes.vogais+"])", "õw̃", seleção)
    seleção = re.sub("[o|ô][m|n]"+"(?=["+classes.consoantes+"|$])", "õw̃", seleção)
    seleção = re.sub("[o|ô][m|n]$", "õw̃", seleção)

    seleção = re.sub("[u|ú](?=j̃)", "ũw̃", seleção)
    seleção = re.sub("[u|ú](?=[m|n]["+classes.vogais+"])", "ũw̃", seleção)
    seleção = re.sub("[u|ú][m|n]"+"(?=["+classes.consoantes+"|$])", "ũw̃", seleção)
    seleção = re.sub("[u|ú][m|n]$", "ũw̃", seleção)
    return seleção

def ditongos_nasais(seleção):
    seleção = re.sub("ãe", "ɐ̃j̃", seleção) ## âim para câimbra
    seleção = re.sub("ão", "ɐ̃w̃", seleção)
    seleção = re.sub("õe", "õj̃", seleção)
    seleção = re.sub("ẽj̃$", "ẽj̃", seleção)
    return seleção