


from maestroPizzero import MaestroPizzero
from mozo import Mozo

class TesterPizzeria:
    def main(self):
        mozo1 = Mozo("Alfredo")
        mozo2 = Mozo("Alfredo")
        print(id(mozo1))
        print(id(mozo2))

if __name__ == '__main__':
  testerPizzeria = TesterPizzeria()
  testerPizzeria.main()