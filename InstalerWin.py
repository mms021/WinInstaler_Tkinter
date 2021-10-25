import tkinter as tk                
from tkinter import font  as tkfont 
from tkinter import messagebox ,ttk
import os , sys , zipfile


def resource_path(relative_path):
    """ for PyInstaller """
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.getcwd()
    return os.path.join(base_path, relative_path)

def zip_file():
    fantasy_zip = zipfile.ZipFile(resource_path('exe1.zip'))
    fantasy_zip.extractall(os.path.join(message.get(),"GalaktikaERP.CORP") )
    fantasy_zip.close()
    

def close_window(): 
    app.destroy()

Lisense = """" 
ЛИЦЕНЗИОННОЕ СОГЛАШЕНИЕ
для конечного пользователя

Настоящие условия являются соглашением (далее - Соглашение) между Правообладателем Общество с ограниченной ответственностью «Галактика Научно-технический центр» (ООО «Галактика НТЦ») и Лицензиатом (Конечным пользователем) и определяют условия установки и использования программы для ЭВМ - Система Галактика ERP.CORP, к которой прилагается настоящее Соглашение. Перед использованием ПО Вы обязаны сообщить о согласии с данным Соглашением в процессе установки ПО.
	0. Определение терминов 
«Программное обеспечение», «ПО» - программы для электронно-вычислительных машин (ЭВМ) Система Галактика ERP.CORP, представленная в объективной форме как совокупность данных и команд, предназначенных для функционирования ЭВМ и других компьютерных устройств в целях получения определенного результата, включая порождаемые ими аудиовизуальные отображения, сопровождающую их документацию, а также их обновления. ПО лицензируется как объект авторского права.  
  «Лицензионное соглашение», «Соглашение» - соглашение между Конечным пользователем ПО (Лицензиатом) и Правообладателем ПО или его уполномоченным лицом (Лицензиаром), о выдаче Лицензиату неисключительной лицензии на право использования ПО.
 «Лицензионные условия» - условия использования ПО, при условии выполнения Лицензиатом которых, лицензии сохраняют свое действие.
«Правообладатель» - ООО «Галактика НТЦ», ОГРН 1197746158037, ИНН 9731031681 (лицо, обладающее исключительными правами на ПО).
«Лицензиат» – лицо, которое в соответствии с условиями заключенного Соглашения, получило лицензии на право использования ПО. 
«Конечный пользователь» - физическое лицо, устанавливающее или использующее Программное обеспечение (ПО) от собственного имени; или, если ПО устанавливается или используется от имени юридического лица, «Конечный пользователь» означает юридическое лицо (включает в себя все виды коммерческих и некоммерческих организаций, государственные и муниципальные органы, предприятия и учреждения), для которого устанавливается или используется ПО, и настоящим утверждается, что данное физическое лицо уполномочено принимать все условия Соглашения и действовать от имени юридического лица.
"""



class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title_font = tkfont.Font(family='Helvetica', size=14, weight="bold")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo, PageTree, PageFinish):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Отображение'''
        frame = self.frames[page_name]
        frame.tkraise()

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, pad=7)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(5, pad=7)

        label = tk.Label(self, text="Вас приветствует мастер\n установки GalaktikaERP.CORP ", font=controller.title_font)
        label.grid(row=1, column=1 , columnspan=3)

        ldl = tk.Label(self, text="Установка системы GalaktikaERP.CORP. \nНажмите кнпку 'Далее', чтобы продолжить \nили кнопку 'Отмена' чтобы выйти\n из мастера. ", font='Times 10')
        ldl.grid(row=2, column=1, pady=4)

        button = tk.Button(self, text="Закрыть",command=close_window)
        button.grid(row=5, column=0, padx=5)

        button2 = tk.Button(self, text="Вперед", command=lambda: controller.show_frame("PageOne"))
        button2.grid(row=5, column=3)


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, pad=7)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(5, pad=7)

        label = tk.Label(self, text="Конечная папка", font=controller.title_font)
        label.grid(row=1, column=1, columnspan=3)

        label1 = tk.Label(self, text="Установка \nGalaktikaERP.CORP в:", font='Times 10')
        label1.grid(row=2, column=0)

        global message
        message = tk.StringVar(self, value=str(os.environ["PROGRAMFILES"]))
        txt = tk.Entry(self,width=50 , textvariable=message)
        txt.grid(row=2, column=1 , columnspan=3)
        
        
       

        button = tk.Button(self, text="Закрыть",command=close_window)
        button.grid(row=5, column=0, padx=5)

        button1 = tk.Button(self, text="Назад",command=lambda: controller.show_frame("StartPage"))
        button1.grid(row=5, column=2)

        button2 = tk.Button(self, text="Далее", command=lambda: controller.show_frame("PageTwo"))
        button2.grid(row=5, column=3)


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, pad=7)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(5, pad=7)

        label = tk.Label(self, text="Лицензионное соглашение", font=controller.title_font)
        label.grid(row=1, column=1, columnspan=4)

        text = tk.Text(self,width=40, height=10)
        text.insert(tk.INSERT, "text"*40)
        text.configure(state='disabled')
        text.grid(row=2, column=1 , columnspan=4)

        scroll = tk.Scrollbar(self,  command=text.yview)
        scroll.grid(row=2, column=0 )
        text.config(yscrollcommand=scroll.set)

        self.var = tk.IntVar()
        chk3 = tk.Checkbutton(self, text='Я принимаю условия лицензионного соглашения',variable=self.var )  
        chk3.grid(row=4, column=2, columnspan=4)
        
        button = tk.Button(self, text="Закрыть",command=close_window)
        button.grid(row=5, column=0, padx=5)

        button1 = tk.Button(self, text="Назад",command=lambda: controller.show_frame("PageOne"))
        button1.grid(row=5, column=4 , padx=5)

        button2 = tk.Button(self, text="Далее", command=lambda: controller.show_frame("PageTree") if self.var.get() !=0 else messagebox.showinfo('Ошибка','Требуется принять лицензионное соглашение'))
        button2.grid(row=5, column=5, padx=5)



class PageTree(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, pad=7)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(5, pad=7)

        label = tk.Label(self, text="Все готово к установке\n GalaktikaERP.CORP", font=controller.title_font)
        label.grid(row=1, column=1, columnspan=3)

        labe2 = tk.Label(self, text="Нажмите кнпку 'Установить', чтобы начать\n установку. Нажмите кнопку 'Назад' что бы проверить\n илли изменить параметры установки.\nНажмите кнопку 'Отмена' чтобы выйти\n из мастера." )
        labe2.grid(row=2, column=1, columnspan=3)

        #style = ttk.Style()
        #style.theme_use('default')
        #style.configure("blue.Horizontal.TProgressbar", background='blue')

        #bar = ttk.Progressbar(self, length=200, style='blue.Horizontal.TProgressbar')
        #bar['value'] = 70
        #bar.grid(row=3, column=1, padx=5 , columnspan=4)
        

        def Instal_run():
            #zip_file()
            lambda: controller.show_frame("PageFinish")

        button = tk.Button(self, text="Закрыть",command=close_window)
        button.grid(row=5, column=0, padx=5)

        button2 = tk.Button(self, text="Установить", command=Instal_run)
        button2.grid(row=5, column=3)

class PageFinish(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, pad=7)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(5, pad=7)

        label = tk.Label(self, text="Установка GalaktikaERP.CORP\n завершена", font=controller.title_font)
        label.grid(row=1, column=1)

        label = tk.Label(self, text="Нажмите 'Готово', чтобы выйти из\n мастера установки. ")
        label.grid(row=2, column=1)

        button = tk.Button(self, text="Готово",command=close_window)
        button.grid(row=5, column=3)



if __name__ == "__main__":
    app = SampleApp()
    app.title("Galaktika ERP.Corp")
    app.geometry("400x300+300+250")
    app.mainloop()
















