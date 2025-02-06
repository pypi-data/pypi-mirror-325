import matplotlib
matplotlib.use('TkAgg')  # Define o backend gráfico correto
import matplotlib.pyplot as plt
import pandas as pd

def create_bar_plot(data, x_column, y_column, title="Gráfico de Barras", 
                   xlabel="Eixo X", ylabel="Eixo Y", figsize=(10,6), color='skyblue'):
    """
    Cria um gráfico de barras simples
    
    Parâmetros:
    data (pd.DataFrame): DataFrame com os dados
    x_column (str): Nome da coluna para o eixo X
    y_column (str): Nome da coluna para o eixo Y
    """
    plt.figure(figsize=figsize)
    plt.bar(data[x_column], data[y_column], color=color)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.3)
    return plt.gcf()

# Criando um DataFrame de exemplo
df = pd.DataFrame({
    'Meses': ['Jan', 'Fev', 'Mar', 'Abr'],
    'Vendas': [100, 150, 130, 200]
})

# Gerando o gráfico de barras e salvando como imagem
fig = create_bar_plot(df, 'Meses', 'Vendas')
fig.savefig("grafico_barras.png")

# Exibir o gráfico na tela
plt.show()
