import matplotlib
matplotlib.use('TkAgg')  # Define o backend gráfico correto
import matplotlib.pyplot as plt
import pandas as pd

def create_histogram(data, column, bins=30, title="Histograma", 
                    xlabel="Valores", ylabel="Frequência", figsize=(10,6), color='skyblue'):
    """
    Cria um histograma
    
    Parâmetros:
    data (pd.DataFrame): DataFrame com os dados
    column (str): Nome da coluna para criar o histograma
    bins (int): Número de bins do histograma
    """
    plt.figure(figsize=figsize)
    plt.hist(data[column], bins=bins, color=color, edgecolor='black')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True, alpha=0.3)
    return plt.gcf() 

# Criando um DataFrame de exemplo
df = pd.DataFrame({'Valores': [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]})

# Gerando o histograma e salvando como imagem
fig = create_histogram(df, 'Valores')
fig.savefig("histograma.png")

# Exibir o gráfico na tela
plt.show()