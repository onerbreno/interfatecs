# import sys
# import re

# password = input()

# characters = ['.', ',' '?', ':', ';']
# accents = ['á','é', 'í','ó', 'ú', 'â','ê', 'ô', 'ã', 'à', 'ç', 'í', 'ó']

# charUpper = 0
# charLower = 0
# lengthPassword = len(password)
# if (lengthPassword > 15 or lengthPassword < 6):
#     print('False.')
#     sys.exit()

# for char in password:
#     char.lower()
#     if char not in characters or char not in accents:
#         print('Teste chars.')
        
        
import re

def validate_password(password):
    # Verifica o comprimento da senha
    if len(password) < 6 or len(password) > 15:
        return False

    # Verifica se a senha contém pelo menos uma letra maiúscula, uma letra minúscula e um número
    if not any(char.isupper() for char in password) or not any(char.islower() for char in password) or not any(char.isdigit() for char in password):
        return False

    # Verifica se a senha contém caracteres especiais
    if not re.match("^[a-zA-Z0-9]+$", password):
        return False

    # Verifica se a senha contém sequências de valores
    for i in range(len(password) - 2):
        if ord(password[i]) + 1 == ord(password[i+1]) and ord(password[i+1]) + 1 == ord(password[i+2]):
            return False

    return True

# Exemplos de uso:
password1 = "Password123"
password2 = "abc123"
password3 = "passw0rd!"
password4 = "AB12345"
password5 = "aaaaaabc1"

print(validate_password(password1))  # True
print(validate_password(password2))  # False
print(validate_password(password3))  # False
print(validate_password(password4))  # False
print(validate_password(password5))  # False
