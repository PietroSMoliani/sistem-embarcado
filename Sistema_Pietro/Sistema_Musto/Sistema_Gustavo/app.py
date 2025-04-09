def ligar_internet(estado_internet):
    if not estado_internet:
        print("🌐 Internet conectada!")
        return True
    else:
        print("🌐 A internet já está ligada.")
        return estado_internet

def desligar_internet(estado_internet):
    if estado_internet:
        print("❌ Internet desconectada!")
        return False
    else:
        print("❌ A internet já está desligada.")
        return estado_internet

def navegar(site, estado_internet):
    if estado_internet:
        print(f"🖥️ Navegando para {site}... Pronto!")
    else:
        print("🚫 Sem internet! Ligue a internet primeiro.")

def menu(estado_internet):
    print("\n=== Sistema de Internet Básico ===")
    print("1. Ligar internet")
    print("2. Desligar internet")
    print("3. Navegar para um site")
    print("4. Sair")
    return estado_internet

def main():
    estado_internet = False
    continuar = True

    while continuar:
        menu(estado_internet)
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            estado_internet = ligar_internet(estado_internet)
        elif opcao == "2":
            estado_internet = desligar_internet(estado_internet)
        elif opcao == "3":
            site = input("Digite o nome do site (exemplo: google.com): ")
            navegar(site, estado_internet)
        elif opcao == "4":
            print("👋 Saindo do sistema. Até logo!")
            continuar = False
        else:
            print("Opção inválida! Tente de novo.")

# Executa o programa
if __name__ == "__main__":
    main()
