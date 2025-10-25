class Task:
    def __init__(self, titulo, descricao, prioridade):
        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = prioridade
        self.status = "pendente"
        self.data_criacao = "2025-10-25"  # Data atual simulada

class User:
    def __init__(self, id, email, senha):
        self.id = id
        self.email = email
        self.senha = senha