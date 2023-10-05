segunda = int(input('votos de segunda feira '))
terca = int(input('votos terca feira '))
quarta = int(input('votos quarta feira '))
quinta = int(input('votos quinta feira '))
sexta = int(input('votos sexta feira '))

# Checar dia com maior número de votos
dia_escolhido = ""
votos_maximos = max(segunda, terca, quarta, quinta, sexta)
if votos_maximos == segunda:
    dia_escolhido = "segunda-feira"
elif votos_maximos == terca:
    dia_escolhido = "terça-feira"
elif votos_maximos == quarta:
    dia_escolhido = "quarta-feira"
elif votos_maximos == quinta:
    dia_escolhido = "quinta-feira"
else:
    dia_escolhido = "sexta-feira"

# Dia escolhido
print("O dia escolhido para a realização das lives é:", dia_escolhido)