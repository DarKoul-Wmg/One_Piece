# One_Piece
Proyecto de diccionarios pre examen UF1

dict_characters = { 1 : {"name" : "Luffy","category": 1, "weapons": [1, 1],"strength" : 6, "speed" :
7,"experience": 0},
 2 : {"name" : "Zoro","category": 1, "weapons" : [4],"strength" : 5, "speed" : 6,"experience":
0},
 3 : {"name" : "Sanji", "category" : 1, "weapons" : [1,3],"strength" : 4, "speed" :
6,"experience": 0 },
 4 : {"name" : "Buggy", "category" : 2, "weapons" : [3], "strength" : 2, "speed" : 4,
"experience" : 0},
 5 : {"name" : "Mr3", "category" : 2, "weapons" : [5], "strength" : 3, "speed" : 2, "experience"
: 0},
 6 : {"name" : "Xebec", "category" : 3, "weapons" : [1,3], "strength" : 6, "speed" : 5,
"experience" : 0},
 7 : {"name" : "Kaido", "category" : 3, "weapons" : [4], "strength" : 8, "speed" : 3,
"experience" : 0},
 8 : {"name" : "Mama grande", "category" : 3, "weapons" : [5], "strength" : 7, "speed" : 1,
"experience" : 0},
 9 : {"name" : "Akainu", "category" : 4, "weapons" : [2], "strength" : 6, "speed" : 4,
"experience" : 0},
 10 : {"name" : "Kizaru", "category" : 4, "weapons" : [1,3], "strength" : 5, "speed" : 8,
"experience" : 0},
 11 : {"name" : "Fujitora", "category" : 4, "weapons" : [5], "strength" : 5, "speed" : 4,
"experience" : 0},
 12 : {"name" : "Garp", "category" : 5, "weapons" : [2], "strength" : 6, "speed" : 3,
"experience" : 0},
 13 : {"name" : "Smoker", "category" : 5, "weapons" : [5], "strength" : 5, "speed" : 5,
"experience" : 0},
 14 : {"name" : "Koby", "category" : 6, "weapons" : [4], "strength" : 3, "speed" : 4,
"experience" : 0},
 15 : {"name" : "Tashigi", "category" : 6, "weapons" : [3], "strength" : 4, "speed" : 4,
"experience" : 0},
 }

dict_weapons = { 1 : {"name" : "Sword","strength": 3,"speed": 5,"two_hand":False},
 2 : {"name" : "Greatsword","strength": 5,"speed": 3,"two_hand":True},
 3 : {"name" : "Gun","strength": 2,"speed": 6,"two_hand":False},
 4: {"name": "Rifle", "strength": 3, "speed": 4,"two_hand":True},
 5: {"name": "Chuchi", "strength": 4, "speed": 4,"two_hand":True},
 }

dict_crews = { 1 : {"name" : "Straw hat","members": [8,6]},
 2 : {"name" : "Pirates Buggy","members": [1,3,5]},
 3: {"name": "Pirates Rocks","members": [2,4,7,]}
 }

dict_ranks = { 1 : {"name" : "Admiral","members": [9,10,11]},
 2 : {"name" : "ViceAdmiral","members": [12,13]},
 3: {"name": "Lieutenant","members": [14,15]}
 }

dict_categorys = {1:"Straw hat",2:"Pirates Buggy",3:"PiratesRocks",4:"Admiral",5:"ViceAdmiral",6:"Lieutenant"}


menu0 ="===========Menu 0 (One Peace)===========\n\n1)Play\n2)Create\n3)Edit\n4)List\n5)Exit"

menu03 ="===Menu03 (Edit Menu)===\n\n1)Edit Character\n2)Edit Weapon\n3)Go Back"

menu031 ="\n1)Name\n2)Weapon\n3)Go Back"

menu04 ="============Menu04 (List)=============\n\n1)List Characters\n2)List Weapons\n3)List Side\n4)List Range\n5)Go Back"

menu041 ="======Menu041 (List Characters)======\n\n1)List by ID\n2)List by Name\n3)List by Strength\n4)List by Speed\n5)Go Back"

menu042 ="======Menu041 (List Characters)======\n\n1)List by ID\n2)List by Name\n3)List by Strength\n4)List by Speed\n5)Go Back"

cabecera_armas = 'Available Weapons'.center(40,'=') + '\n' + 'None'.center(40,'-') + '\n'+ 'Character weapons:'.center(40,'=')



salir = False
flg_01 = False
flg_00 = True
flg_03 = False
flg_02 = False
flg_04 = False
flg_05 = False






while salir != True:
    ##menu principal(00)
    while flg_00:
        print(menu0)

        opc = input("->Options: " + "\n")
        #comprobar opciones menu correctas
        if not opc.isdigit():
            print("wrong option")
        elif not int(opc) in range(1, 6):
            print("wrong option")
        elif int(opc) == 1:
            flg_00 = True
            print('not implemented')
        elif int(opc) == 3:
            flg_05 = True
            flg_00 = False
            #para menu03
        elif int(opc) == 4:
            flg_02 = True
            flg_00 = False
            # para menu04

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
            #para menu041
        elif int(opc) == 2:
            flg_04 = True
            flg_02 = False
            # para menu042
        elif int(opc) == 5:
            flg_02 = False
            flg_00 = True
            #atras
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
            #atras
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
            #atras
        elif int(opc) == 1:
            print()

    #####################menu03######################
    while flg_05:
        print(menu03)

        opc = input("->Options: " + "\n")
        # comprobar opciones menu correctas
        if not opc.isdigit():
            print("wrong option")
        elif not int(opc) in range(1, 4):
            print("wrong option")
        elif int(opc) == 3:
            flg_05 = False
            flg_00 = True

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

                        print("ID: " + str(key) + " Name " + dict_characters[key]["name"] + ", Category: " +
                              dict_categorys[dict_characters[key]["category"]] +
                              ", Weapons: " + cadena + " Strength ," + str(
                            dict_characters[key]["strength"]) + " Speed " + str(
                            dict_characters[key]["speed"]) + " Exp " + str(dict_characters[key]["experience"]))
            print()
            id_correcto = False

            while not id_correcto:
                id = input('ID to edit:'+'\n')
                if not  id.isdigit():
                    print('==================Invalid Option==================3')
                    input('Pres enter to continue') + '\n'
                else:

                    #comprobacion de id
                    if not int(id) in dict_characters:
                        print('==================Invalid Option==================3')
                        input('Pres enter to continue')+'\n'

                    else:
                        id2 = int(id)

                        print('Select feature to edit to character ID:',int(id),' Name: ', dict_characters[id2]['name'])
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
                            flg_05 = False
                            flg_00 = True
                            #atras
                        elif int(opc) == 1:
                            new_name = input('Enter the new name: ')

                            s_n = str(input('Do you want to change name'+ dict_characters[id2]['name'] + 'by'+ new_name +'? Press y/n'+'\n'))

                            if s_n == 'n':
                                flg_05 = False
                                flg_00 = True

                            elif s_n == 'y':
                                dict_characters[id2]['name'] = new_name
                                print(dict_characters[id2]['name'])
                                flg_05 = False
                                flg_00 = True

                        elif int(opc) == 2:
                            print('rangelist =  ')####hay que poner el rango justo despues de la ' pero ahora no se que es.
                            print()
                            print(cabecera_armas)

                            for item in dict_characters[id2]:
                                if item == "weapons":

                                    cadena = ""
                                    for weapon in dict_characters[id2]["weapons"]:
                                        print(dict_weapons[weapon]["name"],
                                              " Strength: " + str(dict_weapons[weapon]["strength"]) + ", Speed " + str(
                                                  dict_weapons[weapon]["speed"]))
                                    print()

#################3editar menu de cambio de arma






