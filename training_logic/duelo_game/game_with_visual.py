from typing import List

class Caracter:
    def __init__(self, identificador: int, 
                 nivel_eneg: float):
        self.id = identificador
        self.n_energia = nivel_eneg
        self.numero_vida: int = 0
        self.capacidad_ofenciva: int = 0
    
    def __str__(self):
        return f'Caracter: ID->{self.id} |'\
            f'N_energia: {self.n_energia} | #Vidas: {self.numero_vida}'\
            f'Ofenciva: {self.capacidad_ofenciva}'
    
    def __repr__(self):
        return f'{self.__class__.__name__}'    
        
    def set_numero_vida(self, numero_vida):
        if 5 >= numero_vida >= 0:
            self.numero_vida = numero_vida
    
    def set_capacidad_ofenciva(self, capacidad):
        if 10 <= capacidad <= 20:
            self.capacidad_ofenciva = capacidad
    
    def get_numero_vida(self):
        return self.numero_vida
    
    def get_capacidad_ofenciva(self):
        return self.capacidad_ofenciva
    
class Personaje(Caracter):
    def __init__(self, magia: int, 
                 identificador: int,
                 nivel_eneg: float):
        super().__init__(identificador, nivel_eneg)
        self.cant_magia = magia
        self.factor_potencia = 1
    
    def __str__(self):
        return f'ID: {self.identificador} | ' \
            f'Magia: {self.cant_magia} | Factor Potencia: {self.factor_potencia}'
    
    def __repr__(self):
        return f'{self.__class__.__name__}' 
    
    def set_factor_potencia(self, potencia):
        if 1<= potencia <=2:
            self.factor_potencia = potencia
    
    def get_factor_potencia(self):
        return self.factor_potencia
    
    
class Enemigo(Caracter):
    def __init__(self, maldad, identificador, nivel_eneg):
        super().__init__(identificador, nivel_eneg)
        self.nivel_maldad = maldad
    
    def __str__(self):
        return f'ID: {self.id} | '\
            f'Nivel de maldad: {self.nivel_maldad}'
    
    def __repr__(self):
        return f'{self.__class__.__name__}(ID = {self.id})'     
        
class Duelos:
    def __init__(self):
        self.caracteres: List[Caracter] = []
        
    def add_caracter(self, caracter: Caracter):
        
        if any(c.id == caracter for c in self.caracteres):
            raise ValueError('Este caracter fue introducido!')
        
        self.caracteres.append(caracter)
    
    def search_caracter(self, caracter: Caracter) -> str:
        
        low, higt = 0, len(self.caracteres) -1
        self.caracteres.sort(key=lambda c : c.id)
        
        while low <= higt:
            mid = (low + higt)//2
      
            if self.caracteres[mid].id == caracter.id:
                return f'El {caracter.id} se encuentra en {mid + 1}'
            elif self.caracteres[mid].id<caracter.id:
                low = mid + 1
            else:
                higt = mid - 1
          
        return f'No se encuentra en la lista el elemento {caracter}'
    
    def calc_capacidad_de_danno(self, caracter) -> int:
        if isinstance(caracter, Personaje):
            return max(caracter.n_energia,caracter.cant_magia)* caracter.capacidad_ofenciva
        elif isinstance(caracter, Enemigo):
            return (caracter.n_energia + caracter.capacidad_ofenciva)*caracter.nivel_maldad
        else:
            raise ValueError('Tipo de caracter no valido!')
    
    def realizar_duelo(self, c1, c2)-> str:
        if c1.get_numero_vida() == 0 or c2.get_numero_vida() == 0:
            raise ValueError("Uno de los jugadores estqa muerto!")
        
        danno1 = self.calc_capacidad_de_danno(c1)
        danno2 = self.calc_capacidad_de_danno(c2)
        
        if danno1>danno2:
            ganador, perdedor = c1, c2
        elif danno1<danno2:
            ganador, perdedor = c2, c1
        else:
            return 'Empate'
        ganador.n_energia += perdedor.n_energia/2
        perdedor.numero_vida -= 1 
        
        return f'El ganador es {ganador.id}'    
    
    def maldadvspotencia(self):
        filter_caracteres = [c for c in self.caracteres if c.numero_vida > 0]
                
        suma_maldad_enemigos = sum(c.nivel_maldad for c in filter_caracteres if isinstance(c, Enemigo))
        suma_potencia_personajes = sum(p.factor_potencia for p in filter_caracteres if isinstance(p, Personaje))
        
        return suma_maldad_enemigos > suma_potencia_personajes

        
                    
         
    