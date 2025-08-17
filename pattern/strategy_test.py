from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float):
        pass

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount: float):
        return f'Pago con tarjeta de Credito {amount *0.25} recibe 25% de descuento'

class PayPalPayment(PaymentStrategy):
    def pay(self, amount: float):
        return f'Pagado por paypal: {amount * 0.9} recibe 10% de descuento' 

class CashPayment(PaymentStrategy):
    def pay(self, amount: float):
        return f'Pagado en efectivo: {amount * 0.95} recibe 5% de descuento'

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
    shop.payment_strategy = CashPayment()
    print(shop.checkout(300))  # Usando el nuevo método de pago en efectivo