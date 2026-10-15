class fih:
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie
        self.fome = 50
        self.felicidade = 50
        self.energia = 50
    def alimentar(self):
        self.fome -= 10
        self.felicidade += 5
        self.fome = max(self.fome, 0)
        self.felicidade = min(self.felicidade, 100)
        print(f"{self.nome} comeu!")
    def dormir(self):
        self.energia += 30
        self.fome += 5
        self.energia = min(self.energia, 100) #min ou max? Por que?
        self.fome = min(self.fome, 100) #min ou max? Por que?
        print(f"{self.nome} dormiu!")
    def brincar(self):
        if self.energia <= 0:
            print(f"{self.nome} está cansado!")
            return
        self.felicidade += 10 #Ao brincar, alguma coisa vai subir
        self.energia -= 10 #Ao brincar, alguma coisa vai diminuir
        self.fome += 10 #Ao brincar, uma outra coisa vai subir, mas essa propriedade subir pode não ser bom.
        self.felicidade = min(self.felicidade, 100) #min ou max? Por que?
        self.energia = max(self.energia, 0) #min ou max? Por que?
        self.fome = min(self.fome, 100) #min ou max? Por que?
        print(f"{self.nome} brincou!")
    def verificar_estado(self):
        if self.fome >= 100:
            print("morri de fome🍕")
            return False
        if self.felicidade <= 0:
            print("Tenho Depressao😔")
            return False
        if self.energia <= 0:
            print("cansei💀")
            return False
        return True

pet = fih("carace de calçado", "carece sem calçado")

while True:


    print("=" * 30)
    print("PET VIRTUAL - PyPet!")
    print("=" * 30)

    print("1 - Alimentar")
    print("2 - Brincar")
    print("3 - Dormir")
    print("4 - Ver status")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        pet.alimentar()

    elif opcao == "2":
        pet.brincar()

    elif opcao == "3":
        pet.dormir()


    elif opcao == "4":
        print(f"nome :{pet.nome}")
        print(f"felicidade : {pet.felicidade}")
        print(f"energia : {pet.energia}")
        print(f"fome : {pet.fome}")


    elif opcao == "5":
        print ("fim")
        break


    if not pet.verificar_estado():
        print("O Pet morreu :/")
        break
