list_film = []

while True:
    print("\nMenu:")
    print("1. Adicionar filme")
    print("2. Remover filme")
    print("3. Modificar nome da filme")
    print("4. Ver lista")
    print("5. SAIR")


    option = input("Escolha uma opção:")

    if option == "1":
        film = input("Digite o filme que deseja inserir:")
        list_film.append(film)
    elif option == "2":
        delete_film = input("Digite o filme que deseja apagar:")
        if delete_film in list_film:
            list_film.remove(delete_film)
        else:
            print ("O filme não foi encontrado")
    elif option == "3":
        indice = int(input ("Digite o indice do filme que deseja modificar:'Indice inicia do 0'"))
        if 0 <= indice < len(list_film):
            new_film = input("Digite o novo filme que deseja inserir:")
            list_film[indice] = new_film
        else:
            print("Não foi encontrado o indice")
    elif option == "4":
        print("\n lista de filmes: ",list_film)
    elif option == "5":
        break
