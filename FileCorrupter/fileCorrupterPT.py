from random import randrange

# working!! finished version a1 in 23/06/2022 at 19:12

allTheCharacters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-=´[~],.;!@#$%¨&*()_+`{^}<>:|'£¢¬§/?°/₢ºª "

nameOfTheFile = input('Nome do arquivo (ex. "Arquivo.txt")\n>')

fileToCorrupt = open(nameOfTheFile, "wt")
fileSizeUnit = input("\nEscreva a unidade de medida to tamanho do arquivo (ex. gb, mb, kb, b)\n>")
fileActualUnit = 0
if fileSizeUnit == 'b':
    fileActualUnit = 1
if fileSizeUnit == 'kb':
    fileActualUnit = 1000
if fileSizeUnit == 'mb':
    fileActualUnit = 1000000
if fileSizeUnit == 'gb':
    fileActualUnit = 1000000000

fileSize = input("\nO tamanho do arquivo em {}s\n>".format(fileSizeUnit))

fileToCorrupt.write("File Corrupter Version a1 by ChaoticFurry @ 2022\n")
fileToCorrupt.close()

fileToCorrupt2 = open(nameOfTheFile, "at")

sizeWhy = float(fileSize) * fileActualUnit * 1.01419878296146  # ** DON'T TOUCH THE LONG NUMBER **!!!
                                                               # a file with 100 kb chosen would end up with 98.6 kb,
                                                               # and doing the division (100/98,6) we get to that constant.
                                                               # surprisingly enough, it actually works lmao 23/06/22 19:11
for i in range(int(sizeWhy)):
    if (randrange(0, 100)) == 0:
        fileToCorrupt2.write("\n")
    else:
        fileToCorrupt2.write(allTheCharacters[randrange(0, 100)])


fileToCorrupt2.close()
