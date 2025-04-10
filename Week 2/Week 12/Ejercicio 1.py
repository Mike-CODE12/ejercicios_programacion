# 1. Cree una clase de `BankAccount` que:
#     1. Tenga un atributo de `balance`.
#     2. Tenga un método para ingresar dinero.
#     3. Tengo un método para retirar dinero.
    
# Cree otra clase que herede de esta llamada `SavingsAccount` que:
# 1. Tenga un atributo de `min_balance` que se pueda asignar al crearla.
# 2. Arroje un error si al intentar retirar dinero, el retiro haría que el `balance` quede debajo del `min_balance`. 
# Es decir que sí se pueden hacer retiros **siempre y cuando** el `balance` quede arriba del `min_balance`.

class BankAccount:


    def __init__(self, balance):
        self.balance=balance


    def deposit_money(self, deposit):
        self.balance=self.balance+deposit
        return self.balance
    

    def withdraw_money(self, withdrawal):
        self.balance=self.balance-withdrawal
        return self.balance
    

first_account=BankAccount(50000)
first_account.deposit_money(7850)
first_account.withdraw_money(7851)
print(first_account.balance)

class SavingsAccount(BankAccount):


    def __init__(self, balance, min_balance, withdrawal):
        super().__init__(balance)   
        self.min_balance= min_balance
        try:
            if self.balance-withdrawal<self.min_balance:        
                raise ValueError("The account's current balance is below the minimum required") 
        except ValueError as ex:
            print(f"{ex}: Due to this, we cannot to process the requested withdrawal")
        else:
            super().withdraw_money(withdrawal) 

second_account=SavingsAccount(50000, 2000, 47000)
print(second_account.balance)