from imblearn.under_sampling import NearMiss
import pandas as pd

# Para balancear os dados, utilizamos o NearMiss do imblearn
# O NearMiss é um método de subamostragem que tenta balancear as classes minoritárias
# ao invés de gerar novos dados, ele remove amostras da classe majoritária
# Isso é útil quando temos um conjunto de dados desbalanceado, como no nosso caso. Mesmo assim ainda nossos dados ficarao desbalanceados, mas com uma proporção melhor entre as classes.
# De acordo com fontes da internet e ChatGpt, a escolha da versão 3 do NearMiss é a mais adequada para o nosso caso, pois ela tenta manter a distribuição das classes minoritárias em relação à classe majoritária, o que pode ser útil quando temos um número muito maior de amostras da classe majoritária.
# O hasGame foi criado apartir do nosso algoritmo de geração de tabuleiros que não tem vencedor e não tem empate com todas as posições ocupadas.
# O tie foi criado na mão e para verificar o tabuleiro foi usado nosso algoritmo de geração e vericação de tabuleiros que verifica se todos os espaços tem 1 e 0, e verifica se foi empate ou não. Ele não foi usado para criar os empates pois estava demorando muito para gerar o resultado esperado.
# Foi criado apartir do algoritmo de geração e vericação de tabuleiros algumas vitorias de X e O, para ter mais diversidade no nosso dataset. E juntando todos os dados utilizamos o NearMiss para balancear os dados.


data = pd.read_csv('./data/dados_finais_300.csv', header=None)
X = data.iloc[:, :9]
Y = data.iloc[:, 9]

nm = NearMiss(version=3)
X_balanceado, Y_balanceado = nm.fit_resample(X, Y)

# Junta e salva
df_resultado = pd.concat([X_balanceado, Y_balanceado], axis=1)
df_resultado.to_csv('xwin_owin_balanceado.csv', index=False)
