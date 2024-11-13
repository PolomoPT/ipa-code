import tonicas
import consoante
import vogais
import re

seleção = input()
seleção_array = seleção.split()

i = 0
while i < len(seleção_array):
    seleção_array[i] = re.sub("-", "", seleção_array[i]) ##remoção de hífens
    pós_consoante = consoante.consoante(seleção_array[i])
    pós_vogal = vogais.vogais(pós_consoante)
    result = pós_vogal
    print(result)
    i += 1


