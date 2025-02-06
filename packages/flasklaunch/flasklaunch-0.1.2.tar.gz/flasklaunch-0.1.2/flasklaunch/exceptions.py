class FlaskLaunchError(Exception):
    """Exceção base para erros do FlaskLaunch."""
    pass

class TemplateNotFoundError(FlaskLaunchError):
    """Exceção para quando o diretório de templates não é encontrado."""
    pass