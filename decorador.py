def decorator(f):
    def envoltura():
        print('First msg...')
        f()
        print('Secund sms...')
    return envoltura

@decorator
def print_hello():
    print('saludos...')

print_hello()
        