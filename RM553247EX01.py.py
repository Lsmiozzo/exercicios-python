tipo_assinatura = input('informe tipo de assinatura ')
faturamento_anual= float(input('informe valor do faturamento anual '))
if tipo_assinatura == "Basic":
    porcentagem = 0.3
elif tipo_assinatura == "Silver":
    porcentagem = 0.2
elif tipo_assinatura == "Gold":
    porcentagem = 0.1
elif tipo_assinatura == "Platinum":
    porcentagem = 0.05
else:
    print("Assinatura inválida.")

    # Valor do bônus
bonus = faturamento_anual * porcentagem
print("O valor do bônus que o cliente deve pagar é de R${:,.2f}.".format(bonus))



