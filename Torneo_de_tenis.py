def solicitar_ganador(partido):
    ganador = input(f"{partido[0]} - {partido[1]}: ")
    return ganador.upper()

def jugar_campeonato():
    tenistas = [input(f"Jugador {i + 1}: ") for i in range(8)]

    rondas = [tenistas]

    while len(rondas[-1]) > 1:
        nueva_ronda = []

        for i in range(0, len(rondas[-1]), 2):
            partido = (rondas[-1][i], rondas[-1][i + 1])
            ganador = solicitar_ganador(partido)
            nueva_ronda.append(ganador)

        rondas.append(nueva_ronda)

    print(f"\nCampeon: {rondas[-1][0]}")

jugar_campeonato()
