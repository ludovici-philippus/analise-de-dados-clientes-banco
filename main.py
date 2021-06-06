#  Passo 1: Importa a base de dados.

#  Passo 2: Visualizar e tratar a base de dados.

#  Passo 3: Analisar a base de dados.

#  Passo 4: Construir uma analise para identificar o 
#           motivo ou os principais morivos dos clientes 
#           estarem cancelando o cartão de crédito


import pandas as pd
import plotly.express as px

# Passo 1:
clientesbanco_df = pd.read_csv("ClientesBanco.csv", encoding="latin1")

# Passo 2:
clientesbanco_df = clientesbanco_df.drop("CLIENTNUM", axis=1)

# Passo 3:
    # Categoria: Difere os clietes e os cancelados
    # Idade: Diz a idade.
    # Dependentes: Mostra quantas pessoas dependem daquela pessoa, como a quantidade de filhos.
    # Educação: Nível da formação da pessoa
    # Estado Cívil: Mostra se a pessoa está solteira, casada, divorciada etc...
    # Faixa Salarial Anual: Mostra a categoria do salário da pessoa no ano.
    # Categoria Cartão: Mostra o tipo de cartão que a pessoa tem.
    # Meses como cliente: Revela por quantos meses aquela pessoa foi ou está sendo cliente.
    # Produtos cadastrados: Quantos de nossos produtos o cliente tem.
    # Inatividade 12m: Nos últimos doze meses, por quantos meses ele ficou sem usar o cartão.
    # Contatos 12m: Nos últimos doze meses, quantas vezes ele precisou do nosso contato.
    # Limite: Demonstra o limite do cartão do sujeito.
    # Limite consumido: Calcula quanto do limite foi consumido.
    # Limite Disponível: Revela a quantidade ainda usável do limite.
    # Mudanças Transações_Q4_Q1: Mudanças de transações do último trimestre pro primeiro trimestre.
    # Valor Transacoes 12m: O Valor das transações nos últimos 12 meses.
    # Qtde Transacoes 12m: Quantas transações foram feitas nos últimos 12 meses.
    # Mudança Qtde Transações_Q4_Q1: 
    # Taxa de Utilização Cartão: O quanto o sujeito utilizou o cartão.

display(clientesbanco_df.info()) # Revelou que dentro da coluna categoria do
                                 # cartão, existe alguma linha com o valor vazio.
                                 # Portanto, há-de ser excluída.

clientesbanco_df = clientesbanco_df.dropna() # Excluí todas as linhas vazias.
display(clientesbanco_df.describe().round(1)) # Analisaremos agora alguns dados importantes
                                     # Como a média, o desvio padrão, o mínimo, 
                                     # o quartil e o máximo.

# Passe 4:
# Vamos avaliar como está a divisão entre Clientes X Cancelados:
qtde_categoria = clientesbanco_df["Categoria"].value_counts()
display(qtde_categoria)

qtde_categoria_perc = clientesbanco_df["Categoria"].value_counts(normalize=True).round(2)
display(qtde_categoria_perc)

# Existem várias formas de descobrirmos o motivo dos cancelamentos:
    # - Podemos olhar a comparação em cada uma das colunas da nossa base de dados,
    #   para ver se essa informação traz algum insight novo.

for coluna in clientesbanco_df:
    if coluna == "Categoria":
        continue
    grafico = px.histogram(clientesbanco_df, x=coluna, color="Categoria")
    grafico.show()
# Conclusões:
    # 1 - A partir de 6 contatos todos os clientes cancelam e de 2 a 3 contatos tem altas taxas, 
    #     portanto um dos motivos do cancelamento é a falta/problemas de suporte.
    # 2 - Clientes com inatividade nos últimos 12 meses de 2 e 3 meses apresentam taxas relativamente altas de abandono.
    # 3 - Aqueles que tem 0% de taxa de utilização do Cartão representam uma grande faixa dos cancelamentos.
    # 4 - Pessoas com quantidades de transação abaixo de 60 tem altas chances de cancelarem.
    # 5 - Sujeitos que tiveram um Valor de Transações abaixo de 3 mil nos últimos 12 meses, tem altas chances de cancelarem.
    # 6 - Pessoas que consumiram do limite menos de 650, tem uma tendência quase certa de abandono.
    # 7 - Aqueles que tem um limite inferior a 3500 possuem mais chance de cancelamento.
    # 8 - A maior parte dos cancelamentos vem daquels com uma faixa salarial abaixo de 40 mil dólares.
# Conclusão geral:
# O suporte e a inatividade são os maiores fatores para o cancelamento.
# Provavelmente, a inativaidade é devida a problemas de renda, pois os canceladores
# tem pouco uso do limite, baixo limite, cartão blue e estão na mais baixa faixa-salarial.
# Talvez uma solução interessante seja a criação de incentivos para o uso do cartão.
