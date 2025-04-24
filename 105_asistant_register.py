from typing import TypedDict, List
from collections import Counter

class Asistente(TypedDict):
    name: str
    state_assistant: bool
    
class Event_asistant:
    def __init__(self):
        self.guests: List[Asistente] = []
    
    def add_guess(self, nombre:str, asisten: bool)->None:
        asistant = Asistente(name = nombre, state_assistant = asisten)
        self.guests.append(asistant)
    
    def count_asisstant(self)->str:
        counts = Counter(guest['state_assistant'] for guest in self.guests)
        return f'Asistieron {counts[True]} -No Asistieron {counts[False]}'
    
    def show_guess(self) -> str:
        invitados = []
        for guest in self.guests:
            status = 'Asistio' if guest['state_assistant'] else 'No Aistio'
            invitados.append(f"{guest['name']}:{status}")
        return "\n".join(invitados)

if __name__ == "__main__":
    asistent = Event_asistant()
    asistent.add_guess("Yoeny", True)
    asistent.add_guess("Dunia", False)
    print(asistent.count_asisstant())
    print(asistent.show_guess())
    
    