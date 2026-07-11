"""
Sales Analysis Script

This script performs a basic sales analysis using Pandas and Matplotlib.
It includes data exploration, sales aggregation by month and product, and the
generation of summary charts.

Developed during the "Cursor AI + Python: Intelligent Development with AI" course
provided by Santander Open Academy.

Functionality:
- Loads sales data from CSV.
- Computes total revenue per sale.
- Aggregates sales data by month and by product.
- Identifies best-selling products by quantity and revenue.
- Generates bar charts for monthly revenue and top 5 products.

Author: [Your Name]
"""

import pandas as pd
import matplotlib.pyplot as plt


def load_sales_data(csv_file: str) -> pd.DataFrame:
    """
    Load sales data from a CSV file, parsing date columns.

    Args:
        csv_file (str): Path to the sales data CSV file.

    Returns:
        pd.DataFrame: Loaded and parsed sales DataFrame.
    """
    df = pd.read_csv(csv_file, parse_dates=["data"])
    print("First rows of loaded data:")
    print(df.head())
    return df


def add_revenue_column(df: pd.DataFrame) -> None:
    """
    Compute sale revenue and add as a new column ("receita") to the DataFrame.

    Args:
        df (pd.DataFrame): DataFrame with 'quantidade' and 'preco' columns.
    """
    df["receita"] = df["quantidade"] * df["preco"]
    print("\nFirst rows after adding 'receita' column:")
    print(df.head())


def add_month_column(df: pd.DataFrame) -> None:
    """
    Add a "mes" column representing the sale's month (period format).

    Args:
        df (pd.DataFrame): DataFrame with a 'data' (datetime) column.
    """
    df["mes"] = df["data"].dt.to_period("M")


def calculate_monthly_sales(df: pd.DataFrame) -> pd.Series:
    """
    Calculate total monthly revenue.

    Args:
        df (pd.DataFrame): DataFrame with 'mes' and 'receita' columns.

    Returns:
        pd.Series: Revenue (sum) by month.
    """
    vendas_por_mes = df.groupby("mes")["receita"].sum()
    print("\nSales by month:")
    print(vendas_por_mes)
    return vendas_por_mes


def aggregate_sales_by_product(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aggregate total quantity sold and revenue per product.

    Args:
        df (pd.DataFrame): Sales DataFrame.

    Returns:
        pd.DataFrame: Aggregated results by product.
    """
    vendas_produto = df.groupby("produto").agg({
        "quantidade": "sum",
        "receita": "sum"
    })
    return vendas_produto


def get_best_selling_product(vendas_produto: pd.DataFrame) -> str:
    """
    Identify the best-selling product by quantity.

    Args:
        vendas_produto (pd.DataFrame): Aggregated product DataFrame.

    Returns:
        str: Name of the best-selling product.
    """
    produto = vendas_produto["quantidade"].idxmax()
    print(f"\nBest-selling product (by quantity): {produto}")
    return produto


def get_highest_revenue_product(vendas_produto: pd.DataFrame) -> str:
    """
    Identify the product with the highest total revenue.

    Args:
        vendas_produto (pd.DataFrame): Aggregated product DataFrame.

    Returns:
        str: Name of the product with highest revenue.
    """
    produto = vendas_produto["receita"].idxmax()
    print(f"Product with highest revenue: {produto}")
    return produto


def plot_monthly_sales(vendas_por_mes: pd.Series, filename: str = "venda_por_mes.png") -> None:
    """
    Generate and save a bar chart of monthly sales revenue.

    Args:
        vendas_por_mes (pd.Series): Series with revenue per month.
        filename (str): Output image filename.
    """
    vendas_por_mes.index = vendas_por_mes.index.astype(str)
    plt.figure(figsize=(8, 5))
    vendas_por_mes.plot(kind="bar")
    plt.title("Vendas por Mês")
    plt.xlabel("Mês")
    plt.ylabel("Receita (R$)")
    plt.tight_layout()
    plt.savefig(filename)
    plt.show()


def plot_top_products_by_revenue(vendas_produto: pd.DataFrame, filename: str = "top5_produtos.png", top_n: int = 5) -> None:
    """
    Generate and save a bar chart of the top N products by revenue.

    Args:
        vendas_produto (pd.DataFrame): Aggregated product DataFrame.
        filename (str): Output image filename.
        top_n (int): Number of top products to show.
    """
    top_products = vendas_produto.nlargest(top_n, "receita")
    plt.figure(figsize=(8, 5))
    plt.bar(top_products.index, top_products["receita"])
    plt.title("Top 5 Produtos por Receita")
    plt.xlabel("Produto")
    plt.ylabel("Receita (R$)")
    plt.tight_layout()
    plt.savefig(filename)
    plt.show()


def main() -> None:
    """
    Main routine for performing sales data analysis and generating plots.
    """
    # 1. Load sales data
    df = load_sales_data("vendas.csv")

    # 2. Calculate sales by month
    add_revenue_column(df)
    add_month_column(df)
    vendas_por_mes = calculate_monthly_sales(df)

    # 3. Analyze sales by product
    vendas_produto = aggregate_sales_by_product(df)
    get_best_selling_product(vendas_produto)
    get_highest_revenue_product(vendas_produto)

    # 4. Generate charts
    plot_monthly_sales(vendas_por_mes, filename="venda_por_mes.png")
    plot_top_products_by_revenue(vendas_produto, filename="top5_produtos.png", top_n=5)


if __name__ == "__main__":
    main()
