#IMPORT FOR CSV READER
import csv
#import random
import random

#WELCOME MESSAGE ===============>
print('======== WELCOME TO OUR COGNITIVE GAME ============')

#OPEN THE CSV
with open('RANDOM_WORDS - Hoja 1.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    #WAIT FOR A CALL FOR DYNAMIC VALUE
    words = [row for row in reader]

# LANGUAGE SELECTION
while True:
    lang = int(input('Put 1 if you want Spanish and 2 if you want English: '))
    if lang == 1:
        print('You have chosen Spanish')
        break
    elif lang == 2:
        print('You have chosen English')
        break

# SELECCIONAMOS UNA SOLA PALABRA RANDOM
random_word = random.choice(words)  # Elegimos una sola palabra aleatoria de la lista

if lang == 1:
    random_spanish = random_word['SPANISH']
    print(random_spanish)
elif lang == 2:
    random_english = random_word['ENGLISH']
    print(random_english)


def switch_case(lang):
    if lang == 1:
        print('======== REGLAS ============')
        print(' ')
        print('Empieza a escribir una palabra de 5 letras.')
        print(' ')
        print('Solo tendrás 5 intentos para adivinar la palabra correcta.')
        print(' ')
        print('Verde = letra y posición correcta')
        print(' ')
        print('Amarillo = letra correcta y posición incorrecta')
        print(' ')
        print('Rojo = letra incorrecta y posición incorrecta')
    elif lang == 2:
        print('======== RULES ============')
        print(' ')
        print('Start typing a word of 5 letters.')
        print(' ')
        print('You will have only 5 attempts to guess the right word.')
        print(' ')
        print('Green = correct letter and correct position')
        print(' ')
        print('Yellow = correct letter but incorrect position')
        print(' ')
        print('Red = incorrect letter and incorrect position')
    else:
        print('Opción no válida. Por favor, elige 1 para español o 2 para inglés.')

# PRINTING RULES
switch_case(lang)
