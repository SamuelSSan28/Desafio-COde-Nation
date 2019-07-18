import json
import string
import hashlib, os

import requests

a = list(string.ascii_lowercase)

def buscaABC(letra):
    if letra == '.' or letra == ',':
        return -1
    else:
        return a.index(letra)


def desemcripta(palavra):
    palavra = list(palavra)
    for i in range(len(palavra)):
        index = buscaABC(palavra[i])
        if(index >= 0):
            r = a[::-1]
            if (index-8) < 0:
                index = 8 - index -1
                palavra[i] = r[index]
            else:
                 palavra[i] = a[index-8]


    return palavra




cifrado = "bpm smg bw xmznwzuivkm qa mtmoivkm, vwb jibbitqwva wn axmkqit kiama. rwv jmvbtmg, lwco ukqtzwg"
cifrado = cifrado.split()
texto = []
d = []
separator = ''


for i in range(len(cifrado)):
    d = desemcripta(cifrado[i])
    texto.append(separator.join(d))

separator = ' '
decifrado = separator.join(texto)
print(decifrado)

salt = os.urandom(32).hex()
hash = hashlib.sha1()
hash.update(('%s' % (decifrado)).encode('utf-8'))
hashCode = hash.hexdigest()
print(hashCode)


#Criando o dicionario
j = {'decifrado': decifrado,
'resumo_criptografico': hashCode}

#Salvando o dicionario como json
def escrever_json(dic):
    with open('answer.json', 'w') as f:
        json.dump(dic, f)
        escrever_json(j)

#Carreguei o arquivo para fazer uma leitura e ver que foi salvo corretamente
def carregar_json(arquivo):
    with open('answer.json', 'r' ) as f:
        return json.load(f)

answer = {'answer': open('answer.json','rb')}
r = requests.post('https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=5c0aad2400f31ce9f4bfc363fa1ecf527aa37ec2', files=answer)
print(r.status_code, r.reason)
