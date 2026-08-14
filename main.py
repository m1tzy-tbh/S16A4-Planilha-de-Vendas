# linhas = vendedores
# colunas = meses

vendas = [
    [100, 200, 150],
    [250, 300, 200],
    [150, 100, 250]
]

# Etapa 1 - Exibição organizada
print("VENDAS POR VENDEDOR")

for i in range(len(vendas)):
    print(f"Vendedor {i}: ", end="")
    
    for j in range(len(vendas[i])):
        print(vendas[i][j], end=" ")
    
    print()

print("\nQuantidade de linhas:", len(vendas))
print("Quantidade de colunas:", len(vendas[0]))


# Etapa 2 - Total por vendedor
print("\nTOTAL POR VENDEDOR")

for i in range(len(vendas)):
    total = 0  # reinicia o acumulador para cada vendedor

    for j in range(len(vendas[i])):
        total += vendas[i][j]

    print(f"Total vendedor {i}: {total}")


# Etapa 3 - Total por mês
print("\nTOTAL POR MÊS")

for j in range(len(vendas[0])):
    total = 0  # reinicia o acumulador para cada mês

    for i in range(len(vendas)):
        total += vendas[i][j]

    print(f"Total mês {j}: {total}")


# Etapa 4 - Total geral
total_geral = 0

for i in range(len(vendas)):
    for j in range(len(vendas[i])):
        total_geral += vendas[i][j]

print("\nTOTAL GERAL")
print("Total geral da empresa:", total_geral)


# Etapa 5 - Melhor vendedor
melhor_vendedor = 0
maior_total = 0

for i in range(len(vendas)):
    total = 0

    for j in range(len(vendas[i])):
        total += vendas[i][j]

    if total > maior_total:
        maior_total = total
        melhor_vendedor = i

print("\nMELHOR VENDEDOR")
print(f"Melhor vendedor: vendedor {melhor_vendedor}")