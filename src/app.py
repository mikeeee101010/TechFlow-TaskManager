# Autenticação simples para usuários

from flask import Flask, request, jsonify, render_template_string
import smtplib
from email.mime.text import MIMEText
from models import Task, User  # Importa modelos

app = Flask(__name__)

# Simulação de banco de dados em memória
tasks_db = []
users_db = [{"id": 1, "email": "admin@example.com", "senha": "123"}]  # Usuário de teste

# HTML simples para interface
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head><title>Task Manager</title></head>
<body>
    <h1>Gerenciador de Tarefas</h1>
    <form method="POST" action="/login">
        Email: <input type="text" name="email"><br>
        Senha: <input type="password" name="senha"><br>
        <input type="submit" value="Login">
    </form>
    {% if tasks %}
    <h2>Tarefas:</h2>
    <ul>{% for task in tasks %}<li>{{ task.titulo }} - {{ task.prioridade }} ({{ task.status }})</li>{% endfor %}</ul>
    {% endif %}
    <form method="POST" action="/tasks">
        Título: <input type="text" name="titulo" required><br>
        Descrição: <input type="text" name="descricao"><br>
        Prioridade: <select name="prioridade"><option>alta</option><option>média</option><option>baixa</option></select><br>
        <input type="submit" value="Criar Tarefa">
    </form>
</body>
</html>
"""

@app.route('/', methods=['GET'])
def index():
    return render_template_string(HTML_TEMPLATE, tasks=tasks_db)

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    senha = request.form['senha']
    user = next((u for u in users_db if u['email'] == email and u['senha'] == senha), None)
    if user:
        return jsonify({"message": "Login bem-sucedido"}), 200
    return jsonify({"error": "Credenciais inválidas"}), 401

@app.route('/tasks', methods=['POST'])
def create_task():
    # Criação de tarefas com validação
    titulo = request.form['titulo']
    descricao = request.form.get('descricao', '')
    prioridade = request.form['prioridade']
    new_task = Task(titulo, descricao, prioridade)
    tasks_db.append(new_task)
    send_email_notification(new_task, "criada")  # Notificação (mudança de escopo)
    return jsonify({"message": "Tarefa criada"}), 201

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    if 0 <= task_id < len(tasks_db):
        tasks_db[task_id].prioridade = request.json.get('prioridade', tasks_db[task_id].prioridade)
        tasks_db[task_id].status = request.json.get('status', tasks_db[task_id].status)
        send_email_notification(tasks_db[task_id], "atualizada")
        return jsonify({"message": "Tarefa atualizada"}), 200
    return jsonify({"error": "Tarefa não encontrada"}), 404

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    if 0 <= task_id < len(tasks_db):
        del tasks_db[task_id]
        return jsonify({"message": "Tarefa excluída"}), 200
    return jsonify({"error": "Tarefa não encontrada"}), 404

@app.route('/tasks', methods=['GET'])
def list_tasks():
    return jsonify([{"id": i, "titulo": t.titulo, "prioridade": t.prioridade, "status": t.status} for i, t in enumerate(tasks_db)])

def send_email_notification(task, action):
    # Simulação de e-mail (configure SMTP real para produção)
    msg = MIMEText(f"Tarefa {action}: {task.titulo} (Prioridade: {task.prioridade})")
    msg['Subject'] = 'Notificação de Tarefa'
    msg['From'] = 'no-reply@techflow.com'
    msg['To'] = 'admin@example.com'
    # smtplib.SMTP('smtp.gmail.com', 587).send_message(msg)  # Descomente para real
    print(f"E-mail simulado enviado para tarefa: {task.titulo}")  # Para demo

if __name__ == '__main__':
    app.run(debug=True)