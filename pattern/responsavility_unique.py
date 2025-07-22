class ManagerUser:
    def __init__(self):
        self.users = []
        
    def add_user(self, user: dict):
        self.users.append(user)
    
    def get_user(self):
        if not self.users:
            return -1
        return self.users
    
    
class SaveUser:
    def save(self, users: list[dict], filename: str):
        try:
            with open(filename, 'w') as f:
                for user in users:
                    f.write(str(user) + '\n')
        except FileNotFoundError:
            print('No se encuentra el fichero')


if __name__ == "__main__":
    muser = ManagerUser()
    muser.add_user({'user_id': 1, 'name': "Yoeny"})
    saveuser = SaveUser()
    saveuser.save(muser.get_user(), 'test.txt')