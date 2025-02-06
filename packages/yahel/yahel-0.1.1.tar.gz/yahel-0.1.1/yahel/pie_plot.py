import matplotlib
matplotlib.use('TkAgg')  # Define o backend gráfico correto
import matplotlib.pyplot as plt
import pandas as pd

def create_pie_plot(data, values, labels, title="Gráfico de Pizza", figsize=(8,8)):
    """
    Cria um gráfico de pizza
    
    Parâmetros:
    data (pd.DataFrame): DataFrame com os dados
    values (str): Nome da coluna com os valores
    labels (str): Nome da coluna com os rótulos
    """
    plt.figure(figsize=figsize)
    plt.pie(data[values], labels=data[labels], autopct='%1.1f%%', startangle=90)
    plt.title(title)
    return plt.gcf() 

# Criando um DataFrame de exemplo
df = pd.DataFrame({
    'Categoria': ['A', 'B', 'C', 'D'],
    'Valores': [25, 30, 15, 30]
})

# Gerando o gráfico de pizza e salvando como imagem
fig = create_pie_plot(df, 'Valores', 'Categoria')
fig.savefig("grafico_pizza.png")

# Exibir o gráfico na tela
plt.show()
