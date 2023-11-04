from functions import*

def interface():
    with open("phonebook.txt","a",encoding="utf-8"):
        pass
    
    command=""
    os.system("cls")
    while command!="4":
        print("Меню пользователя:\n"
            "1. Вывод данных на экран\n"
            "2. Добавить контакт\n"
            "3. Поиск контакта\n"
            "4. Выход\n")
        
        command=input("Выберите пункт меню: ")
        
        while command not in ("1","2","3","4"):
            print("Некорректный ввод, повторите запрос")
            command=input("Выберите пункт меню: ")
            
        match command:
            case "1":
                print_data()
            case "2":
                add_contact()
            case "3":
                search_contact()
            case "4":
                print("Завершение программы")
                