import pytest
from src.models import Task

def test_create_task_valid():
    task = Task("Teste Tarefa", "Descrição", "alta")
    assert task.titulo == "Teste Tarefa"
    assert task.prioridade == "alta"
    assert task.status == "pendente"

def test_update_priority():
    task = Task("Tarefa", "", "média")
    task.prioridade = "alta"
    assert task.prioridade == "alta"

def test_invalid_title():
    with pytest.raises(ValueError):  # Simula validação
        Task("", "Desc", "baixa")
    # Nota: Validação real seria adicionada no app.py