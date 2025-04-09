def verificar_codigo(codigo_correto, tentativas_restantes):
    """
    Verifica o código digitado pelo usuário e controla o número de tentativas restantes.
    """
    while tentativas_restantes > 0:
        entrada_usuario = input("Digite o código: ")

        if entrada_usuario == codigo_correto:
            print("🎉 Código certo! Fechadura aberta! 🎉")
            abrir_fechadura()
            return True  # Retorna sucesso
        else:
            tentativas_restantes -= 1
            if tentativas_restantes > 0:
                print(f"❌ Código errado! Você tem mais {tentativas_restantes} tentativa(s).")
            else:
                print("🚫 Você usou todas as suas tentativas. Fechadura bloqueada!")
    return False  # Retorna falha

def abrir_fechadura():
    """
    Simula o processo de abrir a fechadura e fechá-la após 5 segundos.
    """
    import time
    print("🔓 A fechadura ficará aberta por 5 segundos...")
    time.sleep(5)  # Espera 5 segundos
    print("🔒 Fechadura fechada novamente.")

def main():
    """
    Função principal que inicia o sistema da fechadura digital.
    """
    codigo_correto = "1234"  # Código da fechadura
    tentativas_restantes = 3  # Número de tentativas permitidas

    print("🔒 Bem-vindo à sua fechadura digital!")
    print(f"Você tem {tentativas_restantes} tentativas para acertar o código.")

    sucesso = verificar_codigo(codigo_correto, tentativas_restantes)
    if not sucesso:
        print("😕 Tente novamente mais tarde ou peça ajuda.")

# Inicia o programa
if __name__ == "__main__":
    main()
