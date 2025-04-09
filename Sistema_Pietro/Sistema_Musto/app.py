import time
import random

def pegar_temperatura():
    """
    Pega uma temperatura de brincadeira (aleatória entre 18°C e 35°C).
    """
    return random.randint(18, 35)

def ligar_ou_desligar_ar(temperatura, temperatura_certa):
    """
    Liga ou desliga o ar-condicionado, dependendo da temperatura.
    """
    if temperatura > temperatura_certa:
        print(f"🔥 Está {temperatura}°C! Tá quente! Ligando o ar-condicionado.")
        return "ligado"
    else:
        print(f"😎 Está {temperatura}°C. Tá fresquinho! Desligando o ar-condicionado.")
        return "desligado"

print("🌬️ Bem-vindo ao controle do ar-condicionado!")
temperatura_certa = int(input("Qual a temperatura que você quer (°C)? "))

estado_do_ar = "desligado"

try:
    while True:
        # Imagina que o ar lê a temperatura do ambiente
        temperatura_atual = pegar_temperatura()

        # O ar decide se liga ou desliga
        novo_estado = ligar_ou_desligar_ar(temperatura_atual, temperatura_certa)

        # Só avisa se mudou de "ligado" pra "desligado"
        if novo_estado != estado_do_ar:
            estado_do_ar = novo_estado
            print(f"O ar-condicionado agora está {estado_do_ar}.\n")

        # Espera 3 segundos antes de ver a temperatura de novo
        time.sleep(3)

except KeyboardInterrupt:
    print("\n🎮 Sistema desligado! Fui brincar!")
