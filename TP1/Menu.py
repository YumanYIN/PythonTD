

if __name__ == "__main__":
    fileName = ""

    while True:
        print("1. Choisir un nom de fichier, \n"
              "2. Ajouter un texte, \n"
              "3. Afficher le fichier complet, \n"
              "4. Vider le fichier, \n"
              "9. Quitter le programme.\n")
        choice = input("please input your choice: ")
        if choice not in ['1', '2', '3', '4', '9']:
            print("Please input correct number!\n")
            continue
        elif choice == '1':
            fileName = showAllFiles()

        elif choice == '2':
            chooseFile(fileName)

        elif choice == '3':
            showFile(fileName)

        elif choice == '4':
            cleanFile(fileName)

        else:
            c = input("are you sure to exit the program? y(es) n(o)")
            if c not in ['y', 'n', 'Y', 'N']:
                print("your input is incorrect, please do that again\n")
                continue
            elif c in ['y', 'Y']:
                print("bye~")
                break
            else:
                continue
