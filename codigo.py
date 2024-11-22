import random
print("El camino al reino Hyrule\n")
print("El reino de Hyrule ha sido un bastión de paz y prosperidad por siglos, pero ahora enfrenta una amenaza insólita: un ejército de pequeños y tiernos chihuahuas malvados. La única esperanza del reino está en la mítica piedra Katuspanti, una gema legendaria que contiene la luz eterna capaz de ahuyentar cualquier oscuridad. Sin embargo, su poder está sellado y sólo puede ser liberado por un héroe que demuestre su valía enfrentando pruebas imposibles.El último guardián de la piedra es Ludwig el Temerario, conocido en todos los reinos como El Gran Apostador. Este peculiar personaje es famoso por su habilidad para crear juegos  y su risa extravagante: ¡JAJAJA! ¿Crees que puedes vencerme, viajero. Ludwig lleva un sombrero ridículamente grande, lentes oscuros que no necesita, y un traje lleno de colores brillantes. Su mascota es un hámster llamado Waffle, un campeón imbatible en las carreras de bolas de hámster. (Si quieres la piedra, viajero, primero debes ganarle a Torbellino. Pero cuidado… ¡nadie lo ha vencido jamás!\n)")
print("¡Lanza tu hamster ajustando las variables físicas para llegar al final de la carrera y lograr salvar a tu reino!.\n")
    
def ctrabajo(fuerza, desplazamiento):
    return fuerza * desplazamiento

def cimpulso(fuerza, t):
    return fuerza * t



distancia_total = 1000  # Metros
energia_disponible = 5000  # Joules
velocidad_actual = 0  # 

while distancia_total > 0 and energia_disponible > 0:
        print(f"Distancia restante: {distancia_total} m")
        print(f"Energía disponible: {energia_disponible} J\n")
        fuerza = int(input("Ingresa la fuerza de la bola hamster (en N, entre 10 y 100): "))
        t = int(input("Ingresa el tiempo de empuje (en s, entre 1 y 10): "))
        trabajo = ctrabajo(fuerza, t)
        impulso = cimpulso(fuerza, t)
        
        energia_disponible -= trabajo
        distancia_recorrida = impulso / 10  # Simplificación para el ejemplo
        distancia_total -= distancia_recorrida
        print(f"\nRealizaste un trabajo de {trabajo} J y generaste un impulso de {impulso} N·s.")
        print(f"Avanzaste {distancia_recorrida:.2f} metros.\n")
        if random.random() < 0.2:
            perdida = random.randint(50, 100)
            print(f"¡Oh no! Una rana flotante dañó a tu hamster y perdiste {perdida} J de energía.\n")
            energia_disponible -= perdida

if distancia_total <= 0:
    print("MISIÓN CUMPLIDA/n")
    print("El público estalla en gritos de asombro mientras tu hámster cruza la línea de meta, dejando atrás a Waffle por un pelo. Ludwig, sorprendido, deja caer su sombrero y dice:¡No puede ser! ¡Has vencido a Waffle! Bueno... un trato es un trato.Con una sonrisa forzada, Ludwig te entrega la piedra Katuspanti, y esta empieza a brillar intensamente en tus manos.Disfruta tu victoria, viajero. Pero recuerda, nos volveremos a ver"
"Levantas la piedra con orgullo mientras el público celebra. Tu misión está un paso más cerca de salvar al reino.")
else:
    print("DERROTA.")
    print("Puedes intentarlo de nuevo... si tienes algo más que apostar. Hasta entonces, la piedra Katuspanti sigue siendo mía.")
