# A "slang" dictionary...?
# Also, all of the programs are in Spanish. I can't do anything' bout it.
# Some meanings may be outdated.
meme_dict = {
            "cringe": "Algo excepcionalmente raro o vergonzoso. Descripcion mia 100% real no falsa.",
            "lol": "Una respuesta comun a algo gracioso. Significa \"Laughing Out Loud\" en ingles.",
            "rofl": "Respuesta a una bromita o chistecito.",
            "sheesh": "Depende de la persona, o ligera desaprobacion, o señal de respeto o de refutacion a alguien o hacia alguien.",
            "creepy": "Siniestro u aterrador en ingles.",
            "aggro": "Abreviacion de agresivo en ingles."
            }
print("¡Buenas! Bienvenido al MemeDict")
while True:
    word = str(input("Escribe una palabra que no entiendas. Alternativamente, escribe \"H\" para ayuda.").lower())
    if word == "h":
        print("Escribe una palabra con el teclado. Pulsa ENTER. Si la palabra no sale, busca en el Urban Dictionary...")
    elif word in meme_dict.keys():
        print(meme_dict[str(word)])
    else:
        print("Palabra no encontrada.")
