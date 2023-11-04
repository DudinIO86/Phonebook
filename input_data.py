def input_name():
    return input("Введите имя контакта: ").title()

def input_surname():
    return input("Введите фамилию контакта: ").title()

def input_patronymic():
    return input("Введите отчество контакта: ").title()
    
def input_phone():
    return input("Введите номер телефона контакта: ").title()

def input_address():
    return input("Введите адрес контакта: ").title()

def input_data():
    surname=input_surname()
    name=input_name()
    patronymic=input_patronymic()
    phone=input_phone()
    address=input_address()
    my_sep=" "
    return f"{surname}{my_sep}{name}{my_sep}{patronymic}{my_sep}{phone}\n{address}\n\n"