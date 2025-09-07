import pandas
import matplotlib.pyplot

matplotlib.pyplot.style.use('seaborn-v0_8-whitegrid')

df_vendas = pandas.read_excel(r"C:\Users\leoog\OneDrive\Área de Trabalho\Proj. Análise de Dados\Plan01.xlsx")

df_vendas = df_vendas.rename(columns={
    'Preço Unitário' : 'Preco',
    'Data Venda': 'Data',
    'ID Venda': 'ID',
})

df_vendas["Total"] = df_vendas['Quantidade'] * df_vendas['Preco']

Total_vendedor = df_vendas.groupby('Vendedor')['Total'].sum().sort_values(ascending=True)

matplotlib.pyplot.figure(figsize=(10,6))
Total_vendedor.plot(kind='bar')
matplotlib.pyplot.title("Maiores Vendedores")
matplotlib.pyplot.xlabel("Vendedores")
matplotlib.pyplot.ylabel("Total de vendas")
matplotlib.pyplot.show()

