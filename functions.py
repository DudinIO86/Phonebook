import os

from input_data import*

def print_data():
    with open("phonebook.txt","r",encoding="utf-8") as file:
        phonebook_str=file.read()
    print(phonebook_str)
    print()
    
def add_contact():
    new_contact_str=input_data()
    with open("phonebook.txt","a",encoding="utf-8") as file:
        file.write(new_contact_str)

def search_contact():
    print("Варианты поиска:\n"
        "1. По фамилии\n"
        "2. По имени\n"
        "3. По отчеству\n"
        "4. По телефону\n"
        "5. По адресу\n")
    
    command=input("Выберите вариант поиска: ")
    
    while command not in ("1","2","3","4","5"):
        print("Некорректный ввод, повторите запрос")
        command=input("Выберите вариант поиска: ")
    
    i_search=int(command)-1      
    search=input("Введите данные для поиска: ").lower()
    print()
    
    with open("phonebook.txt","r",encoding="utf-8") as file:
        contacts_list=file.read().rstrip().split("\n\n")
    
    check_cont=False
    
    for contact_str in contacts_list:
        lst_contact=contact_str.lower().replace("\n"," ").split()
      
        if search in lst_contact[i_search]:
            print(contact_str)
            print()
            check_cont=True
            
    if not check_cont:
        print("Такого контакта нет.")