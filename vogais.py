import re
import classes

def vogais(seleção):
    seleção = ditongos_nasais(seleção)
    seleção = finais(seleção)
    seleção = ditongos_orais(seleção)
    seleção = monotongos_nasais(seleção)
    seleção = vogais_acentuadas(seleção)
    return seleção

def ditongos_orais(seleção):
    seleção = re.sub("ai", "aj", seleção)
    seleção = re.sub("au", "aw", seleção)
    seleção = re.sub("ei", "ej", seleção)
    seleção = re.sub("eu", "ew", seleção)
    seleção = re.sub("éi", "ɛj", seleção)
    seleção = re.sub("éu", "ɛw", seleção)
    seleção = re.sub("iu", "iw", seleção)
    seleção = re.sub("oi", "oj", seleção)
    seleção = re.sub("ou", "ow", seleção)
    seleção = re.sub("ói", "ɔj", seleção)
    seleção = re.sub("óu", "ɔw", seleção)
    seleção = re.sub("ui", "uj", seleção)
    return seleção

def finais(seleção):
    seleção = re.sub("e$", "i", seleção)
    seleção = re.sub("es$", "is", seleção)
    seleção = re.sub("io$", "ju", seleção)
    seleção = re.sub("ios$", "jus", seleção)
    seleção = re.sub("(?<!i)o$", "u", seleção)
    seleção = re.sub("(?<!i)os$", "us", seleção)
    seleção = re.sub("a$", "ɐ", seleção)
    seleção = re.sub("as$", "ɐs", seleção)
    return seleção

def vogais_acentuadas(seleção):
    seleção = re.sub("á", "a", seleção)
    seleção = re.sub("é", "ɛ", seleção)
    seleção = re.sub("ê", "e", seleção)
    seleção = re.sub("í", "i", seleção)
    seleção = re.sub("ó", "ɔ", seleção)
    seleção = re.sub("ô", "o", seleção)
    seleção = re.sub("ú", "u", seleção)
    return seleção

def monotongos_nasais(seleção):
    seleção = re.sub("ã(?![o|e])", "ɐ̃", seleção)
    seleção = re.sub("[a|â](?=j̃)", "ɐ̃", seleção)
    seleção = re.sub("[a|â](?=[m|n]["+classes.l_vogais+classes.vogais+"])", "ɐ̃", seleção)
    seleção = re.sub("[a|â][m|n]"+"(?=["+classes.consoantes+"|$])", "ɐ̃", seleção)
    seleção = re.sub("[a|â][m|n]$", "ɐ̃", seleção)

    seleção = re.sub("[e|ê](?=j̃)", "ẽ", seleção)
    seleção = re.sub("[e|ê](?=[m|n]["+classes.l_vogais+classes.vogais+"])", "ẽ", seleção)
    seleção = re.sub("[e|ê|é][m|n]"+"(?=["+classes.consoantes+"])", "ẽj̃", seleção)
    seleção = re.sub("[e|ê|é][m|n]$", "ẽj̃", seleção)

    seleção = re.sub("[i|í](?=j̃)", "ĩ", seleção)
    seleção = re.sub("[i|í](?=[m|n]["+classes.l_vogais+classes.vogais+"])", "ĩ", seleção)
    seleção = re.sub("[i|í][m|n]"+"(?=["+classes.consoantes+"])", "ĩj̃", seleção)
    seleção = re.sub("[i|í][m|n]$", "ĩj̃", seleção)

    seleção = re.sub("õ(?!e)", "õ", seleção)
    seleção = re.sub("[o|ô](?=j̃)", "õ", seleção)
    seleção = re.sub("[o|ô](?=[m|n]["+classes.l_vogais+classes.vogais+"])", "õ", seleção)
    seleção = re.sub("[o|ô][m|n]"+"(?=["+classes.consoantes+"|$])", "õw̃", seleção)
    seleção = re.sub("[o|ô][m|n]$", "õw̃", seleção)

    seleção = re.sub("[u|ú](?=j̃)", "ũ", seleção)
    seleção = re.sub("[u|ú](?=[m|n]["+classes.l_vogais+classes.vogais+"])", "ũ", seleção)
    seleção = re.sub("[u|ú][m|n]"+"(?=["+classes.consoantes+"|$])", "ũw̃", seleção)
    seleção = re.sub("[u|ú][m|n]$", "ũw̃", seleção)
    return seleção

def ditongos_nasais(seleção):
    seleção = re.sub("ãe", "ɐ̃j̃", seleção) ## âim para câimbra
    seleção = re.sub("ão", "ɐ̃w̃", seleção)
    seleção = re.sub("õe", "õj̃", seleção)
    seleção = re.sub("ẽj̃$", "ẽj̃", seleção)
    return seleção