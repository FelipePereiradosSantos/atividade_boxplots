import pandas as pd
import matplotlib as plt

df_atividade = pd.read_csv("atividade.csv")

df_atividade.plot(kind='box')