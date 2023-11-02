import re

def validar_email(email):
    """Valida o formato do email."""
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

def validar_telefone(telefone):
    """Valida o formato do telefone."""
    pattern = r'^\d{2}-\d{8,9}$'
    return re.match(pattern, telefone) is not None
