# -*- coding: cp1252 -*-
#Skrevet i Python 2.7
import pygame
print "Laget av Hans Jorgen for Kiwi Tertnes"
print "Vennligst ta i bruk Highscore vedlegg for a legge til poeng \n"
import random, math, os
loop1 = True
loop2 = False
gameover = False
deltakere = []
oppgave = 0

def filepath(filename):
    data_dir = os.path.normpath(os.path.join(''))
    return os.path.join(data_dir, filename)

def load(filename, mode='rb'):
    return open(os.path.join(data_dir, filename), mode)
    
while loop1 == True:
    open("highscore.sav", "w").write(str())
    try:
        spillere = int(raw_input("Hvor mange spillere deltar? "))
    except(TypeError, ValueError):
            print ("Ma vare et siffer")
            continue

    for i in range(spillere):
        navn = raw_input("Skriv navn: ")
        deltakere.append(navn)
        f = open(filepath("highscore.sav"), "w")
        f.write("Spillere: \n"), f.write("\n")
        lst = '\n'.join(deltakere)
        f.write(lst)
        f.write("\n\n"), f.write("Lag: ")
        f.close()
        intro_complete = True
        loop1 = False
    
    #INTRO
    print ""
    print deltakere, "-", spillere, "spillere har deltatt. Velkommen til Kiwi PLU spill."
    print "Lykke til! \n"

if intro_complete == True:
    os.startfile("highscore.sav")
    loop2 = True

print "- Les oppgavene godt - \n"

while loop2 == True:
    oppgave += 1
    def feil():
        print ""
        print "Feil svar"
        print "Prov igjen"
        print ""
    PLU = ["Banan", "Agurk", "Rode Epler", "Klementiner", "Gule Epler", "Gronne Epler",
           "Varlok", "Smagodt i pose", "Smagodt i beger", "Blomkal", "Brokkoli", "Tomater",
           "Grillkull", "Sellerirot", "Pastinakk", "Persillerot", "Notter Losvekt", "Mandler Losvekt",
           "Pepsi Max 4pk", "Coca Cola 4pk", "Ananas", "Kokosnott", "Parer", "Asparges", "Aubergine",
           "MyPack", "Avokado", "Fennikel", "Kinakal", "Hodekal", "Nykal", "Ingefer", "Kalrot", "Rod Paprika",
           "Gronn Paprika", "Squash", "Champignon/Sjampinjong", "Stangselleri", "Sotpotet", "Appelsiner", "Nektarin",
           "Granateple", "Kiwi Stk", "Lime", "Moreller", "Mango", "Jordber Kurv Import", "Purrelok", "Paprika Trafikklys",
           "Paprika Sotspisset 2pk", "Nypoteter Losvekt", "Poteter Losvekt", "Grapefrukt", "Lok Losvekt", "Bakepoteter",
           "Sharon Persimon", "First Price Bananer", "Okologiske Bananer", "Dadler", "Fersken", "Vannmelon Hel",
           "Vannmelon Delt", "Melon Piel de Sapo", "Honningmelon", "Cantaloupe Melon", "Galia Melon", "Rabarbra",
           "Sitron", "Jordber Norske Kurv", "Nektarin Kurv", "Neper Bunt", "Plommer Rod/Bla", "Rettich", "Rodkal",
           "Kiwi Pluss", "Reker", "Reker 5kg 90/130 Stor Eske", "Vedsekk", "Farin 10kg", "Hvetemel 4x2kg",
           "Tvist Grov Piripiri", "Kornbaguette", "Sommerbolle", "Skillingsbolle", "Skolebrod", "Solskinnsbolle",
           "Kanelknute", "Wienerbrod", "Rundstykke Fint", "Rundstykke Grov/Kneip", "Ostehorn", "Ostebaguette",
           "Lunsjhjul", "Frokostbrod Gammel", "Energistykke", "Croissant", "Minipizza", "Havrebrix", "Tebrix",
           "Fyrstikkeske", "Pant/Tom Kasse", "Cola Zero 1.25l 6pk", "Coca Cola 8pk", "Pepsi Max 8pk", "Cola Zero 4pk",
           "Cola Zero 8pk", "Pepsi Max 6pk", "Knutekal", "Bringeber Eske", "Fiken stk", "Sukkererter Losvekt", "Gronne Druer Losvekt",
           "Isberg Salat", "Rode Druer Losvekt"]
    chosen_word = random.choice(PLU)
    print "Oppgave:", oppgave
    print chosen_word
    svar = ["4011", "4316", "4015", "4055", "4021", "4139", "4068", "9009", "509", "4079", "4349",
            "4064", "9035", "4390", "4363", "4671", "9018", "4924", "5670", "9534", "4430", "4260", "3017",
            "4080", "4081", "9980", "4222", "4515", "4355", "3050", "3051", "4612", "4747", "4088", "4065", "4067",
            "4645", "4380", "4091", "4196", "4036", "4445", "4030", "4048", "4045", "4049", "3355", "4629", "4362",
            "4702", "4083", "4073", "4281", "4358", "4367", "4428", "4186", "94011", "3047", "4038", "4032", "4031",
            "3101", "4317", "4049", "3033", "4326", "4745", "4033", "4197", "4276", "4810", "4041", "4740", "4554",
            "1100", "1900", "1895", "9464", "9050", "9997", "2008", "2009", "2013", "2039", "2040", "2042", "2047",
            "2048", "2089", "2084", "2085", "6882", "2297", "2502", "2075", "2651", "2854", "6085", "9060", "9063",
            "9010", "9011", "9995", "9090", "9045", "9535", "9061", "9301", "4628", "3081", "4267", "4675", "4274", "4376",
            "4056"]
    guess = (raw_input("Hva er PLU Koden: "))
    if guess in ["quit", "Quit", "QUIT"]:
        gameover = True
        loop2 = False
        break
    if guess in svar:
        if guess == "4011":
            if chosen_word == "Banan":
                print"Svar = Banan, Riktig"
                print""
            else:
                feil()
        elif guess == "4316":
            if chosen_word == "Agurk":
                print"Svar = Agurk, Riktig"
                print""
            else:
                feil()
        elif guess == "4015":
            if chosen_word == "Rode Epler":
                print"Svar = Rode Epler, Riktig"
                print ""
            else:
                feil()
        elif guess == "4055":
            if chosen_word == "Klementiner":
                print"Svar = Klementiner, Riktig"
                print ""
            else:
                feil()
        elif guess == "4021":
            if chosen_word == "Gule Epler":
                print"Svar = Gule Epler, Riktig"
                print ""
            else:
                feil()
        elif guess == "4139":
            if chosen_word == "Gronne Epler":
                print"Svar = Gronne Epler, Riktig"
                print ""
            else:
                feil()
        elif guess == "4068":
            if chosen_word == "Varlok":
                print"Svar = Varlok, Riktig"
                print ""
            else:
                feil()
        elif guess == "9009":
            if chosen_word == "Smagodt i pose":
                print"Svar = Smagodt i Pose, Riktig"
                print ""
            else:
                feil()
        elif guess == "509":
            if chosen_word == "Smagodt i beger":
                print"Svar = Smagodt i Beger, Riktig"
                print ""
            else:
                feil()
        elif guess == "4079":
            if chosen_word == "Blomkal":
                print"Svar = Blomkal, Riktig"
                print ""
            else:
                feil()
        elif guess == "4349":
            if chosen_word == "Brokkoli":
                print"Svar = Brokkoli, Riktig"
                print ""
            else:
                feil()
        elif guess == "9035":
            if chosen_word == "Grillkull":
                print"Svar = Grillkull, Riktig"
                print ""
            else:
                feil()
        elif guess == "4390":
            if chosen_word == "Sellerirot":
                print"Svar = Sellerirot, Riktig"
                print ""
            else:
                feil()
        elif guess == "4363":
            if chosen_word == "Pastinakk":
                print"Svar = Pastinakk, Riktig"
                print ""
            else:
                feil()
        elif guess == "4671":
            if chosen_word == "Persillerot":
                print"Svar = Persillerot, Riktig"
                print ""
            else:
                feil()
        elif guess == "9018":
            if chosen_word == "Notter Losvekt":
                print"Svar = Notter Losvekt, Riktig"
                print ""
            else:
                feil()
        elif guess == "4924":
            if chosen_word == "Mandler Losvekt":
                print"Svar = Mandler Losvekt, Riktig"
                print ""
            else:
                feil()
        elif guess == "5670":
            if chosen_word == "Pepsi Max 4pk":
                print"Svar = Pepsi Max 4pk, Riktig"
                print ""
            else:
                feil()
        elif guess == "9534":
            if chosen_word == "Coca Cola 4pk":
                print"Svar = Coca Cola 4pk, Riktig"
                print ""
            else:
                feil()
        elif guess == "4430":
            if chosen_word == "Ananas":
                print"Svar = Ananas, Riktig"
                print ""
            else:
                feil()
        elif guess == "4260":
            if chosen_word == "Kokosnott":
                print"Svar = Kokosnott, Riktig"
                print ""
            else:
                feil()
        elif guess == "3017":
            if chosen_word == "Parer":
                print"Svar = Parer, Riktig"
                print ""
            else:
                feil()
        elif guess == "4080":
            if chosen_word == "Asparges":
                print"Svar = Asparges, Riktig"
                print ""
            else:
                feil()
        elif guess == "4081":
            if chosen_word == "Aubergine":
                print"Svar = Aubergine, Riktig"
                print ""
            else:
                feil()
        elif guess == "9980":
            if chosen_word == "MyPack":
                print"Svar = MyPack, Riktig"
                print ""
            else:
                feil()
        elif guess == "4222":
            if chosen_word == "Avokado":
                print"Svar = Avokado, Riktig"
                print ""
            else:
                feil()
        elif guess == "4515":
            if chosen_word == "Fennikel":
                print"Svar = Fennikel, Riktig"
                print ""
            else:
                feil()
        elif guess == "4355":
            if chosen_word == "Kinakal":
                print"Svar = Kinakal, Riktig"
                print ""
            else:
                feil()
        elif guess == "3050":
            if chosen_word == "Hodekal":
                print"Svar = Hodekal, Riktig"
                print ""
            else:
                feil()
        elif guess == "3051":
            if chosen_word == "Nykal":
                print"Svar = Nykal, Riktig"
                print ""
            else:
                feil()
        elif guess == "4612":
            if chosen_word == "Ingefer":
                print"Svar = Ingefer, Riktig"
                print ""
            else:
                feil()
        elif guess == "4747":
            if chosen_word == "Kalrot":
                print"Svar = Kalrot, Riktig"
                print ""
            else:
                feil()
        elif guess == "4088":
            if chosen_word == "Rod Paprika":
                print"Svar = Rod Paprika, Riktig"
                print ""
            else:
                feil()
        elif guess == "4065":
            if chosen_word == "Gronn Paprika":
                print"Svar = Gronn Paprika, Riktig"
                print ""
            else:
                feil()
        elif guess == "4067":
            if chosen_word == "Squash":
                print"Svar = Squash, Riktig"
                print ""
            else:
                feil()
        elif guess == "4645":
            if chosen_word == "Champignon/Sjampinjong":
                print"Svar = Champignon/Sjampinjong, Riktig"
                print ""
            else:
                feil()
        elif guess == "4380":
            if chosen_word == "Stangselleri":
                print"Svar = Stangselleri, Riktig"
                print ""
            else:
                feil()
        elif guess == "4091":
            if chosen_word == "Sotpotet":
                print"Svar = Sotpotet, Riktig"
                print ""
            else:
                feil()
        elif guess == "4196":
            if chosen_word == "Appelsiner":
                print"Svar = Appelsiner, Riktig"
                print ""
            else:
                feil()
        elif guess == "4036":
            if chosen_word == "Nektarin":
                print"Svar = Nektarin, Riktig"
                print ""
            else:
                feil()
        elif guess == "4445":
            if chosen_word == "Granateple":
                print"Svar = Granateple, Riktig"
                print ""
            else:
                feil()
        elif guess == "4030":
            if chosen_word == "Kiwi Stk":
                print"Svar = Kiwi Stk, Riktig"
                print ""
            else:
                feil()
        elif guess == "4048":
            if chosen_word == "Lime":
                print"Svar = Lime, Riktig"
                print ""
            else:
                feil()
        elif guess == "4045":
            if chosen_word == "Moreller":
                print"Svar = Moreller, Riktig"
                print ""
            else:
                feil()
        elif guess == "4049":
            if chosen_word == "Mango":
                print"Svar = Mango, Riktig"
                print ""
            else:
                feil()
        elif guess == "3355":
            if chosen_word == "Jordber Kurv Import":
                print"Svar = Jordber Kurv Import, Riktig"
                print ""
            else:
                feil()
        elif guess == "4629":
            if chosen_word == "Purrelok":
                print"Svar = Purrelok, Riktig"
                print ""
            else:
                feil()
        elif guess == "4362":
            if chosen_word == "Paprika Trafikklys":
                print"Svar = Paprika Trafikklys, Riktig"
                print ""
            else:
                feil()
        elif guess == "4702":
            if chosen_word == "Paprika Sotspisset 2pk":
                print"Svar = Paprika Sotspisset 2pk, Riktig"
                print ""
            else:
                feil()
        elif guess == "4083":
            if chosen_word == "Nypoteter Losvekt":
                print"Svar = Nypoteter Losvekt, Riktig"
                print ""
            else:
                feil()
        elif guess == "4073":
            if chosen_word == "Poteter Losvekt":
                print"Svar = Poteter Losvekt, Riktig"
                print ""
            else:
                feil()
        elif guess == "4281":
            if chosen_word == "Grapefrukt":
                print"Svar = Grapefrukt, Riktig"
                print ""
            else:
                feil()
        elif guess == "4358":
            if chosen_word == "Lok Losvekt":
                print"Svar = Lok Losvekt, Riktig"
                print ""
            else:
                feil()
        elif guess == "4367":
            if chosen_word == "Bakepoteter":
                print"Svar = Bakepoteter, Riktig"
                print ""
            else:
                feil()
        elif guess == "4428":
            if chosen_word == "Sharon Persimon":
                print"Svar = Sharon Persimon, Riktig"
                print ""
            else:
                feil()
        elif guess == "4186":
            if chosen_word == "First Price Bananer":
                print"Svar = First Price Bananer, Riktig"
                print ""
            else:
                feil()
        elif guess == "94011":
            if chosen_word == "Okologiske Bananer":
                print"Svar = Okologiske Bananer, Riktig"
                print ""
            else:
                feil()
        elif guess == "3047":
            if chosen_word == "Dadler":
                print"Svar = Dadler, Riktig"
                print ""
            else:
                feil()
        elif guess == "4038":
            if chosen_word == "Fersken":
                print"Svar = Fersken, Riktig"
                print ""
            else:
                feil()
        elif guess == "4032":
            if chosen_word == "Vannmelon Hel":
                print"Svar = Vannmelon Hel, Riktig"
                print ""
            else:
                feil()
        elif guess == "4031":
            if chosen_word == "Vannmelon Delt":
                print"Svar = Vannmelon Delt, Riktig"
                print ""
            else:
                feil()
        elif guess == "3101":
            if chosen_word == "Melon Piel de Sapo":
                print"Svar = Melon Piel de Sapo, Riktig"
                print ""
            else:
                feil()
        elif guess == "4317":
            if chosen_word == "Honningmelon":
                print"Svar = Honningmelon, Riktig"
                print ""
            else:
                feil()
        elif guess == "4049":
            if chosen_word == "Cantaloupe Melon":
                print"Svar = Cantaloupe Melon Riktig"
                print ""
            else:
                feil()
        elif guess == "3033":
            if chosen_word == "Cantaloupe Melon":
                print"Svar = Cantaloupe Melon Riktig"
                print ""
            else:
                feil()
        elif guess == "4326":
            if chosen_word == "Galia Melon":
                print"Svar = Galia Melon Riktig"
                print ""
            else:
                feil()
        elif guess == "4745":
            if chosen_word == "Rabarbra":
                print"Svar = Rabarbra, Riktig"
                print ""
            else:
                feil()
        elif guess == "4033":
            if chosen_word == "Sitron":
                print"Svar = Sitron, Riktig"
                print ""
            else:
                feil()
        elif guess == "4197":
            if chosen_word == "Jordber Norske Kurv":
                print"Svar = Jordber Norske Kurv, Riktig"
                print ""
            else:
                feil()
        elif guess == "4276":
            if chosen_word == "Nektarin Kurv":
                print"Svar = Nektarin Kurv, Riktig"
                print ""
            else:
                feil()
        elif guess == "4810":
            if chosen_word == "Neper Bunt":
                print"Svar = Rabarbra, Riktig"
                print ""
            else:
                feil()
        elif guess == "4041":
            if chosen_word == "Plommer Rod/Bla":
                print"Svar = Plommer Rod/Bla, Riktig"
                print ""
            else:
                feil()
        elif guess == "4740":
            if chosen_word == "Rettich":
                print"Svar = Rettich, Riktig"
                print ""
            else:
                feil()
        elif guess == "4554":
            if chosen_word == "Rodkal":
                print"Svar = Rodkal, Riktig"
                print ""
            else:
                feil()
        elif guess == "1100":
            if chosen_word == "Kiwi Pluss":
                print"Svar = Kiwi Pluss, Riktig"
                print ""
            else:
                feil()
        elif guess == "1900":
            if chosen_word == "Reker":
                print"Svar = Reker, Riktig"
                print ""
            else:
                feil()
        elif guess == "1895":
            if chosen_word == "Reker 5kg 90/130 Stor Eske":
                print"Svar = Reker 5kg 90/130 Stor Eske Riktig"
                print ""
            else:
                feil()
        elif guess == "9464":
            if chosen_word == "Vedsekk":
                print"Svar = Vedsekk, Riktig"
                print ""
            else:
                feil()
        elif guess == "9050":
            if chosen_word == "Farin 10kg":
                print"Svar = Farin 10kg, Riktig"
                print ""
            else:
                feil()
        elif guess == "9997":
            if chosen_word == "Hvetemel 4x2kg":
                print"Svar = Reker, Riktig"
                print ""
            else:
                feil()
        elif guess == "2008":
            if chosen_word == "Tvist Grov Piripiri":
                print"Svar = Twivst Grov Piripiri, Riktig"
                print ""
            else:
                feil()
        elif guess == "2009":
            if chosen_word == "Kornbaguette":
                print"Svar = Kornbaguette, Riktig"
                print ""
            else:
                feil()
        elif guess == "2013":
            if chosen_word == "Sommerbolle":
                print"Svar = 2013, Riktig"
                print ""
            else:
                feil()
        elif guess == "2039":
            if chosen_word == "Skillingsbolle":
                print"Svar = Skillingsbolle, Riktig"
                print ""
            else:
                feil()
        elif guess == "2040":
            if chosen_word == "Skolebrod":
                print"Svar = Skolebrod, Riktig"
                print ""
            else:
                feil()
        elif guess == "2042":
            if chosen_word == "Solskinnsbolle":
                print"Svar = Solskinnsbolle, Riktig"
                print ""
            else:
                feil()
        elif guess == "2047":
            if chosen_word == "Kanelknute":
                print"Svar = Kanelknute, Riktig"
                print ""
            else:
                feil()
        elif guess == "2048":
            if chosen_word == "Wienerbrod":
                print"Svar = Wienerbrod, Riktig"
                print ""
            else:
                feil()
        elif guess == "2089":
            if chosen_word == "Wienerbrod":
                print"Svar = Wienerbrod, Riktig"
                print ""
            else:
                feil()
        elif guess == "2084":
            if chosen_word == "Rundstykke Fint":
                print"Svar = Rundstykke Fint, Riktig"
                print ""
            else:
                feil()
        elif guess == "2085":
            if chosen_word == "Rundstykke Grov/Kneip":
                print"Svar = Rundstykke Grov/Kneip, Riktig"
                print ""
            else:
                feil()
        elif guess == "6882":
            if chosen_word == "Ostehorn":
                print"Svar = Ostehorn, Riktig"
                print ""
            else:
                feil()
        elif guess == "2297":
            if chosen_word == "Ostebaguette":
                print"Svar = Ostebaguette, Riktig"
                print ""
            else:
                feil()
        elif guess == "2502":
            if chosen_word == "Lunsjhjul":
                print"Svar = Lunsjhjul, Riktig"
                print ""
            else:
                feil()
        elif guess == "2075":
            if chosen_word == "Frokostbrod Gammel":
                print"Svar = Frokostbrod Gammel, Riktig"
                print ""
            else:
                feil()
        elif guess == "2651":
            if chosen_word == "Energistykke":
                print"Svar = Energistykke, Riktig"
                print ""
            else:
                feil()
        elif guess == "2854":
            if chosen_word == "Croissant":
                print"Svar = Croissant, Riktig"
                print ""
            else:
                feil()
        elif guess == "6085":
            if chosen_word == "Minipizza":
                print"Svar = Minipizza, Riktig"
                print ""
            else:
                feil()
        elif guess == "9060":
            if chosen_word == "Havrebrix":
                print"Svar = Havrebrix, Riktig"
                print ""
            else:
                feil()
        elif guess == "9063":
            if chosen_word == "Tebrix":
                print"Svar = Tebrix, Riktig"
                print ""
            else:
                feil()
        elif guess == "9010":
            if chosen_word == "Fyrstikkeske":
                print"Svar = Fyrstikkeske, Riktig"
                print ""
            else:
                feil()
        elif guess == "9011":
            if chosen_word == "Pant/Tom Kasse":
                print"Svar = Pant/Tom Kasse, Riktig"
                print ""
            else:
                feil()
        elif guess == "9995":
            if chosen_word == "Cola Zero 1.25l 6pk":
                print"Svar = Cola Zero 1.25l 6pk, Riktig"
                print ""
            else:
                feil()
        elif guess == "9090":
            if chosen_word == "Coca Cola 8pk":
                print"Svar = Coca Cola 8pk, Riktig"
                print ""
            else:
                feil()
        elif guess == "9045":
            if chosen_word == "Pepsi Max 8pk":
                print"Svar = Pepsi Max 8pk, Riktig"
                print ""
            else:
                feil()
        elif guess == "9035":
            if chosen_word == "Cola Zero 4pk":
                print"Svar = Coca Zero 4pk, Riktig"
                print ""
            else:
                feil()
        elif guess == "9061":
            if chosen_word == "Cola Zero 8pk":
                print"Svar = Coca Zero 8pk, Riktig"
                print ""
            else:
                feil()
        elif guess == "9301":
            if chosen_word == "Pepsi Max 6pk":
                print"Svar = Pepsi Max 6pk, Riktig"
                print ""
            else:
                feil()
        elif guess == "4628":
            if chosen_word == "Knutekal":
                print"Svar = Knutekal, Riktig"
                print ""
            else:
                feil()
        elif guess == "3081":
            if chosen_word == "Bringeber Eske":
                print"Svar = Bringeber Eske, Riktig"
                print ""
            else:
                feil()
        elif guess == "4267":
            if chosen_word == "Fiken":
                print"Svar = Fiken, Riktig"
                print ""
            else:
                feil()
        elif guess == "4675":
            if chosen_word == "Sukkererter Losvekt":
                print"Svar = Sukkererter Losvekt, Riktig"
                print ""
            else:
                feil()
        elif guess == "4274":
            if chosen_word == "Gronne Druer Losvekt":
                print"Svar = Gronne Druer Losvekt, Riktig"
                print ""
            else:
                feil()
        elif guess == "4376":
            if chosen_word == "Isberg Salt":
                print"Svar = Isberg Salat, Riktig"
                print ""
            else:
                feil()
        elif guess == "4056":
            if chosen_word == "Rode Druer Losvekt":
                print"Svar = Rode Druer Losvekt, Riktig"
                print ""
            else:
                feil()
    elif ValueError:
        print ""
        print "Ma vere en PLU kode"
        print "Prov igjen"
        print ""
        continue
    
#End
