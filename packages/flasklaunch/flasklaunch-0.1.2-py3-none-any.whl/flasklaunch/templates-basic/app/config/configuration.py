# app/config/configuration.py

from dynaconf import FlaskDynaconf
from app.config.extensions import load_extensions

def init_app(app):
    FlaskDynaconf(app, settings_files=["settings.yaml"], envvar_prefix="DYNACONF")
    
    # Configuração do DEBUG
    app.config["DEBUG"] = app.config.get("DEBUG", False)

    load_extensions(app)
