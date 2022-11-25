class Hero:
    def __init__(self, power=0, fly=0, skill=0, magic=0):
        self.__power = power
        self.__fly = fly
        self.__skill = skill
        self.__magic = magic

    def setpwr(self, power):
        self.__power = power

    def getpwr(self):
        return self.__power

    def setfly(self, fly):
        self.__fly = fly

    def getfly(self):
        return self.__fly

    def setskl(self, skill):
        self.__skill = skill

    def getskl(self):
        return self.__skill

    def setmgc(self, magic):
        self.__magic = magic

    def getmgc(self):
        return self.__magic


hr = Hero()
hr.setpwr(65)
hr.setfly(75)
hr.setskl(70)
hr.setmgc(60)
print(f'Сила-{hr.getpwr()} \n'
      f'Полет-{hr.getfly()} \n'
      f'Умение-{hr.getskl()} \n'
      f'Магия-{hr.getmgc()}')