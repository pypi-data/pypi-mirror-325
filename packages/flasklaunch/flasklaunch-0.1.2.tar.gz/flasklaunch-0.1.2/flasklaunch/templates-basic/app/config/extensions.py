# app/config/extensions.py

import logging
from importlib import import_module

def load_extensions(app):
    """Carrega as extensões configuradas no settings.yaml."""
    logging.debug("Carregando extensões...")
    for extension in app.config.get("EXTENSIONS", []):
        try:
            module_name, factory = extension.split(":")
            ext = import_module(module_name)
            getattr(ext, factory)(app)
            logging.debug(f"{extension} carregada com sucesso.")
        except Exception as e:
            logging.error(f"Erro ao carregar {extension}: {e}")