import datetime
import time

def alarme():
    global alarm_time
    heures = int(input("Entrez les heures: "))
    minutes = int(input("Entrez les minutes: "))
    secondes = int(input("Entrez les secondes: "))
    alarm_time = datetime.datetime.now().replace(hour=heures, minute=minutes, second=secondes)
    print("Alarme enregistrée !!")
    return(True)


def horloge():
    print("Configuration de l'horloge")
    heures = int(input("Entrez les heures: "))
    minutes = int(input("Entrez les minutes: "))
    secondes = int(input("Entrez les secondes: "))
    if 0 <= heures <= 24:
        if 0 <= minutes <= 59:
            if 0<= secondes <= 59:
                    current_time = datetime.datetime.now().replace(hour=heures, minute=minutes, second=secondes)
                    temps = datetime.timedelta(seconds=1)

                    while True:
                        updated_time = current_time + temps
                        current_time = updated_time
                        result = current_time.strftime("%H:%M:%S")
                        print("\n\n         +~~~~~~~~~~~~~~~~~~~+")
                        print(f"         |      {result}     |")
                        print("         +~~~~~~~~~~~~~~~~~~~+\n\n")
                        if alarm_time.strftime("%H:%M:%S") == current_time.strftime("%H:%M:%S"):
                            print("DRING DRING DRING")
                            question = input("Relancer l'horloge ? (oui ou non) : ")
                            if question == "oui":
                                horlogev2()
                            break
                        else:
                            time.sleep(1)

def horlogev2():
    print("Configuration de l'horloge")
    heures = int(input("Entrez les heures: "))
    minutes = int(input("Entrez les minutes: "))
    secondes = int(input("Entrez les secondes: "))
    if 0 <= heures <= 24:
        if 0 <= minutes <= 59:
            if 0<= secondes <= 59:
                    current_time = datetime.datetime.now().replace(hour=heures, minute=minutes, second=secondes)
                    temps = datetime.timedelta(seconds=1)

                    while True:
                        updated_time = current_time + temps
                        current_time = updated_time
                        result = current_time.strftime("%H:%M:%S")
                        print("\n\n         +~~~~~~~~~~~~~~~~~~~+")
                        print(f"         |      {result}     |")
                        print("         +~~~~~~~~~~~~~~~~~~~+\n\n")
                        time.sleep(1)
                        



def main():
    alarm = input("Voulez vous mettre en place une alarme ?( oui ou non : ")
    if alarm == "oui":
        alarme()
        horloge()
    else:
        horlogev2()

main()
