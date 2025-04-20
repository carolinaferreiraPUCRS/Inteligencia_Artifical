import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv("./data/dados.csv")  # Dataset original com coluna 'class'

df_train, df_test = train_test_split(
    df, 
    test_size=0.2, 
    stratify=df["class"], 
    random_state=42
)

df_train.to_csv("dados_treinamento_1.csv", index=False)
df_test.to_csv("dados_teste_1.csv", index=False)
