class Cliente:
    def __init__(self, id: int, nome: str, cpf: int, idade: int) -> None:
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.idade = idade


class Quarto:
    def __init__(self, id: int, nome: str, valor: float) -> None:
        self.id = id
        self.nome = nome
        self.valor = valor
        self.disponibilidade = True


class Reserva:
    def __init__(self, id: int, data_entrada: str, quarto: Quarto, cliente: Cliente, data_saida: str) -> None:
        self.id = id
        self.data_entrada = data_entrada
        self.quarto = quarto
        self.cliente = cliente
        self.data_saida = data_saida
        self.status = False


class Gerenciador_de_reservas:
    def __init__(self) -> None:
        self.lista_de_reservas = []
        self.lista_de_quartos = []
        self.lista_de_clientes = []

    def adicionar_quarto(self, quarto: Quarto):
        self.lista_de_quartos.append(quarto)

    def quartos_disponiveis(self):
        print("Quartos disponíveis:")
        for quarto in self.lista_de_quartos:
            if quarto.disponibilidade:
                print(f"Quarto {quarto.id} - {quarto.nome}: R$ {quarto.valor:.2f} disponíveis!")

    def quartos_reservados(self):
        print("Quartos reservados:")
        for reserva in self.lista_de_reservas:
            print(f"Quarto {reserva.quarto.id} - {reserva.quarto.nome} reservado para {reserva.cliente.nome}")

    def fazer_reserva(self, reserva: Reserva):
        for quarto in self.lista_de_quartos:
            if quarto.id == reserva.quarto.id and quarto.disponibilidade:
                quarto.disponibilidade = False
                self.lista_de_reservas.append(reserva)
                print(f"O quarto {reserva.quarto.id} foi reservado para o cliente {reserva.cliente.nome}.")
                return
        
        print("Nenhum quarto disponível!")


gerenciador = Gerenciador_de_reservas()
quarto1 = Quarto(1, "Quarto 1", 1000)
quarto2 = Quarto(2, "Quarto 2", 2000)
gerenciador.adicionar_quarto(quarto1)
gerenciador.adicionar_quarto(quarto2)

while True:
    menu = input("""
1 - Ver quartos disponíveis
2 - Ver quartos reservados
3 - Fazer reserva
0 - Sair
    """)
    match menu:
        case "1":
            gerenciador.quartos_disponiveis()
        case "2":
            gerenciador.quartos_reservados()
        case "3":
            nome_cliente = input("Nome do cliente: ")
            cliente = Cliente(1, nome_cliente, 123456789, 24)
            reserva = Reserva(1, "30/10/2024", quarto1, cliente, "31/10/2024")
            gerenciador.fazer_reserva(reserva)
        case "0":
            print("Saindo...")
            break
        case _:
            print("Opção inválida! Tente novamente.")
