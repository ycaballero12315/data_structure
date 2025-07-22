import re
from typing import TypedDict, List, Dict

EMAIL_REGEX = r'^(?!.*\.\.)[a-zA-Z0-9._-]+@[a-zA-Z0-9]+(\.[a-zA-Z0-9-]+)*\.[a-zA-Z]{2,}$'

class Email(TypedDict):
    valid_email: List[str]
    invalid_email: List[str]
    
def valid_regex(emails:List[str])->Dict[str, List[str]]:
    filter_email: Email = {'valid_email': [], 'invalid_email': []}
    for email in emails:
        (filter_email['valid_email'] if re.match(EMAIL_REGEX, email) else filter_email['invalid_email']).append(email)
    return  filter_email       
            
if __name__ == "__main__":
    emails = [
    "usuario@example.com",
    "nombre.apellido@dominio.co",
    "correo+alias@sub.dominio.com",
    "correo@dominio",  # Inválido
    "correo@dominio..com",  # Inválido
    "usuario@-dominio.com"  # Inválido
    ]
    temp_all_emails = valid_regex(emails)
    
    messages = {
    "valid_email": "Emails Válidos",
    "invalid_email": "Emails Inválidos"
    }
    for name, e_mails in temp_all_emails.items():
        for mail in e_mails:
            print(f'{messages[name]}:{mail}' )
        