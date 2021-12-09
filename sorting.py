"""
изначальный набор комманд по ТЗ:
1 загрузить список в панель
2 отсортировать список пузырьком
3 отсортировать список выбором
4 отсортировать список вставками
5 вывести полученый список в панель
0 выход
"""

"""TODO pep 257; 
расширить загрузку файла, чтоб можно было подавать списки и через пробел;
добавить функцию сохранения вывода; 
оформить загрузку и выгрузку в поле в меню;подготовить презентацию"""

from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename

from mysorts import bubble_sort, selection_sort, insertion_sort


lst = []        # Глобальный спискок


def  my_sort(lst):
    if lst:
        if sort_type.get() == 'bubble':

            bubble_sort(lst)
            debug_display_var.set("список отсортирован пузырьком")
            
        elif sort_type.get() == 'selection':
            
            selection_sort(lst)
            debug_display_var.set("список отсортирован выбором")

        elif sort_type.get() == 'insertion':
            
            insertion_sort(lst)
            debug_display_var.set("список отсортирован вставками")
    else:
        debug_display_var.set('список пуст')


def load_lst(*args):
    
    filename = askopenfilename()
    file = open(filename,'r')
    
    global lst
    lst = []

    try:
        for line in file:
            lst.extend(list(map(int, line.split(","))))
    except ValueError:
        debug_display_var.set("нечитаемый файл")
    else:
        debug_display_var.set("список загружен")
    file.close()


def update_display(*args):
    if lst:
        if not print_limited_state.get() or len(lst)<=20:
            main_display_var.set(", ".join(map(str,lst)))
        else:
            main_display_var.set(", ".join(map(str,lst[:20]))+"...")
    else:
        debug_display_var.set("список пуст")



# Определяем элементы окна

# Основное окно
root = Tk()
root.title("Сортировка числовых списков")
# Основная рамка, в которой находятся все элементы
mainframe = ttk.Frame(root, padding=12,)

# Малый дисплей, выводящий доп информацию
debug_display_var = StringVar()
debug_display_var.set("загрузите список")
debug_display = ttk.Label(
    mainframe, textvariable=debug_display_var, wraplength=200)

# Кнопка загрузки списка из файла TODO переделать в меню
load_button = ttk.Button(
    mainframe, text='загрузить список из файла', command=load_lst)

# Главный дисплей, отвечающий за вывод списка
main_display_var = StringVar()#переменная дисплея
main_display_var.set("")
#wraplength указан константой, что не очень хорошо
#но я без понятия, как сделать его по требуемой минимальной ширине
main_display = ttk.Label(
    mainframe, textvariable=main_display_var, 
    borderwidth=8, relief='ridge', wraplength=340, 
    justify='center',anchor='center')

# Обработка печати на дисплей
# Галочка, отвечающая за длинну выводимого списка
print_limited_state = BooleanVar(value=False)
print_limited_check = ttk.Checkbutton(
    mainframe, text="напечатать только первые 20 эмелентов",
    variable=print_limited_state)
# Кнопка печати на главный дисплей
print_button = ttk.Button(
    mainframe, text='напечатать список', command=update_display)

# Выбор и запуск сортировки списка
# Выбор сотрировки
sort_type = StringVar(value='bubble')
sort_radio_bubble = ttk.Radiobutton(mainframe, 
    text="сортировка пузырьком", variable=sort_type, value='bubble' )
sort_radio_selection = ttk.Radiobutton(mainframe, 
    text="сортировка выбором", variable=sort_type, value='selection' )
sort_radio_insertion = ttk.Radiobutton(mainframe, 
    text="сортировка вставками", variable=sort_type, value='insertion' )
# Кнопка сортировки
sort_button = ttk.Button(mainframe, 
    text="отсортировать", command=lambda: my_sort(lst))

# Кнопка выхода
exit_button = ttk.Button(mainframe, 
    text="выход", command=lambda: root.destroy())


# Расставляем элементы

# Основная рамка на всё окно
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

# Дебаг-дисплей слева сверху
debug_display.grid(column=0, row=0)
# Кнопка загрузки сверху справа TODO переделать в меню
load_button.grid(column=1, row=0)
# Главный дисплей под ними, на всю ширину и высоту
main_display.grid(column=0, row=1, columnspan=2, sticky='nwes')

# Элементы печати списка на дисплей, левая часть внизу
print_limited_check.grid(column=0, row=2)
print_button.grid(column=0, row=3)

# Кнопка выхода в самом низу слева
exit_button.grid(column=0, row=5, sticky=W)

# Элементы сортировки, правая часть внизу
sort_radio_bubble.grid(column=1, row=2, sticky=W)
sort_radio_selection.grid(column=1, row=3, sticky=W)
sort_radio_insertion.grid(column=1, row=4, sticky=W)
sort_button.grid(column=1, row=5)

# Паддинг для всех элементов в рамке
for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

# Кнопка <x> выводит текущие размеры окна 
# и требуемые размеры окна в малый дисплей
root.bind('<x>', 
    lambda e: debug_display_var.set(
        str(root.winfo_width())+" "
        + str(root.winfo_height())+" ; " + str(root.winfo_reqwidth())+" "
        + str(root.winfo_reqheight()))
)

# Кнопка l (L) выводит длинну хранимого списка
root.bind('<l>', lambda e: debug_display_var.set(str(len(lst))))

# Запрет изменения размера окна
root.resizable(False, False)

# Основной ивент окна
root.mainloop()
