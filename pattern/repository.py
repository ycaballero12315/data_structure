from abc import ABC, abstractmethod
'''La logica separada de la capa de acceso a datos Repositorio'''


class UserPepository(ABC):
    @abstractmethod
    def get_user(self, user_id: int):
        pass
    
    @abstractmethod
    def add_user(self, user: dict):
        pass
    

class InMemoryUserRepository(UserPepository):
    def __init__(self):
        super().__init__()
        self.users = {}
    
    def get_user(self, user_id: int):
        return self.users.get(user_id)
    
    def add_user(self, user: dict):
        self.users[user['user_id']] = user
     
        
repo = InMemoryUserRepository()
repo.add_user({'user_id': 1, 'name': "Yoeny"})
print(repo.get_user(1))
        