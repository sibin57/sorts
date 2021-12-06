####################################
#изначальный набор комманд:
#1 загрузить список в панель
#2 отсортировать список пузырьком
#3 отсортировать список выбором
#4 отсортировать список вставками
#5 вывести полученый список в панель
#0 выход
# 
####################################
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename

def sort(*args):
    if lst:
        if sort_type.get() =='bubble':

            had_swaps = True
            while had_swaps:
                had_swaps = False
                for i in range(1, len(lst)):
                    if lst[i]<lst[i-1]:
                        lst[i], lst[i-1] = lst[i-1], lst[i]
                        had_swaps = True
            debug_display_var.set("список отсортирован пузырьком")
            
        elif sort_type.get() == 'selection':
            for i in range(len(lst)-1, -1, -1):
                for j in range(i, -1, -1):
                    if lst[j]>lst[i]:
                        lst[i], lst[j] = lst[j], lst[i]
            debug_display_var.set("список отсортирован выбором")

        elif sort_type.get() == 'insertion':

            debug_display_var.set("список НЕ отсортирован вставками")
    else:
        debug_display_var.set('Список пуст')

def load_lst(*args):
    
    filename = askopenfilename()
    file = open(filename,'r')

    try:
        global lst
        lst=[]
        for line in file:
            lst.extend(list(map(int, line.split())))
            debug_display_var.set(lst)
        main_display_var.set("Список загружен")
    except:
        main_display_var.set("Нечитаемый файл")

def update_display(*args):
    if lst:
        if print_all_state.get():
            main_display_var.set(", ".join(map(str,lst)))
        else:
            main_display_var.set(", ".join(map(str,lst[:20]))+"...")
    else:
        main_display_var.set("Список пуст")


lst = []#глобальный лист

#определяем элементы окна
root = Tk()
root.title("Сортировка числовых списков")

#подсветка для дебага
color_style = ttk.Style()
color_style.configure('Color.TFrame', background='#FF0000', borderwidth=5, relief='raised')

mainframe = ttk.Frame(root, padding=12,)

#малый дисплей
debug_display_var = StringVar()
debug_display_var.set("пусто")
debug_display =ttk.Label(mainframe, textvariable=debug_display_var, wraplength=150)

#загрузка списка из файла
load_button = ttk.Button(mainframe, text='загрузить список из файла', command=load_lst)

#главный дисплей
main_display_var = StringVar()#переменная дисплея
main_display_var.set("Загрузите список из файла")
#wraplength указан константой, что не очень хорошо, но я без понятия, как сделать его по требуемой минимальной ширине
main_display = ttk.Label(mainframe, textvariable=main_display_var, borderwidth=8, relief='ridge', wraplength=340, justify='center',anchor='center')

#печать на дисплей
print_all_state = BooleanVar(value=True)
print_all_check = ttk.Checkbutton(mainframe, text="напечатать список целиком", variable=print_all_state)

print_button = ttk.Button(mainframe, text='напечатать список', command=update_display)

#выбор и сортировка списка

sort_type = StringVar(value='bubble')

sort_radio_bubble = ttk.Radiobutton(mainframe, text="сортировка пузырьком", variable=sort_type, value='bubble' )
sort_radio_selection = ttk.Radiobutton(mainframe, text="сортировка выбором", variable=sort_type, value='selection' )
sort_radio_insertion = ttk.Radiobutton(mainframe, text="сортировка вставками", variable=sort_type, value='insertion' )

sort_button = ttk.Button(mainframe, text="отсортировать", command=sort)

#TODO кнопка выхода

#расставляем элементы

mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

#дебаг-дисплейчик
debug_display.grid(column=0, row=0)
#кнопка загрузки в самом верху
load_button.grid(column=1, row=0) #заменить на column=0, row=0, columnspan=2
#дисплей под ней, на всю ширину и высоту
main_display.grid(column=0, row=1, columnspan=2, sticky='nwes')

#элементы печати, левая часть внизу
print_all_check.grid(column=0, row=2)
print_button.grid(column=0, row=3)

#элементы сортировки, правая часть внизу
sort_radio_bubble.grid(column=1, row=2, sticky=W)
sort_radio_selection.grid(column=1, row=3, sticky=W)
sort_radio_insertion.grid(column=1, row=4, sticky=W)
sort_button.grid(column=1, row=5)

#растяигивание элементов?
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

#паддинг для всех элементов
for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

root.bind('<x>', lambda e: debug_display_var.set(str(root.winfo_width())+" "+ str(root.winfo_height())+" ; " + str(root.winfo_reqwidth())+" "+ str(root.winfo_reqheight()) ))

root.resizable(False, False)

#root.maxsize(x,y)

root.mainloop()