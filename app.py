import streamlit as st
import sqlite3

# Conecta ou cria banco de dados
conn = sqlite3.connect('microempreendedores.db', check_same_thread=False)
cursor = conn.cursor()

# Cria a tabela se não existir
cursor.execute('''
CREATE TABLE IF NOT EXISTS empreendedores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    servico TEXT NOT NULL,
    telefone TEXT,
    instagram TEXT,
    endereco TEXT
)
''')
conn.commit()

st.title("Cadastro de Microempreendedores da Comunidade")

# Formulário para adicionar
with st.form(key='form_cadastro'):
    nome = st.text_input("Nome")
    servico = st.text_input("Tipo de Serviço")
    telefone = st.text_input("Telefone")
    instagram = st.text_input("Instagram")
    endereco = st.text_input("Endereço/Bairro")
    enviar = st.form_submit_button("Cadastrar")

    if enviar:
        if nome and servico:
            cursor.execute('''
                INSERT INTO empreendedores (nome, servico, telefone, instagram, endereco)
                VALUES (?, ?, ?, ?, ?)
            ''', (nome, servico, telefone, instagram, endereco))
            conn.commit()
            st.success(f"✅ {nome} cadastrado com sucesso!")
        else:
            st.error("Nome e Tipo de Serviço são obrigatórios!")

# Mostrar lista cadastrada
st.header("Lista de Microempreendedores Cadastrados")
cursor.execute('SELECT nome, servico, telefone, instagram, endereco FROM empreendedores')
dados = cursor.fetchall()

for i, (nome, servico, telefone, instagram, endereco) in enumerate(dados, start=1):
    st.write(f"{i}. **{nome}** - {servico}")
    st.write(f"Telefone: {telefone} | Instagram: {instagram} | Endereço: {endereco}")
    st.write("---")
