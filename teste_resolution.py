import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


# Importando os dados
dataset = pd.read_csv('bank-full.csv', sep = ";")


#---------------------RESOLUÇÃO DA QUESTÃO 1-----------------------------------

#criando dataframe com housing loan = yes e personal loan = yes
#o dataframe housing loan = yes (housing_loan) também é usado na questão 6
housing_loan = dataset[dataset.housing != 'no']  
personal_loan = dataset[dataset.loan != 'no']

#obtendo valores de contagens para empréstimos imobiliários(housing loan) e pessoais(personal loan)
housing_profission = (housing_loan.job.value_counts()).to_dict()
loan_profission = (personal_loan.job.value_counts()).to_dict()

#Extraindo valores e índices dos dicionários de empréstimos imobiliários (profission_housing ) e pessoais (profission loan)

valores_housing = list(housing_profission.values())
index_housing = list(housing_profission.keys())

valores_loan = list(loan_profission.values())
index_loan = list(loan_profission.keys())

def plot(valor1,index1,valor2,index2):
     plt.figure(figsize=(10,4))
     plt.subplot(2,2,1)
     sns.barplot(valor1,index1)
     plt.title("Job vs Housing loan")
     plt.xlabel("Quantidade")
     plt.subplot(2,2,2)
     sns.barplot(valor2,index2)
     plt.title("Job vs Personal loan")
     plt.xlabel("Quantidade")
     plt.tight_layout()
          
plot(valores_housing,index_housing,valores_loan,index_loan)

#-----------------------RESOLUÇÃO DA QUESTÃO 2 e 3 ----------------------------

#criando novo dataframe com dados em que y=yes. Esse mesmo dataframe é usado
# nas questões 3, 5 e 6
df_pos=dataset[dataset.y != 'no']

#visualizando dados estatísticos do dataframe y=yes
df_pos.campaign.describe()

#função para cálculo de percentual
def percent(parte,total):
    return 100*parte/total

#calculando o percentual de clientes que aderiram à campanha
percent(len(df_pos),len(dataset))

#visualizando os valores de contatos e repetições para os clientes que aderiram à campanha
valor_pos = list(df_pos.campaign)

for x in set(valor_pos):
      print (x,'-',valor_pos.count(x))


#criando novo dataframe com dados em que y=no. 
df_neg=dataset[dataset.y != 'yes']
#visualizando dados estatísticos do dataframe y=no
df_neg.campaign.describe()

#calculando o percentual de clientes que não aderiram à campanha
percent(len(df_neg),len(dataset))

#visualizando os valores de contatos e repetições para os clientes que não aderiram à campanha
valor_neg = list(df_neg.campaign)

for x in set(valor_neg):
     print (x,'-',valor_neg.count(x))
    

#-----------------------RESOLUÇÃO DA QUESTÃO 4---------------------------------

#CODIFICAÇÃO DUMMY- Dummy encode

#drop_first para evitar Dummy trap

X = pd.get_dummies(dataset, prefix=['job','marital','education','default','housing','loan','contact','month','poutcome','y'],drop_first=True)
corr = X.corr()
corr_y = pd.DataFrame(corr['y_yes'].drop('y_yes'))
corr_y = corr_y.sort_values(by = 'y_yes', ascending = False)

#---------------------RESOLUÇÃO DA QUESTÃO 5-----------------------------------

#Checando as estatísticas ,para a variável "balance",dos dados contendo apenas y=yes 
df_pos.balance.describe()
#Pegando a contagem de quantos clientes estão inadimplentes
pos_counts =   (df_pos.default.values == 'yes').sum()
#Checando quantos recebem acima e abaixo da média anual
count_balance_up = (df_pos.balance.values >= 1804).sum()
count_balance_down = (df_pos.balance.values <= 1804).sum()

#--------------------RESULUÇÃO DA QUESTÃO 6------------------------------------

#Checando dados estatísticos dos clientes que possuem empréstimo imobiliário
housing_loan.describe()

temp_df = housing_loan.loc[:, 'job':'default']

for i in (temp_df).to_dict():
    a = (temp_df[i].value_counts()).to_dict()
    valores = list(a.values())
    index = list( a.keys())
    sns.barplot(valores, index)
    plt.title(i)
    plt.xlabel("quantidade")
    plt.show()
   
    
    
    
    

