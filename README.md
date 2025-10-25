# TechFlow Task Manager

Sistema web básico de gerenciamento de tarefas para uma startup de logística, desenvolvido com Flask (Python) pela TechFlow Solutions. Permite CRUD de tarefas, autenticação de usuários, priorização e notificações por e-mail.

## Objetivo
Acompanhar o fluxo de trabalho em tempo real, priorizar tarefas críticas e monitorar o desempenho da equipe, seguindo metodologias ágeis (Kanban).

## Escopo Inicial
- CRUD para tarefas (título, descrição, prioridade: alta/média/baixa, status).
- Autenticação de usuários (login simples).
- Interface web básica.

## Metodologia
Kanban via GitHub Projects: Colunas "To Do", "In Progress", "Done". Iterações semanais para priorização.

## Como Executar
1. Clone o repositório: `git clone https://github.com/SEU_USUARIO/TechFlow-TaskManager`
2. Instale dependências: `pip install -r requirements.txt`
3. Execute o app: `python src/app.py`
4. Acesse: http://127.0.0.1:5000
5. Para testes: `pytest tests/`

## Mudança de Escopo
Adicionada funcionalidade de **notificação por e-mail** ao criar/atualizar tarefas (justificativa: melhorar comunicação em equipes remotas). Implementada com `smtplib` (configurar SMTP real para produção; simulado aqui). Novo card no Kanban: "Implementar notificações por e-mail".

## Estrutura
- `/src`: Código-fonte (app.py, models.py).
- `/tests`: Testes unitários (test_tasks.py).
- `/docs`: Diagramas UML (use PlantUML para renderizar).

## Histórico de Commits
- Pelo menos 12 commits com mensagens semânticas.

## Kanban
Acesse a aba "Projects" para ver o quadro com 12 cards.

Exemplo de uso: Crie uma tarefa, priorize como "alta" e receba notificação.