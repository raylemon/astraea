from lib.beans import *


def menu():
    print("""
            Génération d’interrogations / examen

        1.  Conversions 10 -> Bases binaires    (1 octet non signé)
        2.  Conversions toutes bases            (1 octet non signé)
        3.  Compléments à 2 (Cà2)               (1 octet)
        4.  Arithmétique (+)                    (1 octet)
        5.  Arithmétique (-)                    (1 octet)
        6.  Arithmétique (×)                    (1 octet)
        7.  Arithmétique (÷)                    (1 octet)
        8.  Décimal -> Flottant                 (2 octets)
        9.  Flottant -> Décimal                 (2 octets)
        10.  Encodage / Décodage de CRC
        11.  Encodage de Hamming
        12.  Décodage de Hamming
        Q.  Quitter l'application
    """.center(80))


def show_exercise(mode):
    exercise = None
    s_key = ''
    while s_key != 'Q':
        if mode == '1':
            exercise = Convert(base_src=10, base_dst=choose_bin_base())
        elif mode == '2':
            exercise = Convert()
        elif mode == '3':
            exercise = Ca2()
        elif mode == '4':
            exercise = Arith(op='+')
        elif mode == '5':
            exercise = Arith(op='-')
        elif mode == '6':
            exercise = Arith(op='×')
        elif mode == '7':
            exercise = Arith(op='÷')
        elif mode == '8':
            exercise = DecimalToFloat16()
        elif mode == '9':
            exercise = Float16ToDecimal()
        elif mode == '10':
            exercise = Crc()
        elif mode == '11':
            exercise = HammingMessage(encoded=True)
        elif mode == '12':
            exercise = HammingMessage(encoded=False)
        print(exercise.statement,"\t",exercise.solution)
        s_key = input("\nTaper Q pour revenir au menu, ou une autre touche pour afficher un nouvel exercice: ").upper() or ' '
    menu()


if __name__ == '__main__':
    print("GenIE")
    key = ''
    menu()
    while key != 'Q':
        key = input("Votre choix ?").upper()
        if not key == 'Q':
            show_exercise(key)
    exit(0)