import unittest
from atm import ATM


class TestATM(unittest.TestCase):

    def setUp(self):
        self.atm = ATM()

    def test_saldo_inicial(self):
        self.assertEqual(self.atm.check_balance(), 1000)

    def test_deposito(self):
        self.atm.deposit(500)
        self.assertEqual(self.atm.check_balance(), 1500)

    def test_retiro(self):
        self.atm.withdraw(200)
        self.assertEqual(self.atm.check_balance(), 800)

    def test_fondos_insuficientes(self):
        with self.assertRaises(ValueError):
            self.atm.withdraw(2000)

    def test_deposito_negativo(self):
        with self.assertRaises(ValueError):
            self.atm.deposit(-100)

    def test_retiro_negativo(self):
        with self.assertRaises(ValueError):
            self.atm.withdraw(-100)


if __name__ == "__main__":
    unittest.main()