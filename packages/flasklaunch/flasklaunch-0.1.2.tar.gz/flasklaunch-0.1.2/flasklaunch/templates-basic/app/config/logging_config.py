# app/config/logging_config.py

import logging

def configure_logging(app):
    """Configura o logging com base no ambiente ativo."""
    log_level = logging.DEBUG if app.config.current_env == 'development' else logging.WARNING
    logging.basicConfig(
        level=log_level,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[logging.StreamHandler()]
    )
    logging.info(f"Logging ativado para o ambiente: {app.config.current_env}")
    logging.info(f"DEBUG está configurado como: {app.config['DEBUG']}")