bateria = int(input("Nível de bateria (0 a 100): "))
temperatura = float(input("Temperatura do ambiente (°C): "))
umidade = int(input("Umidade do solo (0 a 100): "))
modo = input("Modo de operação (plantio, colheita, irrigação): ")



if bateria < 20:
    print("Bateria muito baixa! Retorne imediatamente para a base.")

if bateria >= 20:
    if bateria < 50:
        print("Atenção: bateria em nível moderado.")

if bateria >= 50:
    print("Bateria suficiente para operação.")


if temperatura > 40:
    print("Temperatura crítica! Operação suspensa.")

if temperatura < 5:
    print("Frio extremo! Modo de economia ativado.")


if umidade < 30:
    print("Solo muito seco. Recomendado iniciar irrigação.")

if umidade > 80:
    print("Solo encharcado! Suspenda irrigação imediatamente.")


if modo == "plantio":
    print("Iniciando modo PLANTIO...")

if modo == "colheita":
    print("Iniciando modo COLHEITA...")

if modo == "irrigação":
    print("Iniciando modo IRRIGAÇÃO...")



autorizado = True  
if bateria < 50:
    autorizado = False


if temperatura < 10:
    autorizado = False

if temperatura > 35:
    autorizado = False


if umidade < 30:
    autorizado = False

if umidade > 80:
    autorizado = False

if autorizado == True:
    print("Robô autorizado a iniciar a operação!")

if autorizado == False:
    print("Operação negada! Verifique as condições do ambiente.")
