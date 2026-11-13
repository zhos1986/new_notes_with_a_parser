from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QPushButton, QLabel, QListWidget, QLineEdit, QTextEdit, QHBoxLayout, QVBoxLayout






app = QApplication([])

notes = []
note = []


def add_note(): #добавляет заметку
    note_name, ok = QInputDialog.getText(notes_win, 'Добавить заметку', 'Название заметки')
    if ok and note_name != '':
        note = list()
        note = [note_name, '', []]
        notes.append(note)
        list_notes.addItem(note[0])
        filename = str(len(notes)-1)+".txt"
        with open(filename, 'w') as file:
            file.write(note[0]+'\n')
            file.write('\n')
            file.write(' \n')


def show_note(): #показывает выбранную заметку:)
    if list_notes.selectedItems():
        name = list_notes.selectedItems()[0].text()
        for note in notes:
            if note[0] == name:
                field_text.setText(note[1])
                list_tags.clear()
                list_tags.addItems(note[2])
                break



def save_note(): #сохраняет заметку(/_')
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        i = 0
        for note in notes:
            if note[0] == key:
                note[1] = field_text.toPlainText()
                filename = str(i)+'.txt'
                with open(filename, 'w') as file:
                    file.write(note[0]+'\n')
                    file.write(note[1]+'\n')
                    for tag in note[2]:
                        file.write(tag+' ')
                    file.write('\n')
            i += 1

def del_note(): # удаляет выбранную заметку(;
    if list_notes.selectedItems():
        pass


def add_tag(): #добавляет тег к заметке'_'
    pass


def del_tag(): #убирает выбранный тег у заметке(!_!)
    pass


def search_tag(): # ищет заметки по тегу (возвращает весь список)))("...")
    pass


'''Интерфейс приложения'''
#параметры окна приложения
notes_win = QWidget()
notes_win.setWindowTitle('Умные заметки')
notes_win.resize(1100, 800)


#виджеты окна приложения
list_notes = QListWidget()
list_notes_label = QLabel('Список заметок')


#появляется окно с полем "Введите имя заметки"
button_note_create = QPushButton('Создать заметку')
button_note_del = QPushButton('Удалить заметку')
button_note_save = QPushButton('Сохранить заметку')


field_tag = QLineEdit('')
field_tag.setPlaceholderText('Введите тег...')
field_text = QTextEdit()
button_tag_add = QPushButton('Добавить к заметке')
button_tag_del = QPushButton('Открепить от заметки')
button_tag_search = QPushButton('Искать заметки по тегу')
list_tags = QListWidget()
list_tags_label = QLabel('Список тегов')
    #расположение виджетов по лэйаутам
layout_notes = QHBoxLayout()
col_1 = QVBoxLayout()
col_1.addWidget(field_text)


col_2 = QVBoxLayout()
col_2.addWidget(list_notes_label)
col_2.addWidget(list_notes)
row_1 = QHBoxLayout()
row_1.addWidget(button_note_create)
row_1.addWidget(button_note_del)
row_2 = QHBoxLayout()
row_2.addWidget(button_note_save)
col_2.addLayout(row_1)
col_2.addLayout(row_2)


col_2.addWidget(list_tags_label)
col_2.addWidget(list_tags)
col_2.addWidget(field_tag)
row_3 = QHBoxLayout()
row_3.addWidget(button_tag_add)
row_3.addWidget(button_tag_del)
row_4 = QHBoxLayout()
row_4.addWidget(button_tag_search)


col_2.addLayout(row_3)
col_2.addLayout(row_4)


layout_notes.addLayout(col_1, stretch = 2)
layout_notes.addLayout(col_2, stretch = 1)
notes_win.setLayout(layout_notes)
#запуск приложения

notes = []
num_name = 0
while True:
    filename = str(num_name) + '.txt'
    try:
        with open(filename, 'r', encoding = 'utf-8') as file:
            note = []
            for line in file:
                note.append(line.replace('\n', ''))
            print(note)
            note[2] = note[2].split()
            notes.append(note)
            num_name += 1
    except IOError:
        break
for note in notes:
    list_notes.addItem(note[0])

print(notes)


list_notes.itemClicked.connect(show_note)
button_note_create.clicked.connect(add_note)
button_note_del.clicked.connect(del_note)
button_tag_add.clicked.connect(add_tag)
button_tag_del.clicked.connect(del_tag)
button_tag_search.clicked.connect(search_tag)
button_note_save.clicked.connect(save_note)

notes_win.show()
app.exec_()