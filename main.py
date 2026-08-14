vendas = [
    [1200, 1500, 1100],
    [1000, 1300, 1400],
    [900, 1700, 1600]
    ]

num_vendedor = len(vendas)
num_mes = len(vendas[0])


for vendedor in range(num_vendedor):
    for mes in range(num_mes):
            print(f"O {vendedor+1} vendedor vendeu no {mes+1} mÃªs R${vendas[vendedor][mes]}")

for vendedor in range(num_vendedor):
    print(f"A soma das vendas do {vendedor+1} vendedor Ã© {sum(vendas[vendedor])}")

for mes in range(num_mes):
    totalmes = 0
    for vendedor in range(num_vendedor):
        totalmes += vendas[vendedor][mes]
    print(f"Total mÃªs {mes+1}: R$ {totalmes}")

total = 0
for i in vendas:
    total = sum(i) + total
print(f"O total das vendas da empresa Ã© {total}")

maiorvenda = 0
melhor = 0

for vendedor in range(num_vendedor):
    if maiorvenda < sum(vendas[vendedor]):
        maiorvenda = sum(vendas[vendedor])
        melhor = 1 + vendedor
print(f"O melhor vendedor e o {melhor} com o total de: R${maiorvenda}")