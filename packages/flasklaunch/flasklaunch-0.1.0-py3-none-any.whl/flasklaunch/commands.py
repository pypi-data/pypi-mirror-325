# flasklaunch/flasklaunch/commands.py

import os
import shutil
import subprocess
import click
import yaml
from flasklaunch.version import get_version

# Função para criar a estrutura de pastas e arquivos
def create_structure(base_path):
    """Cria a estrutura de pastas e arquivos vazios no diretório do usuário."""
    structure = [
        ".env",
        "README.md",
        "run.py",
        "settings.yaml",
        "app/api/resources.py",
        "app/api/__init__.py",
        "app/config/configuration.py",
        "app/config/__init__.py",
        "app/extensions/database.py",
        "app/extensions/visuals.py",
        "app/extensions/__init__.py",
        "app/models/Example.py",
        "app/tests/",
        "app/web/views.py",
        "app/web/__init__.py",
        "app/web/templates/example.html",
        "app/web/templates/index.html",
    ]

    try:
        for item in structure:
            path = os.path.join(base_path, item)
            if item.endswith("/"):  # É uma pasta
                os.makedirs(path, exist_ok=True)
            else:  # É um arquivo
                os.makedirs(os.path.dirname(path), exist_ok=True)
                with open(path, "w") as f:
                    pass  # Cria o arquivo vazio
    except Exception as e:
        click.secho(f"Erro ao criar a estrutura de pastas e arquivos: {e}", fg="red", bold=True)
        raise


# Função para copiar o conteúdo dos templates
def copy_template(src, dst):
    """Copia o conteúdo dos templates para a estrutura criada."""
    try:
        for item in os.listdir(src):
            src_path = os.path.join(src, item)
            dst_path = os.path.join(dst, item)

            if os.path.isdir(src_path):
                shutil.copytree(src_path, dst_path, dirs_exist_ok=True)
            else:
                shutil.copy2(src_path, dst_path)
    except Exception as e:
        click.secho(f"Erro ao copiar os templates: {e}", fg="red", bold=True)
        raise


# Função para atualizar o arquivo settings.yaml
def update_extension_in_yaml(extension):
    """Atualiza o arquivo settings.yaml para incluir novas extensões."""
    try:
        settings_file = "settings.yaml"
        if os.path.exists(settings_file):
            with open(settings_file, "r", encoding="utf-8") as f:
                settings = yaml.safe_load(f) or {}
        else:
            settings = {}

        settings.setdefault("default", {}).setdefault("EXTENSIONS", [])
        if extension not in settings["default"]["EXTENSIONS"]:
            settings["default"]["EXTENSIONS"].append(extension)

        with open(settings_file, "w", encoding="utf-8") as f:
            yaml.dump(settings, f, default_flow_style=False, allow_unicode=True)
    except Exception as e:
        click.secho(f"Erro ao atualizar o settings.yaml: {e}", fg="red", bold=True)
        raise

# Função para atualizar o requirements.txt
def update_requirements(package):
    """Adiciona pacotes ao requirements.txt e instala a dependência."""
    try:
        with open("requirements.txt", "a", encoding="utf-8") as f:
            f.write(f"{package}\n")
        subprocess.run(["pip", "install", package], check=True)
        click.secho(f"{package} instalado e adicionado ao requirements.txt.", fg="green", bold=True)
    except Exception as e:
        click.secho(f"Erro ao atualizar requirements.txt: {e}", fg="red", bold=True)
        raise
        
# Comando para inicializar o projeto
@click.command(name="init-project")
@click.option('--overwrite', is_flag=True, help="Sobrescrever arquivos existentes")
def init_project(overwrite):
    """Inicializa a estrutura base do projeto Flask."""
    base_path = os.getcwd()
    template_path = os.path.join(os.path.dirname(__file__), "templates")

    if not os.path.exists(template_path):
        click.secho("Erro: Diretório de templates não encontrado. 🚨", fg="red", bold=True)
        click.secho("Solução: Verifique se o pacote foi instalado corretamente ou se o diretório flasklaunch/templates existe.", fg="yellow")
        return

    # Limpa a estrutura existente se a flag --overwrite for usada
    if overwrite:
        click.secho("🔄 Limpando estrutura existente...", fg="yellow")
        try:
            for item in os.listdir(base_path):
                item_path = os.path.join(base_path, item)
                if os.path.isdir(item_path):
                    shutil.rmtree(item_path)
                else:
                    os.remove(item_path)
            click.secho("✅ Estrutura existente limpa com sucesso.", fg="green")
        except Exception as e:
            click.secho(f"Erro ao limpar a estrutura existente: {e}", fg="red", bold=True)
            return

    # Cria a estrutura de pastas e arquivos com barra de progresso
    click.secho("🔧 Criando estrutura de arquivos...", fg="cyan")
    with click.progressbar(range(100), label="Criando arquivos...") as bar:
        for i in bar:
            create_structure(base_path)

    # Copia o conteúdo dos templates
    click.secho("📂 Copiando templates...", fg="cyan")
    copy_template(template_path, base_path)

    # Gera o requirements.txt com as dependências instaladas
    subprocess.run(["pip", "freeze"], stdout=open("requirements.txt", "w"), check=True)
    click.secho("✅ Projeto Flask inicializado com sucesso! 🎉", fg="green", bold=True)


# Comando para adicionar suporte a API
@click.command()
def add_api():
    """Adiciona suporte a API RESTful (flask-restful)."""
    base_path = os.getcwd()
    template_path = os.path.join(os.path.dirname(__file__), "templates/app/api")

    try:
        # Cria a estrutura de API
        os.makedirs(os.path.join(base_path, "app", "api"), exist_ok=True)
        copy_template(template_path, os.path.join(base_path, "app", "api"))

        # Atualiza o settings.yaml e requirements.txt
        update_extension_in_yaml("app.api:init_app")
        update_requirements("flask-restful")

        click.secho("✅ API adicionada com sucesso! 🚀", fg="green", bold=True)
    except Exception as e:
        click.secho(f"Erro ao adicionar API: {e}", fg="red", bold=True)


# Comando para adicionar suporte a banco de dados
@click.command()
def add_db():
    """Adiciona suporte a banco de dados (flask-sqlalchemy)."""
    base_path = os.getcwd()
    template_path = os.path.join(os.path.dirname(__file__), "templates/app/extensions")

    try:
        # Cria a estrutura de banco de dados
        os.makedirs(os.path.join(base_path, "extensions"), exist_ok=True)
        os.makedirs(os.path.join(base_path, "models"), exist_ok=True)
        copy_template(template_path, os.path.join(base_path, "extensions"))

        # Atualiza o settings.yaml e requirements.txt
        update_extension_in_yaml("app.extensions.database:init_app")
        update_requirements("flask-sqlalchemy")

        click.secho("✅ Banco de dados adicionado com sucesso! 💾", fg="green", bold=True)
    except Exception as e:
        click.secho(f"Erro ao adicionar banco de dados: {e}", fg="red", bold=True)


# Comando para adicionar suporte a web
@click.command()
def add_web():
    """Adiciona suporte a templates e views (flask-bootstrap)."""
    base_path = os.getcwd()
    template_path = os.path.join(os.path.dirname(__file__), "templates/app/web")

    try:
        # Cria a estrutura de web
        os.makedirs(os.path.join(base_path, "web/templates"), exist_ok=True)
        copy_template(template_path, os.path.join(base_path, "web"))

        # Atualiza o settings.yaml e requirements.txt
        update_extension_in_yaml("app.web:init_app")
        update_requirements("flask-bootstrap")

        click.secho("✅ Web adicionada com sucesso! 🌐", fg="green", bold=True)
    except Exception as e:
        click.secho(f"Erro ao adicionar Web: {e}", fg="red", bold=True)


# Comando para gerar o requirements.txt
@click.command()
def generate_requirements():
    """Gera o requirements.txt com as dependências instaladas."""
    try:
        subprocess.run(["pip", "freeze"], stdout=open("requirements.txt", "w"), check=True)
        click.secho("✅ requirements.txt gerado com sucesso!", fg="green", bold=True)
    except Exception as e:
        click.secho(f"Erro ao gerar requirements.txt: {e}", fg="red", bold=True)


# Comando para executar a aplicação Flask
@click.command()
def run_app():
    """Executa a aplicação Flask."""
    try:
        os.system("flask run")
    except Exception as e:
        click.secho(f"Erro ao executar a aplicação Flask: {e}", fg="red", bold=True)


def get_database_uri(config):
    """Gera a string de conexão do banco de dados dinamicamente."""
    engine = config.get("ENGINE").lower()  # No default, raise error if missing
    name = config.get("NAME")  # No default, raise error if missing
    user = config.get("USER")
    password = config.get("PASSWORD")
    host = config.get("HOST")
    port = config.get("PORT")

    if engine == "sqlite":
        return f"sqlite:///{name}"

    elif engine == "mysql":
        if not all([user, password, host, port]):
            raise ValueError("Para MySQL, USER, PASSWORD, HOST e PORT são obrigatórios.")
        return f"mysql://{user}:{password}@{host}:{port}/{name}"

    elif engine == "postgres":
        if not all([user, password, host, port]):
            raise ValueError("Para Postgres, USER, PASSWORD, HOST e PORT são obrigatórios.")
        return f"postgresql://{user}:{password}@{host}:{port}/{name}"

    else:
        raise ValueError(f"Banco de dados '{engine}' não suportado.")

# Função para atualizar o settings.yaml
def update_settings_yaml(db_config):
    try:
        settings_file = "settings.yaml"
        with open(settings_file, "r", encoding="utf-8") as f:
            settings = yaml.safe_load(f) or {}

        settings["default"]["DATABASE"] = db_config  # Directly update the DATABASE section

        with open(settings_file, "w", encoding="utf-8") as f:
            yaml.dump(settings, f, default_flow_style=False, allow_unicode=True)

        click.secho("✅ settings.yaml atualizado com as novas configurações de banco de dados.", fg="green", bold=True)
    except Exception as e:
        click.secho(f"Erro ao atualizar settings.yaml: {e}", fg="red", bold=True)

# Comando para criar o banco de dados
@click.command()
@click.option('--engine', type=str, required=True, help="Tipo de banco de dados (ex: mysql, postgres, sqlite).")
@click.option('--name', type=str, required=True, help="Nome do banco de dados.")
@click.option('--user', type=str, help="Usuário do banco de dados (obrigatório para MySQL e Postgres).")
@click.option('--password', type=str, help="Senha do banco de dados (obrigatório para MySQL e Postgres).")
@click.option('--host', type=str, default="localhost", help="Host do banco de dados.")
@click.option('--port', type=int, help="Porta do banco de dados (obrigatório para MySQL e Postgres).")
def create_db(engine, name, user, password, host, port):
    """Cria o banco de dados usando Flask-Migrate e configurações dinâmicas."""

    db_config = {  # Start with a dictionary
        "ENGINE": engine,
        "NAME": name,
    }

    if engine in ("mysql", "postgres"):
        db_config["USER"] = user
        db_config["PASSWORD"] = password
        db_config["HOST"] = host
        db_config["PORT"] = port

    try:
        db_uri = get_database_uri(db_config)  # Get the URI *before* updating settings.yaml
        update_settings_yaml(db_config)  # Update settings.yaml with the config
        click.echo(f"Database URI: {db_uri}") # Print the URI for verification

        # Set the environment variable for Flask-Migrate (important!)
        os.environ["SQLALCHEMY_DATABASE_URI"] = db_uri

        # Now run migrations
        os.system("flask db upgrade")
        click.secho("✅ Migrações aplicadas com sucesso!", fg="green", bold=True)

    except ValueError as e:
        click.secho(f"Erro: {e}", fg="red", bold=True)
    except Exception as e:
        click.secho(f"Erro ao criar/migrar banco de dados: {e}", fg="red", bold=True)

# Comando para remover o banco de dados
@click.command()
def drop_db():
    """Remove todas as migrações do banco de dados."""
    try:
        os.system("flask db downgrade")
    except Exception as e:
        click.secho(f"Erro ao remover banco de dados: {e}", fg="red", bold=True)


# Comando para exibir a versão do flasklaunch
@click.command()
def version():
    """Exibe a versão do flasklaunch."""
    click.secho(f"flasklaunch version {get_version()}", fg="blue", bold=True)