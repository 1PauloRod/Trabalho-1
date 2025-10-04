# Biblioteca Online - Projeto Web com Django

**Componentes do grupo:**  
- Paulo Rodrigues
  
---

## Descrição do Projeto

Este projeto consiste em um site web desenvolvido em **Python com Django**, utilizando **HTML e CSS**, sem JavaScript. O site permite gerenciar livros e empréstimos, com controle de acesso baseado em usuários.  
O sistema implementa as **quatro operações básicas de banco de dados (CRUD)** para livros e possibilita ações específicas para usuários comuns e administradores.  

O site foi projetado para ser publicado em servidor web (PythonAnywhere) e pode opcionalmente ser containerizado usando Docker.

---

## Funcionalidades

### Para todos os usuários
- Cadastro e login no sistema.
- Recuperação de senha via e-mail.
- Visualização de livros disponíveis.
- Empréstimo de livros.
- Consulta dos empréstimos realizados e status de devolução.

### Para administradores
- Gerenciar livros (adicionar, atualizar, excluir, listar).
- Visualizar lista completa de empréstimos ativos.
- Atualizar disponibilidade de livros.

---

## Estrutura do Projeto

- **accounts/** - Gerencia usuários, login, registro e recuperação de senha.
- **livros/** - Gerencia CRUD de livros e empréstimos.
- **templates/** - Templates HTML do site.
- **static/** - Arquivos CSS.
- **db.sqlite3** - Banco de dados SQLite.
- **Dockerfile** (opcional) - Para criar container do projeto.

---

## Como usar

1. Clone o repositório:

```bash
git clone <link_do_repositorio>
cd <nome_do_projeto>

2. Crie e ative um ambiente virtual:

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

3. Instale as dependências:

pip install -r requirements.txt

4. Execute as migrações do banco de dados:

python manage.py migrate

5. Crie um superusuário (opcional, para testes de admin):

python manage.py createsuperuser

6. Execute o servidor de desenvolvimento:

python manage.py runserver

7. Acesse no navegador:

http://127.0.0.1:8000/

---

## URLs principais

- `/` - Página de boas-vindas.  
- `/home/` - Lista de livros para todos os usuários.  
- `/livros/lista_livros_admin/` - Listagem de livros para admin.  
- `/livros/adiciona_livro_admin/` - Adicionar livro (admin).  
- `/livros/atualiza_livro_admin/<pk>/` - Atualizar livro (admin).  
- `/livros/deleta_livro_admin/<pk>/` - Deletar livro (admin).  
- `/livros/<pk>/emprestar/` - Emprestar livro (usuário).  
- `/livros/<pk>/devolver/` - Devolver livro (usuário).  
- `/accounts/login/` - Login.  
- `/accounts/register/` - Registro de novo usuário.  
- `/accounts/password_reset/` - Recuperação de senha. 

---

## O que funciona

- CRUD completo de livros.  
- Empréstimo e devolução de livros com atualização automática da disponibilidade.  
- Listagem de empréstimos por usuário.  
- Login, registro e recuperação de senha.  
- Diferenciação de permissões entre usuários comuns e administradores.  

---

## O que não funciona / limitações

- O envio de e-mail de recuperação requer configuração válida do servidor SMTP (Hotmail, Gmail, etc.).  
- Gerenciador de usuários por meio do superuser/moderador

---

## Deploy no Python Anywhere

pip install --user pythonanywhere
pa_autoconfigure_django.py https://github.com/1PauloRod/Trabalho-1.git --python=3.10






