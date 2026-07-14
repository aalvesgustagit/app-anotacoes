import sqlite3

# Nome do arquivo do banco de dados
DB_NAME = "notas.db"


# Função para conectar ao banco de dados e criar a tabela se não existir
def inicializar_banco():
    # Conecta ao banco de dados (cria o arquivo se não existir)
    conexao = sqlite3.connect(DB_NAME)
    cursor = conexao.cursor()

    # Cria a tabela de notas com ID autoincrementável
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS notas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            conteudo TEXT NOT NULL
        )
    """
    )

    # Salva as alterações e fecha a conexão
    conexao.commit()
    conexao.close()


# Executa a inicialização do banco assim que o arquivo é importado
inicializar_banco()


def criar_nova_nota(titulo, conteudo):
    # Conecta ao banco de dados
    conexao = sqlite3.connect(DB_NAME)
    cursor = conexao.cursor()

    # Insere uma nova nota
    cursor.execute("INSERT INTO notas (titulo, conteudo) VALUES (?, ?)", (titulo, conteudo))

    # Salva as alterações e fecha a conexão
    conexao.commit()
    conexao.close()
    print("Nota criada com sucesso!")


def listar_todas_as_notas():
    conexao = sqlite3.connect(DB_NAME)
    cursor = conexao.cursor()

    # Seleciona todas as notas
    cursor.execute("SELECT id, titulo, conteudo FROM notas")
    linhas = cursor.fetchall()

    # Fecha a conexão
    conexao.close()

    # Converte o resultado para uma lista de dicionários
    notas = []
    for linha in linhas:
        notas.append({"id": linha[0], "titulo": linha[1], "conteudo": linha[2]})
    return notas


def buscar_nota_por_id(id_nota):
    conexao = sqlite3.connect(DB_NAME)
    cursor = conexao.cursor()

    # Busca uma nota específica pelo ID
    cursor.execute("SELECT id, titulo, conteudo FROM notas WHERE id = ?", (id_nota,))
    linha = cursor.fetchone()

    conexao.close()

    # Retorna a nota como dicionário se encontrada, ou None
    if linha:
        return {"id": linha[0], "titulo": linha[1], "conteudo": linha[2]}
    return None


def atualizar_nota(id_nota, novo_titulo, novo_conteudo):
    conexao = sqlite3.connect(DB_NAME)
    cursor = conexao.cursor()

    # Atualiza o título e o conteúdo da nota pelo ID
    cursor.execute(
        "UPDATE notas SET titulo = ?, conteudo = ? WHERE id = ?",
        (novo_titulo, novo_conteudo, id_nota),
    )

    conexao.commit()
    conexao.close()
    print("Nota atualizada!")
    return True


def deletar_nota(id_nota):
    conexao = sqlite3.connect(DB_NAME)
    cursor = conexao.cursor()

    # Remove uma nota pelo ID
    cursor.execute("DELETE FROM notas WHERE id = ?", (id_nota,))

    conexao.commit()
    conexao.close()
    print("Nota deletada!")
    return True