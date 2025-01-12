class Animals:
    a = "horse"

class Pets(Animals):
    b = "dog"

class Dogs(Pets):
    def Bark(self):
        print("bow bow")

dikz = Dogs()
print(Dogs.a, Dogs.b, dikz.Bark())
dikz.Bark()
dikz.Bark()