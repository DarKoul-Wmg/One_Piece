import random

dict_characters = {1: {"name": "Luffy", "category": 1, "weapons": [1, 1], "strength": 6, "speed":
    7, "experience": 0},
                   2: {"name": "Zoro", "category": 1, "weapons": [4], "strength": 5, "speed": 6, "experience":
                       0},
                   3: {"name": "Sanji", "category": 1, "weapons": [1, 3], "strength": 4, "speed":
                       6, "experience": 0},
                   4: {"name": "Buggy", "category": 2, "weapons": [3], "strength": 2, "speed": 4,
                       "experience": 0},
                   5: {"name": "Mr3", "category": 2, "weapons": [5], "strength": 3, "speed": 2, "experience"
                   : 0},
                   6: {"name": "Xebec", "category": 3, "weapons": [1, 3], "strength": 6, "speed": 5,
                       "experience": 0},
                   7: {"name": "Kaido", "category": 3, "weapons": [4], "strength": 8, "speed": 3,
                       "experience": 0},
                   8: {"name": "Mama grande", "category": 3, "weapons": [5], "strength": 7, "speed": 1,
                       "experience": 0},
                   9: {"name": "Akainu", "category": 4, "weapons": [2], "strength": 6, "speed": 4,
                       "experience": 0},
                   10: {"name": "Kizaru", "category": 4, "weapons": [1, 3], "strength": 5, "speed": 8,
                        "experience": 0},
                   11: {"name": "Fujitora", "category": 4, "weapons": [5], "strength": 5, "speed": 4,
                        "experience": 0},
                   12: {"name": "Garp", "category": 5, "weapons": [2], "strength": 6, "speed": 3,
                        "experience": 0},
                   13: {"name": "Smoker", "category": 5, "weapons": [5], "strength": 5, "speed": 5,
                        "experience": 0},
                   14: {"name": "Koby", "category": 6, "weapons": [4], "strength": 3, "speed": 4,
                        "experience": 0},
                   15: {"name": "Tashigi", "category": 6, "weapons": [3], "strength": 4, "speed": 4,
                        "experience": 0},
                   }

dict_weapons = {1: {"name": "Sword", "strength": 3, "speed": 5, "two_hand": False},
                2: {"name": "Greatsword", "strength": 5, "speed": 3, "two_hand": True},
                3: {"name": "Gun", "strength": 2, "speed": 6, "two_hand": False},
                4: {"name": "Rifle", "strength": 3, "speed": 4, "two_hand": True},
                5: {"name": "Chuchi", "strength": 4, "speed": 4, "two_hand": True},
                }

dict_crews = {1: {"name": "Straw hat", "members": [8, 6]},
              2: {"name": "Pirates Buggy", "members": [1, 3, 5]},
              3: {"name": "Pirates Rocks", "members": [2, 4, 7, ]}
              }

dict_ranks = {1: {"name": "Admiral", "members": [9, 10, 11]},
              2: {"name": "ViceAdmiral", "members": [12, 13]},
              3: {"name": "Lieutenant", "members": [14, 15]}
              }

dict_categorys = {1: "Straw hat", 2: "Pirates Buggy", 3: "PiratesRocks", 4: "Admiral", 5: "ViceAdmiral",
                  6: "Lieutenant"}

menu0 = "===========Menu 0 (One Peace)===========\n\n1)Play\n2)Create\n3)Edit\n4)List\n5)Exit"

menu02 = "=============Menu02 Create=============\n\n1)Create Character\n2)Create Weapon\n3)Go Back"

menu03 = "===Menu03 (Edit Menu)===\n\n1)Edit Character\n2)Edit Weapon\n3)Go Back"

menu031 = "\n1)Name\n2)Weapon\n3)Go Back"

menu032X = "===Menu 032X (Weapon Feature to Edit) ===\n\n1)Name\n1)Plus Strength\n3)Plus speed\n4)Go back"

menu04 = "============Menu04 (List)=============\n\n1)List Characters\n2)List Weapons\n3)List Side\n4)List Range\n5)Go Back"

menu041 = "======Menu041 (List Characters)======\n\n1)List by ID\n2)List by Name\n3)List by Strength\n4)List by Speed\n5)Go Back"

menu042 = "======Menu041 (List Characters)======\n\n1)List by ID\n2)List by Name\n3)List by Strength\n4)List by Speed\n5)Go Back"

cabecera_armas = 'Available Weapons'.center(40, '=') + '\n' + 'None'.center(40,
                                                                            '-') + '\n' + 'Character weapons:'.center(
    40, '=')

menu_ad_weapon = 'Add Weapons:\nid Weapon) To add Weapon id\n0)Finish add Weapons\n- Weapon Id ) Delete weapon id'

salir = False

flg_01 = False
flg_00 = True
flg_03 = False
flg_02 = False
flg_04 = False
flg_05 = False
flg_06 = False
print_armas = True

# VARIABLES MENU 2
creacionCharacter = False  # FLAG MENU CREAR PERSONAJE
creacionArmas = False  # FLAG MENU CREAR ARMA

seleccionArma = True
crearCharacter = True
saveCharacter = True
saveWeapon = True

while salir != True:
    ##menu principal(00)
    while flg_00:
        print(menu0)

        opc = input("->Options: " + "\n")
        # comprobar opciones menu correctas
        if not opc.isdigit():
            print("wrong option")
        elif not int(opc) in range(1, 6):
            print("wrong option")
        elif int(opc) == 1:
            flg_00 = True
            print('not implemented')

        elif int(opc) == 2:
            flg_06 = True
            flg_00 = False
            # para menu 2

        elif int(opc) == 3:
            flg_05 = True
            flg_00 = False
            # para menu03

        elif int(opc) == 4:
            flg_02 = True
            flg_00 = False
            # para menu04

    ############### menu2 ###############
    while flg_06:
        print(menu02)

        opc = input("->Options: " + "\n")
        # comprobar opciones menu correctas
        if not opc.isdigit():
            print("wrong option")
        elif not int(opc) in range(1, 4):
            print("wrong option")
        elif int(opc) == 3:
            flg_06 = False
            flg_00 = True
        else:
            if int(opc) == 1:
                creacionCharacter = True
                flg_06 = False

            elif int(opc) == 2:
                creacionArmas = True
                flg_06 = False

    while creacionCharacter:
        name = ""
        cat = 0
        id = len(dict_characters) + 1
        weapons = []
        strenght = 0
        speed = 0

        print("****** Menu 21 - Create Character**")
        if name == "" and cat == 0:

            name = input("Name of the new character:\n")
            while crearCharacter:
                print("SIde of the new character:\n" + "1)Marine\n" + "2)Pirates")
                opcion = input("Option >\n")
                if opcion.isdigit():
                    opcion = int(opcion)

                    if opcion == 1:

                        print(
                            "Range or crew of the new character:\n" + "1) Admirant\n" + "2) Viceadmirant\n" +
                            "3)Lieutenant\n")
                        opcion = input("Option >\n")

                        if opcion.isdigit():
                            opcion = int(opcion)

                            if opcion == 1:  # admirant
                                cat = 4
                                crearCharacter = False


                            elif opcion == 2:  # viceadmirant
                                cat = 5
                                crearCharacter = False


                            elif opcion == 3:  # Lieutenant
                                cat = 6
                                crearCharacter = False


                            else:
                                print("Opción no válida\n")
                        else:
                            print("opción no valida")


                    elif opcion == 2:

                        print(
                            "Range or crew of the new character:\n" + "1) Straw hat\n" + "2) Pirates Buggy\n" + "3) Pirates Rocks\n")
                        opcion = input("Option >\n")

                        if opcion.isdigit():
                            opcion = int(opcion)

                            if opcion == 1:
                                cat = 1
                                crearCharacter = False

                            elif opcion == 2:
                                cat = 2
                                crearCharacter = False

                            elif opcion == 3:
                                cat = 3
                                crearCharacter = False

                            else:
                                print("Opción no válida\n")
                        else:
                            print("Introduce una opcion numerica\n")
                    else:
                        print("Opción no válida\n")

                else:
                    print("Introduce una opcion numerica\n")

        while seleccionArma:
            cadenaAvalible = "=" * 10 + "Available Weapons" + "=" * 10 + "\n"
            cadenaInUse = "=" * 10 + "Character Weapons" + "=" * 10 + "\n"

            if len(weapons) == 0:  # MOSTRAR PRINT SIN ARMAS
                cadenaInUse += "\n" + "-" * 15 + " None " + "-" * 15 + "\n" * 4
                for weapon in range(len(dict_weapons)):
                    cadenaAvalible += str(weapon + 1) + ") name " + dict_weapons[weapon + 1][
                        "name"] + " Strength " + str(dict_weapons[weapon + 1]["strength"]) + \
                                      " Speed " + str(dict_weapons[weapon + 1]["speed"]) + "\n"

            if len(weapons) >= 1:  # MOSTRAR PRINT ARMAS
                if dict_weapons[weapons[0]]["two_hand"] == True or len(
                        weapons) == 2:  # COMPROBAR QUE ARMA TENGA 2 MANOS 0 QUE SEAN 2 DE UNA MANO
                    cadenaAvalible += "-" * 15 + " None " + "-" * 15 + "\n" * 4

                if dict_weapons[weapons[0]]["two_hand"] == False and len(
                        weapons) <= 1:  # SEGUNDA COMPROBACIÓN DE ARMA 2 MANOS
                    for weapon in range(len(dict_weapons)):
                        if dict_weapons[weapon + 1][
                            "two_hand"] == False:  # PASAR ARMAS 2 MANOS A FALSO APRA QUE NO SE MUESTREN
                            cadenaAvalible += str(weapon + 1) + ") name " + dict_weapons[weapon + 1][
                                "name"] + " Strength " + str(dict_weapons[weapon + 1]["strength"]) + \
                                              " Speed " + str(dict_weapons[weapon + 1]["speed"]) + "\n"

                for weapon in range(len(weapons)):  # MUESTRA ARMAS PERSONAJES
                    cadenaInUse += str(weapons[weapon]) + ") name " + dict_weapons[weapons[weapon]][
                        "name"] + " Strength " + str(dict_weapons[weapons[weapon]]["strength"]) + \
                                   " Speed " + str(dict_weapons[weapons[weapon]]["speed"]) + "\n"

            cabecera2 = "Add Weapons:\n" + "- Enter Id) to add Weapon\n" + "- Enter 0 to finish add weapons\n" + \
                        "- Enter  '-Id' to delete weapon in character"
            while True:

                print(cadenaAvalible)
                print(cadenaInUse)
                print(cabecera2)
                deleteWeapon = False
                opcion = input("Option >\n")
                if opcion.isspace() or opcion == "":  # EVITAR QUE PETE CON ENTER
                    print("Introduce una opcion numerica\n")
                elif opcion[0] == "-":  # ELIMINAR ARMA COMPROBANDO SI TIENE "-"
                    if opcion[1:].isdigit():  # Comprueba la id de arma conforme existe
                        opcion = int(opcion[1:])
                        deleteWeapon = True
                        if opcion in weapons:  # Salir del While
                            break
                    else:
                        print("Opción no válida.\n")
                elif opcion.isdigit():
                    opcion = int(opcion)
                    if opcion == 0:
                        seleccionArma = False
                        break
                    if opcion in range(len(dict_weapons) + 1):  # Comprueba la id de arma conforme existe

                        if len(weapons) == 0:
                            break
                        elif len(weapons) == 2 or dict_weapons[weapons[0]]["two_hand"] == True:
                            print("Ya tienes dos armas o un arma de dos manos\n")
                        elif len(weapons) >= 0:
                            if dict_weapons[opcion]["two_hand"] == False:
                                break

                    else:
                        print("Opción no válida.\n")
                else:
                    print("Introduce una opcion numerica\n")

            if deleteWeapon == True:
                if len(weapons) == 1:
                    weapons.remove(opcion)  # Eliminar un elemento
                else:
                    for i in range(len(weapons)):  # recorre weapons para eliminar arma
                        if opcion == weapons[i]:
                            weapons.remove(opcion)
                            break
            if opcion != 0 and deleteWeapon == False:
                weapons.append(opcion)

        strenght = random.randint(1, 9)
        speed = random.randint(1, 9)
        cadena = ""
        for key in weapons:  # MOSTRAR ARMAS PERSONAJE
            cadena += dict_weapons[key]["name"] + ", "
            cadena = cadena[: len(cadena) - 2]

        while saveCharacter:
            cabeceraPersonaje = "The new player will be:\n" + "\n" + f"Name: {name}\n" + f"Category: {dict_categorys[cat]}\n" + f"Weapons:{cadena}\n" + \
                                f"Strength:{strenght}\n" + f"Speed:{speed}\n" + f"Experience: 0\n"
            print(cabeceraPersonaje)
            save = input("Save this player? S/N")
            if save == "s" or save == "S":
                dict_characters[id] = {"name": name, "category": cat, "weapons": weapons, "strength": strenght,
                                       "speed": speed, "experience": 0}
                saveCharacter = False


            elif save == "n" or save == "N":
                saveCharacter = False

            else:
                print("Invalid option")
        flg_06 = True
        creacionCharacter = False
    while creacionArmas:
        id_weapon = len(dict_weapons) + 1

        print("****** Menu 22 - Create Weapon**")
        nameWeapon = input("Name of the new weapon:\n")
        print("Weapon strenght: 1-9 \n")
        strength = int(input("->Strenght: "))

        if not strength in range(10) or strength == 0:  # VALOR VALIDO
            print("==== Invalid Option ====")
            input("Press Enter to continue")
            strength = int(input("->Strenght: "))

        print("Weapon speed: 1-9 \n")
        speed = int(input("->Speed: "))

        if not speed in range(10) or speed == 0:
            print("==== Invalid Option ====\n")
            input("Press Enter to continue\n")
            speed = int(input("->Speed: "))

        print("\nKind of weapon\n1)One hand\n2)Two hand")  # TIPO DE ARMA
        opcion = input("Option >\n")
        if opcion.isdigit():
            opcion = int(opcion)
            if opcion == 1:
                two_hands = False

            elif opcion == 2:
                two_hands = True

            else:
                print("Opción no válida.\n")
        else:
            print("Opción no válida\n")

        while saveWeapon:
            cabeceraArma = f"Name: {nameWeapon}\n" + f"Strength:{strength}\n" + f"Speed:{speed}\n" + f"Two hands type: {two_hands}\n"
            print(cabeceraArma)

            save = input("Save this weapon? S/N\n")

            if save == "s" or save == "S":
                dict_weapons[id_weapon] = {"name": nameWeapon, "strength": strength, "speed": speed,
                                           f"two_hand": two_hands}
                saveWeapon = False

            elif save == "n" or save == "N":
                saveWeapon = False
        flg_06 = True
        creacionArmas = False
    ######################################menu04####################
    while flg_02:
        print(menu04)

        opc = input("->Options: " + "\n")
        # comprobar opciones menu correctas
        if not opc.isdigit():
            print("wrong option")
        elif not int(opc) in range(1, 7):
            print("wrong option")
        elif int(opc) == 1:
            flg_03 = True
            flg_02 = False
            # para menu041
        elif int(opc) == 2:
            flg_04 = True
            flg_02 = False
            # para menu042
        elif int(opc) == 5:
            flg_02 = False
            flg_00 = True
            # atras
    #############menu041####################
    while flg_03:
        print(menu041)

        opc = input("->Options: " + "\n")
        # comprobar opciones menu correctas
        if not opc.isdigit():
            print("wrong option")
        elif not int(opc) in range(1, 6):
            print("wrong option")

        elif int(opc) == 5:
            flg_03 = False
            flg_00 = True
            # atras
        elif int(opc) == 1:
            print()

    #############menu042####################
    while flg_04:
        print(menu042)

        opc = input("->Options: " + "\n")
        # comprobar opciones menu correctas
        if not opc.isdigit():
            print("wrong option")
        elif not int(opc) in range(1, 6):
            print("wrong option")
        elif int(opc) == 5:
            flg_04 = False
            flg_00 = True
            # atras
        #elif int(opc) == 1:
            #print()

    #####################menu03######################
    while flg_05:
        print(menu03)

        opc = input("->Options: " + "\n")
        # comprobar opciones menu correctas
        if not opc.isdigit():
            print("wrong option")
        elif not int(opc) in range(1, 5):
            print("wrong option")
        elif int(opc) == 3:
            flg_05 = False
            flg_00 = True
            # atras al menu 0

        elif int(opc) == 1:
            ####todo menu031
            print('===Menu 031 (Select Caracter to Edit) ===')
            lista = list(dict_characters.keys())
            # print (lista)
            for key in lista:
                for item in dict_characters[key]:
                    if item == "weapons":

                        cadena = ""
                        for weapon in dict_characters[key]["weapons"]:
                            cadena += dict_weapons[weapon]["name"] + ", "
                        cadena = cadena[: len(cadena) - 2]

                        print("ID: " + str(key) + " Name:" + dict_characters[key]["name"] + ", Category: " +
                              dict_categorys[dict_characters[key]["category"]] +
                              ", Weapons: " + cadena + " Strength:" + str(
                            dict_characters[key]["strength"]) + " Speed: " + str(
                            dict_characters[key]["speed"]) + " Experience: " + str(dict_characters[key]["experience"]))
            print()
            id_correcto = False

            while not id_correcto:
                id = input('ID to edit:' + '\n')
                if not id.isdigit():
                    print('==================Invalid Option==================3')
                    input('Pres enter to continue') + '\n'
                else:

                    # comprobacion de id
                    if not int(id) in dict_characters:
                        print('==================Invalid Option==================3')
                        input('Pres enter to continue') + '\n'

                    else:
                        id2 = int(id)

                        print('Select feature to edit to character ID:', int(id), ' Name: ',
                              dict_characters[id2]['name'])
                        id_correcto = True
                        print(menu031)
                        opc = input("->Options: " + "\n")
                        # comprobar opciones menu correctas
                        if not opc.isdigit():
                            print("wrong option")
                        elif not int(opc) in range(1, 4):
                            print("wrong option")
                            ############menu031

                        elif int(opc) == 3:
                            print()

                            # atras al menu 3
                        elif int(opc) == 1:
                            # ops1
                            new_name = input('Enter the new name: ')

                            s_n = str(input('Do you want to change name' + dict_characters[id2][
                                'name'] + 'by' + new_name + '? Press y/n' + '\n'))

                            if s_n == 'n':
                                flg_05 = False
                                flg_00 = True

                            elif s_n == 'y':
                                dict_characters[id2]['name'] = new_name
                                print(dict_characters[id2]['name'])
                                flg_05 = False
                                flg_00 = True

                        elif int(opc) == 2:
                            # ops 2 menu31
                            print_armas = False
                            while not print_armas:
                                if len(dict_characters[id2]['weapons']) == 2:

                                    print()

                                    print(cabecera_armas, '@')
                                    for i in range(len(dict_characters[id2]['weapons'])):
                                        print(dict_characters[id2]['weapons'][i], ')',
                                              dict_weapons[dict_characters[id2]['weapons'][i]]['name'], ',',
                                              'Strength: ',
                                              dict_weapons[dict_characters[id2]['weapons'][i]]['strength'], 'Speed: ',
                                              dict_weapons[dict_characters[id2]['weapons'][i]]['speed'])

                                    # print_armas = True
                                elif len(dict_characters[id2]['weapons']) == 1:
                                    if dict_characters[id2]['weapons'][0] == 1 or dict_characters[id2]['weapons'][
                                        0] == 3:

                                        print()

                                        print('===========Available Weapons============1')

                                        for clave in dict_weapons.keys():

                                            if dict_weapons[clave]['two_hand'] == False:
                                                print(clave, ')', dict_weapons[clave]['name'], ',', 'Strength: ',
                                                      dict_weapons[clave]['strength'],
                                                      'Speed: ', dict_weapons[clave]['speed'])
                                        print('===========Character weapons:===========2')
                                        for i in range(len(dict_characters[id2]['weapons'])):
                                            print(dict_characters[id2]['weapons'][i], ')',
                                                  dict_weapons[dict_characters[id2]['weapons'][i]]['name'], ',',
                                                  'Strength: ',
                                                  dict_weapons[dict_characters[id2]['weapons'][i]]['strength'],
                                                  'Speed: ',
                                                  dict_weapons[dict_characters[id2]['weapons'][i]]['speed'])
                                        # print_armas = True
                                        print()
                                    else:

                                        print()
                                        print('===========Available Weapons============3')
                                        print('------------------None------------------')
                                        print('===========Character weapons:===========')
                                        for i in range(len(dict_characters[id2]['weapons'])):
                                            print(dict_characters[id2]['weapons'][i], ')',
                                                  dict_weapons[dict_characters[id2]['weapons'][i]]['name'],
                                                  ',',
                                                  'Strength: ',
                                                  dict_weapons[dict_characters[id2]['weapons'][i]]['strength'],
                                                  'Speed: ',
                                                  dict_weapons[dict_characters[id2]['weapons'][i]]['speed'])
                                            # print_armas = True
                                        print()


                                else:

                                    print()

                                    print('===========Available Weapons============5')
                                    for clave in dict_weapons.keys():
                                        print(clave, ')', dict_weapons[clave]['name'], ',', 'Strength: ',
                                              dict_weapons[clave]['strength'],
                                              'Speed: ', dict_weapons[clave]['speed'])
                                    print('===========Character weapons:===========6')
                                    print()
                                    # print_armas = True

                                print()
                                print(menu_ad_weapon)
                                opcion = input("Option ->\n")

                                if opcion.isspace() or opcion == "":  # EVITAR QUE PETE CON ENTER
                                    print("Enter a numerical option\n")
                                elif opcion[0] == "-":  # ELIMINAR ARMA COMPROBANDO SI TIENE "-"
                                    if opcion[1:].isdigit():  # Comprueba que sea numerico
                                        opcion = int(opcion[1:])
                                        if opcion in dict_characters[id2]['weapons']:
                                            dict_characters[id2]['weapons'].index(opcion)
                                            if dict_characters[id2]['weapons'].index(opcion) == 0:
                                                dict_characters[id2]['weapons'] = dict_characters[id2]['weapons'][1:]

                                                dict_characters[id2]['strength'] = (dict_characters[id2]['strength']
                                                                                    - dict_weapons[opcion]['strength'])
                                                dict_characters[id2]['speed'] = (
                                                        dict_characters[id2]['speed'] - dict_weapons[opcion]['speed'])
                                                print('ok1')
                                            else:
                                                dict_characters[id2]['weapons'] = dict_characters[id2]['weapons'][:-1]

                                                dict_characters[id2]['strength'] = (dict_characters[id2]['strength']
                                                                                    - dict_weapons[opcion]['strength'])
                                                dict_characters[id2]['speed'] = (
                                                        dict_characters[id2]['speed'] - dict_weapons[opcion]['speed'])


                                        else:
                                            print('==================Invalid Option==================1')
                                            input('Press enter to continue')


                                    else:
                                        print('==================Invalid Option==================2')
                                        input('Press enter to continue')
                                elif opcion.isdigit():
                                    opcion = int(opcion)
                                    if int(opcion) == 0:

                                        print_armas = True


                                    elif opcion == 2 or opcion == 4 or opcion == 5:

                                        if len(dict_characters[id2]['weapons']) == 0:

                                            if opcion in dict_weapons:  # Comprueba la id de arma conforme existe
                                                dict_characters[id2]['weapons'].append(opcion)
                                                dict_characters[id2]['strength'] = (dict_characters[id2]['strength']
                                                                                    + dict_weapons[opcion]['strength'])
                                                dict_characters[id2]['speed'] = (
                                                        dict_characters[id2]['speed'] + dict_weapons[opcion]['speed'])

                                                edit_menu_fin = True

                                            else:
                                                print('==================Invalid Option==================1a')
                                                input('Press enter to continue')


                                        else:
                                            print('==================Invalid Option==================2a')
                                            input('Press enter to continue')

                                    elif opcion == 1 or opcion == 3:

                                        if len(dict_characters[id2]['weapons']) == 0 or len(
                                                dict_characters[id2]['weapons']) == 1:
                                            if opcion in dict_weapons:  # Comprueba la id de arma conforme existe
                                                dict_characters[id2]['weapons'].append(opcion)
                                                dict_characters[id2]['strength'] = (dict_characters[id2]['strength']
                                                                                    + dict_weapons[opcion]['strength'])
                                                dict_characters[id2]['speed'] = (
                                                        dict_characters[id2]['speed'] + dict_weapons[opcion]['speed'])



                                            else:
                                                print('==================Invalid Option==================1b')
                                                input('Press enter to continue')

                                    else:
                                        print('==================Invalid Option==================2b')
                                        input('Press enter to continue')

        elif int(opc) == 2:
            # menu32
            print('===Menu 032 (Select Weapon to Edit) ===')
            print()
            lista = list(dict_weapons.keys())
            for key in lista:
                print(key, ')', str(
                    dict_weapons[key]["name"]), ',', " Strength: " + str(
                    dict_weapons[key]["strength"]), ',', " Speed: " + str(
                    dict_weapons[key]["speed"]))
            print()

            id = input('ID weapon to edit: \n')

            print(menu032X, '\n')

            print('Select feature to edit to weapon ID: ', id, ', Name:', dict_weapons[int(id)]["name"])
            opc = input("->Options: " + "\n")
            if not opc.isdigit():
                print('==================Invalid Option==================')
                input('Press enter to continue')
            elif not int(opc) in range(1, 5):
                print('==================Invalid Option==================')
                input('Press enter to continue')
                ############menu031

            elif int(opc) == 4:
                print()

                # atras al menu 3
            elif int(opc) == 1:

                new_n_w = input('Enter the new name:\n')

                s_n = str(input('Do you want to change name' + dict_weapons[int(id)][
                    'name'] + 'by' + new_n_w + '? Press y/n' + '\n'))

                if s_n == 'n' or s_n == 'N':
                    print()



                elif s_n == 'y' or s_n == 'Y':
                    dict_weapons[int(id)][
                        'name'] = new_n_w
                    print(dict_weapons[int(id)])  ###se borra al final

            elif int(opc) == 2:
                #strength

                strength2 = input('Enter the new Strength:\n')

                if int(strength2) < 0 or int(strength2) > 9:
                    print('==================Invalid Option==================')
                    input('Press enter to continue')
                elif not strength2.isdigit():
                    print('==================Invalid Option==================')
                    input('Press enter to continue')

                else:

                    s_n = str(input('Do you want to change strength '+str(dict_weapons[int(id)][
                        'strength'])+' by '+ str(strength2) + '? Press y/n' + '\n'))



                    if s_n == 'n' or s_n == 'N':
                        print()



                    elif s_n == 'y' or s_n == 'Y':
                        #dict_weapons[int(id)]['strength'] = int(Strength2)



                        dict_weapons[int(id)]['strength'] = int(strength2)
                        print(dict_weapons[int(id)]['strength'])

                        print('+++@@@')



            elif int(opc) == 3:
                #speed

                speed2 = input('Enter the new Speed:\n')

                if int(speed2) < 0 or int(speed2) > 9:
                    print('==================Invalid Option==================')
                    input('Press enter to continue')
                elif not speed2.isdigit():
                    print('==================Invalid Option==================')
                    input('Press enter to continue')

                else:

                    s_n = str(input('Do you want to change speed '+str(dict_weapons[int(id)][
                        'speed'])+' by '+ str(speed2) + '? Press y/n' + '\n'))

                    if s_n == 'n' or s_n == 'N':
                        print()

                    elif s_n == 'y' or s_n == 'Y':

                        dict_weapons[int(id)]['speed'] = int(speed2)









