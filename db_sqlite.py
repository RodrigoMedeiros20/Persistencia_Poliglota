import sqlite3

conn = sqlite3.connect('jantares.db', check_same_thread=False)
c = conn.cursor()

# --- Funções para Cozinhas ---
def criar_tabela_cozinhas():
    c.execute('''
        CREATE TABLE IF NOT EXISTS cozinhas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL UNIQUE
        )
    ''')
    conn.commit()

def adicionar_cozinha(nome):
    try:
        c.execute("INSERT INTO cozinhas (nome) VALUES (?)", (nome,))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False

def get_todas_cozinhas():
    c.execute("SELECT id, nome FROM cozinhas ORDER BY nome")
    return c.fetchall()

def get_cozinha_por_id(cozinha_id):
    c.execute("SELECT nome FROM cozinhas WHERE id = ?", (cozinha_id,))
    resultado = c.fetchone()
    return resultado[0] if resultado else "Não definida"

# --- Funções para Bairros ---
def criar_tabela_bairros():
    c.execute('''
        CREATE TABLE IF NOT EXISTS bairros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL UNIQUE
        )
    ''')
    conn.commit()

def adicionar_bairro(nome):
    try:
        c.execute("INSERT INTO bairros (nome) VALUES (?)", (nome,))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False

def get_todos_bairros():
    c.execute("SELECT id, nome FROM bairros ORDER BY nome")
    return c.fetchall()

def get_bairro_por_id(bairro_id):
    c.execute("SELECT nome FROM bairros WHERE id = ?", (bairro_id,))
    resultado = c.fetchone()
    return resultado[0] if resultado else "Não definido"

# --- Inicialização do Banco de Dados ---
criar_tabela_cozinhas()
criar_tabela_bairros()

# Adiciona dados iniciais se as tabelas estiverem vazias
if not get_todas_cozinhas():
    adicionar_cozinha("Brasileira")
    adicionar_cozinha("Italiana")
    adicionar_cozinha("Japonesa")

if not get_todos_bairros():
    adicionar_bairro("Manaíra")
    adicionar_bairro("Tambaú")
    adicionar_bairro("Bessa")
    adicionar_bairro("Cabedelo")