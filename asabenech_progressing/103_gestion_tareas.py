from typing import Set, List, Dict, TypedDict

class User(TypedDict):
    user: str
    tasks: Set[str]

class Admin_tasks:
    def __init__(self):
        self.users: List[User] = []
        
    def add_user(self, name: str, tasks: List[str])->None:
        collections_task = set(tasks)
        
        user = User(user=name, tasks = collections_task)
        
        self.users.append(user)
        
    def show_users(self)-> str:
        msj = []
        for user in self.users:
            msj.append(f"User: {user['user']} -Trasks: {', '.join(user["tasks"])}")
        return f','.join(msj)

if __name__ == "__main__":
    tasks = ['comprar_pan', 'ir al banco', 'andar por la zona'] 
    admin_task = Admin_tasks()
    
    admin_task.add_user('Yoeny', tasks)
    print(admin_task.show_users())
    