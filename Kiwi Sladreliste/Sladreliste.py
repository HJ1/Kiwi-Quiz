#Skrevet i Python 2.7 av HJ
print """Sladreliste 2017 Kiwi Tertnes - Laget av Hans Jorgen\n""" \
      """-- Versjon 1.0 September PLU koder i bruk pa Kiwi Tertnes -- \n"""

menu = True
while menu == True:
    print ("""1.Se alle PLU
2.Frukt & Gront
3.Ferske Bakevarer
4.Andre nyttige PLU
5.Exit/Quit""")
    
    choice=raw_input("Hva vil du gjore? ") 
    if choice=="1": 
      print ("""\nAlle PLU Versjon 1.0: \n""" \
             """\nFrukt & Gront PLU - Skrevet i alfabetisk rekkefolge: \n""" \
             """\nAgurk - 4316\nAnanas - 4430\nAppelsiner - 4196\nAsparges - 4090\nAubergine - 4081\nAvokado - 4222\nBakepoteter - 4367\nBanan - 4011\nBiff Tomat - 3061\nBlomkal - 4079\nBrokkoli - 4349\n""" \
             """Bringeber Kurv - 3081\nChampignon/Sjampinjong - 4645\nDadler - 3047\nDruer Gronne Losvekt - 4274\nEpler Gronn - 4139\nEpler Gule - 4021\nEpler Norske - 4204\nEpler Rode - 4015\n""" \
             """Fennikel - 4515\nFersken - 4038\nFirst Price Bananer - 4186\nGranateple - 4445\nGrapefrukt - 4281\nHodekal - 3050\nIngefer - 4612\nIsberg Salat - 4376\nJordber Kurv Import (Gjennomsiktig) - 3355\n""" \
             """Jordber Kurv Norske (Svart) - 4197\nKinakal i Pakke - 4355\nKiwi Stk - 4030\nKnutekal - 4628\nKlementiner - 4055\nKalrot - 4747\nLime Stk - 4048\nLok Losvekt - 4358\nMango - 4959\nMelon: Cantaloupe - 4049\n""" \
             """Melon: Honning - 4317\nMelon: Piel de Sapo - 3101\nMelon: Vannmelon Delt - 4031\nMelon: Vannmelon Hel - 4032\nNektarin - 4036\nNektarin Kurv - 4276\nNeper Bunt - 4810\nNypoteter Losvekt - 4073\n""" \
             """Paprika First Price 2pk - 4360\nPaprika Gronn - 4065\nPaprika Rod - 4088\nPaprika Sotspisset 2pk - 4702\nPaprika Trafikklys - 4362\nPastinakk - 4363\nPersillerot - 4671\nPerer - 3017\nPlommer Norske - 4405\n""" \
             """Plommer Rode/Bla - 4041\nRettich - 4740\nRodbeter Bunt 3pk - 4539\nSellerirot - 4390\nSitron - 4033\nSquash - 4067\nStangselleri - 4380\nSotpotet - 4091\nTomater - 4064\nOkologiske Bananer - 94011\nOkologiske Blomkal - 94079\nOkologiske Brokkoli - 94349\n-----\n""" \
            
             """\nFerske Bakevarer PLU - Skrevet i alfabetisk rekkefolge: \n""" \
             """Legg merke til at vi bruker Sommerbolle - 2013, Solskinnsbolle -\n""" \
             """2042 selges ikke lenger.\n""" \
             """\nCroissant - 2854\nEnergistykke - 2651\nGresskarstykke Grov - 2088\nHavrebrix - 9060\nKanelknute - 2047\nKornbaguette - 2009\nLunsjhjul - 2502\nMinipizza - 6085\nOstebaguette - 2297\nOstehorn - 6882\n""" \
             """Rundstykke Fint - 2084\nRundstykke Grov/Kneip - 2085\nSkillingsbolle - 2039\nSkolebrod - 2040\nSolsikkestykke - 2007\nSommerbolle - 2013\nTebrix - 9063\nTvist Grov Piripiri - 2008\nWienerbrod - 2048\n-----\n"""

            """\nAndre nyttige PLU - Skrevet i alfabetisk rekkefolge: \n""" \
            """\nCoca Cola 4pk - 9534\nCola Zero 4pk - 9535\nCola Zero 1.25L 6pk - 9995\nFarin/Sukker 10kg - 9050\nFyrstikkeske 1x - 9010\nGrillkull 2.5kg - 9935\nHvetemel 4x2kg - 9997\n""" \
            """Kiwi Pluss - 1100\nMypack Betaling i Kasse - 9980\nMandler Losvekt - 4924\nNotter Losvekt - 9018\nPant Kasse - 9011\nPepsi Max 4pk - 5670\nPepsi Max 8pk - 9045\nReker - 1900""" \
            """\nReker 5kg 90/130 Stor Eske - 1895\nSmagodt - 9009\nSmagodt i Beger - 509\n-----\n""")
    elif choice == "2":
        print("""\nFrukt & Gront PLU - Skrevet i alfabetisk rekkefolge: \n""" \
              """\nAgurk - 4316\nAnanas - 4430\nAppelsiner - 4196\nAsparges - 4090\nAubergine - 4081\nAvokado - 4222\nBakepoteter - 4367\nBanan - 4011\nBiff Tomat - 3061\nBlomkal - 4079\nBrokkoli - 4349\n""" \
              """Bringeber Kurv - 3081\nChampignon/Sjampinjong - 4645\nDadler - 3047\nDruer Gronne Losvekt - 4274\nEpler Gronn - 4139\nEpler Gule - 4021\nEpler Norske - 4204\nEpler Rode - 4015\n""" \
              """Fennikel - 4515\nFersken - 4038\nFirst Price Bananer - 4186\nGranateple - 4445\nGrapefrukt - 4281\nHodekal - 3050\nIngefer - 4612\nIsberg Salat - 4376\nJordber Kurv Import (Gjennomsiktig) - 3355\n""" \
              """Jordber Kurv Norske (Svart) - 4197\nKinakal i Pakke - 4355\nKiwi Stk - 4030\nKnutekal - 4628\nKlementiner - 4055\nKalrot - 4747\nLime Stk - 4048\nLok Losvekt - 4358\nMango - 4959\nMelon: Cantaloupe - 4049\n""" \
              """Melon: Honning - 4317\nMelon: Piel de Sapo - 3101\nMelon: Vannmelon Delt - 4031\nMelon: Vannmelon Hel - 4032\nNektarin - 4036\nNektarin Kurv - 4276\nNeper Bunt - 4810\nNypoteter Losvekt - 4073\n""" \
              """Paprika First Price 2pk - 4360\nPaprika Gronn - 4065\nPaprika Rod - 4088\nPaprika Sotspisset 2pk - 4702\nPaprika Trafikklys - 4362\nPastinakk - 4363\nPersillerot - 4671\nPerer - 3017\nPlommer Norske - 4405\n""" \
              """Plommer Rode/Bla - 4041\nRettich - 4740\nRodbeter Bunt 3pk - 4539\nSellerirot - 4390\nSitron - 4033\nSquash - 4067\nStangselleri - 4380\nSotpotet - 4091\nTomater - 4064\nOkologiske Bananer - 94011\nOkologiske Blomkal - 94079\nOkologiske Brokkoli - 94349\n--\n""")
    elif choice=="3":
      print("""\nFerske Bakevarer PLU - Skrevet i alfabetisk rekkefolge: \n""" \
            """Legg merke til at vi bruker Sommerbolle - 2013, Solskinnsbolle -\n""" \
            """2042 selges ikke lenger.\n""" \
            """\nCroissant - 2854\nEnergistykke - 2651\nGresskarstykke Grov - 2088\nHavrebrix - 9060\nKanelknute - 2047\nKornbaguette - 2009\nLunsjhjul - 2502\nMinipizza - 6085\nOstebaguette - 2297\nOstehorn - 6882\n""" \
            """Rundstykke Fint - 2084\nRundstykke Grov/Kneip - 2085\nSkillingsbolle - 2039\nSkolebrod - 2040\nSolsikkestykke - 2007\nSommerbolle - 2013\nTebrix - 9063\nTvist Grov Piripiri - 2008\nWienerbrod - 2048\n--\n""")
    elif choice=="4":
      print("""\nAndre nyttige PLU - Skrevet i alfabetisk rekkefolge: \n""" \
            """\nCoca Cola 4pk - 9534\nCola Zero 4pk - 9535\nCola Zero 1.25L 6pk - 9995\nFarin/Sukker 10kg - 9050\nFyrstikkeske 1x - 9010\nGrillkull 2.5kg - 9935\nHvetemel 4x2kg - 9997\n""" \
            """Kiwi Pluss - 1100\nMypack Betaling i Kasse - 9980\nMandler Losvekt - 4924\nNotter Losvekt - 9018\nPant Kasse - 9011\nPepsi Max 4pk - 5670\nPepsi Max 8pk - 9045\nReker - 1900""" \
            """\nReker 5kg 90/130 Stor Eske - 1895\nSmagodt - 9009\nSmagodt i Beger - 509\n--\n""")
    elif choice=="5":
      print("\n" "Hade bra :)")
      raw_input("press any key...")
      break
    elif choice !="":
      print("\n" "Ikke et gyldig valg, prov igjen" "\n") 

