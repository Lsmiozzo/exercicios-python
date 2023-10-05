

soma_impares = 0
soma_pares = 0


media_impares = 0
media_pares = 0



# Notas dos alunos ímpares
for i in range(1, 50, 2):
    print(f"VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS ÍMPARES.")
    nota = float(input(f"POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {i}: "))
    soma_impares += nota

# Notas dos alunos pares
for i in range(2, 51, 2):
    print(f"VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES.")
    nota = float(input(f"POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {i}: "))
    soma_pares += nota

# Das médias
media_impares = soma_impares / 25
media_pares = soma_pares / 25

# Apuração da metade da sala que obteve a maior média
if media_impares > media_pares:
    print("A metade ímpar da sala teve a maior nota.")
elif media_pares > media_impares:
    print("A metade par da sala teve a maior nota.")
else:
    print("As duas metades da sala tiveram notas iguais.")


print(f"Média dos alunos ímpares: {media_impares}")
print(f"Média dos alunos pares: {media_pares}")
