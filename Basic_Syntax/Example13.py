class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        print("Class Create")

    def move(self, way):
        print(f"{self.name}이 {way}로 이동")

class Unit2:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        print("Class Create")

    def move(self, way):
        print(f"{self.name}이 {way}로 이동")

class EvolUnit(Unit, Unit2):
    def __init__(self, name, hp, attr):
        Unit.__init__(self, name, hp)
        Unit2.__init__(self, name, hp)
        # super().__init__(name, hp)
        self.attr = attr

    def info(self):
        print("{0} 이다.".format(self.name))



u1 = Unit("person", 40)
u2 = Unit("fish", 20)

print(u1.name)
u1.move("forward")

print("========================")

eu1 = EvolUnit("digdak", 123, "fire")
eu1.info()
