from imblearn.under_sampling import NearMiss
import pandas as pd

data = pd.read_csv('newdata.csv', header=None)
X = data.iloc[:, :9]
Y = data.iloc[:, 9]

nm = NearMiss(version=3)
X_balanceado, Y_balanceado = nm.fit_resample(X, Y)

# Junta e salva
df_resultado = pd.concat([X_balanceado, Y_balanceado], axis=1)
df_resultado.to_csv('dados_balanceados.csv', index=False)
