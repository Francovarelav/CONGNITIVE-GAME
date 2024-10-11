#IMPORT FOR CSV READER
import csv
#import random
import random

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
