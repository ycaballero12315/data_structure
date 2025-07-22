from typing import Dict, TypedDict, List

class Registro(TypedDict):
    numeros: List[int]
    e_mails: List[str]

class Contacto(TypedDict):
    nombre: str
    registro: Registro

class Contactos:
    def __init__(self):
      self.contactos_phone: Dict[str, Contacto] = {}
    
    def add_contacto(self, nombre: str, numeros: List[int], e_mails:List[str])->None:
        if nombre in self.contactos_phone:
            raise ValueError(f"El {nombre} ya existe en el registro.")
        if not numeros or not e_mails:
            raise ValueError("Es obligatorio los campos numeros y e-mails")
        self.contactos_phone[nombre] = Contacto(
            nombre = nombre,
            registro = Registro(
                numeros = numeros,
                e_mails = e_mails
            )
        )
    
    def mostrar_ctos(self)-> List[Contacto]:
        if not self.contactos_phone:
            raise ValueError("No existe contactoas registrados")
        contactos_register: List[Contacto] = []
        for nombre, datos in self.contactos_phone.items():
            contactos_register.append(
                Contacto(
                    nombre = nombre,
                    registro = Registro(
                        numeros = datos['registro']['numeros'],
                        e_mails = datos['registro']['e_mails']
                    )
                ),
            )
        return contactos_register

def main():
    contacto = Contactos()
    while True:
        nombre = input("Nombre del contacto: ").strip().lower()
        if not nombre:
            raise ValueError("El nombre no puede estar vacio...")
        numeros = [58388827, 53023377, 59041530]
        e_mails = ["ycaballero@refcfg.cu", "ycaballero12315@gmail.com", "yoenycaballerogonzalez@gmail.com"]
        try:
           contacto.add_contacto(nombre,numeros,e_mails)
        except:
          print('An exception occurred')
        op = input("Continuara actualizando los contactos. (si/no): ").strip().lower()
        if op != "si":
            print("Saliendo del programa.")
            break
    
    for i, contacto in enumerate(contacto.mostrar_ctos(), 1):
        print(f"{i}: {contacto}")

if __name__ == "__main__":
    main()