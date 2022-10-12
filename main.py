documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def name_output(num):
    for doc in documents:
        if num == doc['number']:
            print(doc['name'])
            return doc['name']
    print('Такого документа не существует')


def shelf_number_output(num_1):
    for key, value in directories.items():
        if num_1 in value:
            print(f'Документ находится на полке {key}')
            return key
    print('Такого документа не существует')


def all_documents():
    for doc in documents:
        docs = f'{doc["type"]} "{doc["number"]}" "{doc["name"]}"'
        print(docs)
    return documents


def add_new_document(doc_number, doc_type, doc_name, shelf):
    new_doc = {}
    new_doc['number'] = doc_number
    new_doc['type'] = doc_type
    new_doc['name'] = doc_name
    shelf_number = shelf
    if shelf_number in directories:
        directories[shelf_number].append(new_doc['number'])
        documents.append(new_doc)
        result = f"{new_doc['type']} {new_doc['name']} добавлен на полку {shelf_number}"
        print(result)
        return True
    else:
        print('Нет полки с таким номером')
        return False


def delete_document(doc_num_1):
    doc_number_1 = doc_num_1
    for key, value in directories.items():
        if doc_number_1 in value:
            value.remove(doc_number_1)
    for doc in documents:
        if doc_number_1 in doc['number']:
            documents.remove(doc)
            print(f'Документ {doc_number_1} удален')
            return True
    print('Такого документа не существует')


def move_document(doc_num_2, shelf_2):
    doc_number_2 = doc_num_2
    shelf_number_2 = shelf_2
    if shelf_number_2 not in directories:
        print('Нет полки с таким номером')
        return False
    for key, value in directories.items():
        if doc_number_2 in value:
            directories[shelf_number_2] += [doc_number_2]
            value.remove(doc_number_2)
            print(f'Документ {doc_number_2} перемещен на полку {shelf_number_2}')
            return True
    print("Документ не найден")
    return False


def add_shelf(shelf_3):
    shelf_number_3 = shelf_3
    for key, value in directories.items():
        if shelf_number_3 in key:
            print('Полка с наким номером уже существует')
            return False
    directories.setdefault(shelf_number_3, [])
    print(f'Полка {shelf_number_3} добавлена')
    return True


def enter():
    print('Список доступных команд:\n'
          'p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;\n'
          's – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;\n'
          'l – list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";\n'
          'a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться;\n'
          'd – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок;\n'
          'm – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую;\n'
          'as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень;\n'
          'q - quit - выход.')
    while True:
        command = input('Введите команду: ')
        if command == 'p':
            num = input('Введите номер документа: ')
            name_output(num)
        elif command == 's':
            num_1 = input('Введите номер документа: ')
            shelf_number_output(num_1)
        elif command == 'l':
            all_documents()
        elif command == 'a':
            doc_number = input('Введите номер документа: ')
            doc_type = input('Введите тип документа: ')
            doc_name = input('Введите имя: ')
            shelf = input('Введите номер полки: ')
            add_new_document(doc_number, doc_type, doc_name, shelf)
        elif command == 'd':
            doc_num_1 = input('Введите номер документа: ')
            delete_document(doc_num_1)
        elif command == 'm':
            doc_num_2 = input('Введите номер документа: ')
            shelf_2 = input('Введите номер полки: ')
            move_document(doc_num_2, shelf_2)
        elif command == 'as':
            shelf_3 = input('Введите номер полки: ')
            add_shelf(shelf_3)
        elif command == 'q':
            print('Выход')
            break


if __name__ == '__main__':
    enter()
