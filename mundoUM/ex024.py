#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cid = str(input('Digite um nome de uma cidade: ')).strip()
print(cid[0:5].upper()=='SANTO')