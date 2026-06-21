import pandas as pd
import matplotlib.pyplot as plt

# 1. Carregar CSV

df = pd.read_csv(
    "vendas.csv",
    parse_dates=["data"]
)

print(df.head())

# 2. Calcular vendas por mês

# Criar coluna Receita
df["receita"] = df["quantidade"] * df["preco"]

print(df.head())

# Criar coluna Mês
df["mes"] = df["data"].dt.to_period("M")

#Calcular vendas por mês
vendas_por_mes = df.groupby("mes")["receita"].sum()

print("\nVendas por mês:")
print(vendas_por_mes)

# 3. Produto mais vendido

# Produto mais vendido
vendas_produto = df.groupby("produto").agg({
    "quantidade": "sum",
    "receita": "sum"
})

# Descobrir o campeão em quantidade
mais_vendido = vendas_produto["quantidade"].idxmax()

print(
    f"\nProduto mais vendidos: {mais_vendido}"
)

# 4. Produto com maior receita

maior_receita = vendas_produto["receita"].idxmax()

print(
    f"Produto com maior receita: {maior_receita}"
)

# 5. Gerar gráficos

#Gráfico de vendas por mês
vendas_por_mes.index = vendas_por_mes.index.astype(str)

plt.figure(figsize=(8, 5))

vendas_por_mes.plot(kind="bar")

plt.title("Vendas por Mês")
plt.xlabel("Mês")
plt.ylabel("Receita (R$)")

plt.tight_layout()

plt.savefig("venda_por_mes.png")

plt.show()

# Top 5 produtos

top5 = vendas_produto.nlargest(
    5,
    "receita"
)

plt.figure(figsize=(8, 5))

plt.bar(
    top5.index,
    top5["receita"]
)

plt.title(
    "Top 5 Produtos por Receita"
)

plt.xlabel("Produto")
plt.ylabel("Receita (R$)")

plt.tight_layout()

plt.savefig(
    "top5_produtos.png"
)

plt.show()
