class fruta:
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade

class Loja:
    def __init__(self):
        self.frutas = []

    def addFruta(self, fruta):
        for f in self.frutas:
            if f.nome == fruta.nome:
                f.quantidade = f.quantidade + fruta.quantidade
                print(f"Quantidade de {fruta.nome} atualizada para {f.quantidade}.")
                return
        self.frutas.append(fruta);
        print(f"Fruta adicionada: {fruta.nome}")

    def listarFrutas(self):
        print("Frutas disponíveis:")
        for fruta in self.frutas:
            print(f"Nome: {fruta.nome}, Quantidade em Estoque: {fruta.quantidade}")

    def comprarFruta(self, nome_fruta, quantidade):
        for fruta in self.frutas:
            if fruta.nome == nome_fruta:
                if fruta.quantidade >= quantidade:
                    fruta.quantidade -= quantidade
                    print(f"{quantidade} {nome_fruta}(s) comprada(s) com sucesso!")
                else:
                    print("Quantidade insuficiente em estoque.")
                return
        print("Fruta não encontrada.")

    def vEstoque(self, nome_fruta):
        for fruta in self.frutas:
            if fruta.nome == nome_fruta:
                print(f"Quantidade de {nome_fruta} em estoque: {fruta.quantidade}")
                return
        print("Fruta não encontrada.")

def main():
    loja = Loja()
    
    while True:
        print("\nMenu:")
        print("1. Adicionar Fruta")
        print("2. Listar Frutas")
        print("3. Comprar Fruta")
        print("4. Verificar Estoque")
        print("5. Sair")

        a = input("Escolha uma opção: ")

        if a == "1":
            nome = input("Nome da fruta: ")
            quantidade = int(input("Quantidade em estoque: "))
            loja.addFruta(fruta(nome, quantidade))
        elif a == "2":
            loja.listarFrutas()
        elif a == "3":
            nome = input("Nome da fruta a comprar: ")
            quantidade = int(input("Quantidade a comprar: "))
            loja.comprarFruta(nome, quantidade)
        elif a == "4":
            nome = input("Nome da fruta a verificar estoque: ")
            loja.vEstoque(nome)
        elif a == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
