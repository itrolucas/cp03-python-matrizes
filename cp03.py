temperaturas = [
    [28, 31, 34, 33],
    [25, 27, 29, 28],
    [32, 35, 36, 34],
    [24, 26, 25, 27]
]



media = 0
maior_risco = 0
sala_maior_risco = 0
for sala in range(len(temperaturas)):
    print(f'\nSala {sala+1}: ')
    soma = 0
    array_sala = temperaturas[sala]
    contador_critico = 0
    for temp in array_sala:
        soma += temp
        if temp >= 33:
            contador_critico += 1

    if maior_risco < contador_critico:
        maior_risco = contador_critico
        sala_maior_risco = sala + 1
    media = soma/len(array_sala)
    print(f"Média: {media}")
    print(f"Registros críticos: {contador_critico}")

print()
print(f'Sala com maior risco: Sala {sala_maior_risco}')




