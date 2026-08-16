class ATM:
    def __init__(self, balance=1000):
        self.balance = balance

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("El deposito debe ser mayor a cero")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("El retiro debe ser mayor a cero")

        if amount > self.balance:
            raise ValueError("Fondos insuficientes")

        self.balance -= amount
        return self.balance


if __name__ == "__main__":
    atm = ATM()

    while True:
        print("\n--- CAJERO AUTOMATICO ---")
        print("1. Consultar saldo")
        print("2. Depositar")
        print("3. Retirar")
        print("4. Salir")

        opcion = input("Selecciona una opcion: ")

        if opcion == "1":
            print(f"Saldo disponible: ${atm.check_balance()}")

        elif opcion == "2":
            cantidad = float(input("Cantidad a depositar: $"))
            try:
                atm.deposit(cantidad)
                print(f"Nuevo saldo: ${atm.check_balance()}")
            except ValueError as error:
                print(error)

        elif opcion == "3":
            cantidad = float(input("Cantidad a retirar: $"))
            try:
                atm.withdraw(cantidad)
                print(f"Nuevo saldo: ${atm.check_balance()}")
            except ValueError as error:
                print(error)

        elif opcion == "4":
            print("Gracias por utilizar el cajero.")
            break

        else:
            print("Opcion no valida.")
            