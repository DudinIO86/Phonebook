import os

from input_data import*

def print_data():
    with open("Phonebook/phonebook.txt","r",encoding="utf-8") as file:
        phonebook_str=file.read()
       
    print(phonebook_str)
    print()
    
def add_contact():
    new_contact_str=input_data()
    with open("Phonebook/phonebook.txt","a",encoding="utf-8") as file:
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
    
    with open("Phonebook/phonebook.txt","r",encoding="utf-8") as file:
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
        
def copy_contacts():
    with open("Phonebook/phonebook.txt","r",encoding="utf-8") as file:
        phonebook_str=file.read().rstrip().split("\n\n")
        phonebook_str2=list(enumerate((phonebook_str),1))
        
        for i in range(len(phonebook_str)):
            s1=phonebook_str2[i][0]
            s2=phonebook_str2[i][1]
            print(str(s1)+". "+s2)
        
        bool_index=False
        
        while bool_index!=True:
            
            choice=input("Какой номер записи скопировать: ")
            
            if int(choice)>0 and int(choice)<=len(phonebook_str):        
                copy_contact_str=phonebook_str[int(choice)-1]
                with open("Phonebook/phonebook_choice.txt","a",encoding="utf-8") as file:
                    file.write(copy_contact_str)
                    file.write("\n\n")
                    bool_index=True
                    print("Запись скопирована")
            else:
                print("Такой позиции нет. Повторите ввод")