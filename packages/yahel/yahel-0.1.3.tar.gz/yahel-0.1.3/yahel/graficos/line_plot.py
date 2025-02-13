import matplotlib
matplotlib.use('TkAgg')  # Define o backend gráfico correto
import matplotlib.pyplot as plt
import pandas as pd

def create_line_plot(data, x_column, y_column, title="Gráfico de Linha", 
                    xlabel="Eixo X", ylabel="Eixo Y", figsize=(10,6), color='blue'):
    """
    Cria um gráfico de linha simples
    
    Parâmetros:
    data (pd.DataFrame): DataFrame com os dados
    x_column (str): Nome da coluna para o eixo X
    y_column (str): Nome da coluna para o eixo Y
    """
    plt.figure(figsize=figsize)
    plt.plot(data[x_column], data[y_column], marker='o', color=color)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True, alpha=0.3)
    return plt.gcf() 

# Criando um DataFrame de exemplo
df = pd.DataFrame({
    'Meses': ['Jan', 'Fev', 'Mar', 'Abr'],
    'Vendas': [100, 150, 130, 200]
})

# Gerando o gráfico de linha e salvando como imagem
fig = create_line_plot(df, 'Meses', 'Vendas')
fig.savefig("grafico_linha.png")

# Exibir o gráfico na tela
plt.show()