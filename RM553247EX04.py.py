


minutos = int(input("Digite o número de minutos atuais: "))
# Inicializar fatorial como 1
fatorial_minutos = 1

for i in range(1, minutos + 1):
    fatorial_minutos *= i

senha = "LIBERDADE" + str(fatorial_minutos)

print("A senha para desbloqueio é:", senha)





