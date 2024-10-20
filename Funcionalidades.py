""" foram definidas 3 funções que serão as funcionalidades do nosso chatbot com
os nome de funcionalidade_denuncia(), funcionalidade_statuslinha(), funcionalidade_bilheteria()
dentro de cada funcionalidade, existe uma ou mais opções
caso nenhuma das opções seja escolhida, o programa retornará ao menu inicial"""

def mostrar_menu():
    print("Menu Principal:")
    print("1. Denúncias")
    print("2. Linha em tempo real")
    print("3. Compra de bilhetes")
    print("0. Sair")

def funcionalidade_denuncia():
    print("Denúncias:")
    print("Digite 1 para fazer sua denúncia")
    escolha = input("Escolha uma opção: ")
    if escolha == '1':
        denuncia = input("Digite sua Denuncia: ")
        print (f'Denuncia recebida, entraremos em contato '
               f'o mais rápido possível \n"{denuncia}"')
        print("Faça sua denúncia aqui")
    else:
        print("Opção inválida.")

def funcionalidade_statuslinha():
    print("Linha em tempo real:")
    print("Digite 1 para ver como está o trajeto da linha 9: ")
    print("Digite 2 para ver como está o trajeto da linha 10: ")
    escolha = input("Escolha uma opção: ")
    if escolha == '1':
        print("O trajeto da linha 9 está fluindo corretamente e sem interrupções.")
    elif escolha == '2':
        print("O trajeto da linha 10 está com lotação máxima no momento,"
              " tempo de espera aproximado de 5 minutos.")
    else:
        print("Opção inválida.")

def funcionalidade_bilheteria():
    print("Compra de bilhetes:")
    print("Digite 1 se você deseja gerar um QR code para a compra de bilhetes: ")
    print("Digite 2 se você deseja gerar um pix copia/cola para a compra de bilhetes: ")
    escolha = input("Escolha uma opção: ")
    if escolha == '1':
        preco_qrcode = 5.00
        quantidade_qrcode = float(input("Quantos bilhetes?"))
        print(f'um QR Code no valor de {preco_qrcode*quantidade_qrcode} reais '
              f' está sendo gerado')
    elif escolha == '2':
        preco_pix = 5.00
        quantidade_pix = float(input("Quantos bilhetes?"))
        print(f' um pix Copia/cola no valor de {preco_pix*quantidade_pix} reais' 
              f' está sendo gerado')
    else:
        print("Opção inválida.")


"""Definida a função main para rodar o programa sem erro.
A função while True foi utilizada para manter o programa em loop até
o usuário decidir sair.
O loop foi constituído pela função mostrar_menu() que exibe as opções do programa.
"""
def main():
    while True:
        mostrar_menu()
        escolha = input("Escolha uma funcionalidade: ")
        if escolha == '1':
            funcionalidade_denuncia()
        elif escolha == '2':
            funcionalidade_statuslinha()
        elif escolha == '3':
            funcionalidade_bilheteria()
        elif escolha == '0':
            print("Saindo do programa...")
            break
        else:
            print("Funcionalidade inválida. Tente novamente.")

if __name__ == "__main__":
    main()