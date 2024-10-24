import tonicas
import consoante
import vogais

seleção = input()
pós_consoante = consoante.consoante(seleção)
pós_vogal = vogais.vogais(pós_consoante)
result = pós_vogal
print(result)