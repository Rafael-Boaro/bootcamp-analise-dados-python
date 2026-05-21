import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np
import sqlite3
import json

conn = sqlite3.connect('dados.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY,
        produtos TEXT,
        preco REAL,
        ano INTEGER
    )
''')
cursor.execute('''
    INSERT INTO produtos (produtos, preco, ano) VALUES
    ('notebook', 1500.0, 2025),
    ('desktop', 2000.0, 2020),
    ('tablet', 1030.0, 2023)
    ''')

conn.commit()

cursor.execute('SELECT * FROM produtos')
dados = cursor.fetchall()
conn.close()

with open('dados.json', 'w') as f:
    json.dump(dados, f)

dados =  pd.DataFrame(dados, columns=['id', 'produtos', 'preco', 'ano'])

dados_df = pd.DataFrame(dados, columns=['id', 'produtos', 'preco', 'ano']).groupby('produtos')['preco'].mean().reset_index()
print(f'Dados dos produtos:\n')
print(f'{dados_df}\n')
print(f'Média dos preços: {dados["preco"].mean()}\n')
print(dados_df.describe())

plt.bar(dados_df['produtos'], dados_df['preco'])
plt.title('Preços dos Produtos')
plt.xlabel('Produtos em estoque')
plt.ylabel('Preço')
plt.show()