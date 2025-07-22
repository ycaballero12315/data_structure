from abc import ABC, abstractmethod

'''Patron estrategia, tambien responde al abierto cerrado en Solid, abierto \
    para el cambio, cerrado para la modificacion'''


class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float):
        pass
    

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount: float):
        return f'Pago con tarjeta de Credito {amount}'
    

class PayPalPayment(PaymentStrategy):
    def pay(self, amount: float):
        return f'Pagado por paypal: {amount}'


class ShoppingCart():
    def __init__(self, payment_strategy: PaymentStrategy):
        self.payment_strategy = payment_strategy
    
    def checkout(self, amount: float):
        return self.payment_strategy.pay(amount)
        

if __name__ == "__main__":
    shop = ShoppingCart(PayPalPayment())
    print(shop.checkout(1000)) 
    shop.payment_strategy = CreditCardPayment()
    print(shop.checkout(200))
            