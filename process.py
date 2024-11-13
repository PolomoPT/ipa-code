import tonicas
import consoante
import vogais
import re

seleção = input()
seleção_array = seleção.split()

i = 0
while i < len(seleção_array):
    pós_consoante = consoante.consoante(seleção_array[i])
    pós_vogal = vogais.vogais(pós_consoante)
    result = pós_vogal
    result = re.sub("-", "", result) ##remoção de hífens
    print(result)
    i += 1


