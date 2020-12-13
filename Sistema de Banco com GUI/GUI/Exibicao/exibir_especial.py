import sys
import tkinter as tk
import tkinter.ttk as ttk

class EspecialExibir:
    def __init__(self):
        global root
        root = tk.Tk()

        windowWidth = root.winfo_reqwidth()
        windowHeight = root.winfo_reqheight()
        X = int(root.winfo_screenwidth()/2 - windowWidth/2)
        Y = int(root.winfo_screenheight()/3 - windowHeight/2)
        X = int(X * 0.9)
        Y = int(Y * 0.9)

        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=[('selected', _compcolor), ('active',_ana2color)])

        root.geometry("465x352+{}+{}".format(X, Y))
        root.minsize(120, 1)
        root.maxsize(3844, 1061)
        root.resizable(1, 1)
        root.title("Exibindo usuário")
        root.configure(background="#d9d9d9")
        root.configure(highlightbackground="#d9d9d9")
        root.configure(highlightcolor="black")

        self.TFrame1Exibir = ttk.Frame(root)
        self.TFrame1Exibir.place(relx=0.013, rely=0.02, relheight=0.949, relwidth=0.974)
        self.TFrame1Exibir.configure(relief='groove')
        self.TFrame1Exibir.configure(borderwidth="2")
        self.TFrame1Exibir.configure(relief="groove")

        self.BotaoRetornar = ttk.Button(self.TFrame1Exibir, command=lambda: self.encerrar())
        self.BotaoRetornar.place(relx=0.397, rely=0.838, height=32, width=80)
        self.BotaoRetornar.configure(takefocus="")
        self.BotaoRetornar.configure(text='''Retornar''')
        self.BotaoRetornar.configure(compound='center')
        self.BotaoRetornar.configure(cursor="hand2")

        self.labelTitular = ttk.Label(self.TFrame1Exibir)
        self.labelTitular.place(relx=0.177, rely=0.057, height=63, width=132)
        self.labelTitular.configure(background="#d9d9d9")
        self.labelTitular.configure(foreground="#000000")
        self.labelTitular.configure(font="-family {Yu Gothic} -size 12")
        self.labelTitular.configure(relief="flat")
        self.labelTitular.configure(anchor='n')
        self.labelTitular.configure(justify='left')
        self.labelTitular.configure(text='''Nome do titular:''')

        self.labelDataAbert = ttk.Label(self.TFrame1Exibir)
        self.labelDataAbert.place(relx=0.155, rely=0.15, height=45, width=143)
        self.labelDataAbert.configure(background="#d9d9d9")
        self.labelDataAbert.configure(foreground="#000000")
        self.labelDataAbert.configure(font="-family {Yu Gothic} -size 12")
        self.labelDataAbert.configure(relief="flat")
        self.labelDataAbert.configure(anchor='n')
        self.labelDataAbert.configure(justify='left')
        self.labelDataAbert.configure(text='''Data de abertura:''')

        self.labelNumAgencia = ttk.Label(self.TFrame1Exibir)
        self.labelNumAgencia.place(relx=0.126, rely=0.254, height=44, width=153)
        self.labelNumAgencia.configure(background="#d9d9d9")
        self.labelNumAgencia.configure(foreground="#000000")
        self.labelNumAgencia.configure(font="-family {Yu Gothic} -size 12")
        self.labelNumAgencia.configure(relief="flat")
        self.labelNumAgencia.configure(anchor='n')
        self.labelNumAgencia.configure(justify='left')
        self.labelNumAgencia.configure(text='''Número da agência:''')

        self.labelNumConta = ttk.Label(self.TFrame1Exibir)
        self.labelNumConta.place(relx=0.143, rely=0.359, height=46, width=151)
        self.labelNumConta.configure(background="#d9d9d9")
        self.labelNumConta.configure(foreground="#000000")
        self.labelNumConta.configure(font="-family {Yu Gothic} -size 12")
        self.labelNumConta.configure(relief="flat")
        self.labelNumConta.configure(anchor='n')
        self.labelNumConta.configure(justify='left')
        self.labelNumConta.configure(text='''Número da conta:''')

        self.labelSaldo = ttk.Label(self.TFrame1Exibir)
        self.labelSaldo.place(relx=0.152, rely=0.437, height=46, width=141)
        self.labelSaldo.configure(background="#d9d9d9")
        self.labelSaldo.configure(foreground="#000000")
        self.labelSaldo.configure(font="-family {Yu Gothic} -size 12")
        self.labelSaldo.configure(relief="flat")
        self.labelSaldo.configure(anchor='e')
        self.labelSaldo.configure(justify='left')
        self.labelSaldo.configure(text='''Saldo:''')

        self.ExibirNome = ttk.Label(self.TFrame1Exibir)
        self.ExibirNome.place(relx=0.486, rely=0.057, height=25, width=217)
        self.ExibirNome.configure(background="#d9d9d9")
        self.ExibirNome.configure(foreground="#000000")
        self.ExibirNome.configure(font="TkDefaultFont")
        self.ExibirNome.configure(relief="flat")
        self.ExibirNome.configure(anchor='w')
        self.ExibirNome.configure(justify='left')
        self.ExibirNome.configure(text='''Tlabel''')

        self.ExibirDataAbert = ttk.Label(self.TFrame1Exibir)
        self.ExibirDataAbert.place(relx=0.486, rely=0.15, height=25, width=207)
        self.ExibirDataAbert.configure(background="#d9d9d9")
        self.ExibirDataAbert.configure(foreground="#000000")
        self.ExibirDataAbert.configure(font="TkDefaultFont")
        self.ExibirDataAbert.configure(relief="flat")
        self.ExibirDataAbert.configure(anchor='w')
        self.ExibirDataAbert.configure(justify='left')
        self.ExibirDataAbert.configure(text='''Tlabel''')

        self.ExibirNumAgencia = ttk.Label(self.TFrame1Exibir)
        self.ExibirNumAgencia.place(relx=0.486, rely=0.254, height=27, width=216)
        self.ExibirNumAgencia.configure(background="#d9d9d9")
        self.ExibirNumAgencia.configure(foreground="#000000")
        self.ExibirNumAgencia.configure(font="TkDefaultFont")
        self.ExibirNumAgencia.configure(relief="flat")
        self.ExibirNumAgencia.configure(anchor='w')
        self.ExibirNumAgencia.configure(justify='left')
        self.ExibirNumAgencia.configure(text='''Tlabel''')

        self.ExibirNumConta = ttk.Label(self.TFrame1Exibir)
        self.ExibirNumConta.place(relx=0.486, rely=0.359, height=26, width=216)
        self.ExibirNumConta.configure(background="#d9d9d9")
        self.ExibirNumConta.configure(foreground="#000000")
        self.ExibirNumConta.configure(font="TkDefaultFont")
        self.ExibirNumConta.configure(relief="flat")
        self.ExibirNumConta.configure(anchor='w')
        self.ExibirNumConta.configure(justify='left')
        self.ExibirNumConta.configure(text='''Tlabel''')

        self.labelLimite = ttk.Label(self.TFrame1Exibir)
        self.labelLimite.place(relx=0.159, rely=0.569, height=26, width=150)
        self.labelLimite.configure(background="#d9d9d9")
        self.labelLimite.configure(foreground="#000000")
        self.labelLimite.configure(font="-family {Yu Gothic} -size 12")
        self.labelLimite.configure(relief="flat")
        self.labelLimite.configure(anchor='n')
        self.labelLimite.configure(justify='left')
        self.labelLimite.configure(text='''Limite de saque:''')

        self.ExibirSaldo = ttk.Label(self.TFrame1Exibir)
        self.ExibirSaldo.place(relx=0.486, rely=0.47, height=26, width=207)
        self.ExibirSaldo.configure(background="#d9d9d9")
        self.ExibirSaldo.configure(foreground="#000000")
        self.ExibirSaldo.configure(font="TkDefaultFont")
        self.ExibirSaldo.configure(relief="flat")
        self.ExibirSaldo.configure(anchor='w')
        self.ExibirSaldo.configure(justify='left')
        self.ExibirSaldo.configure(text='''Tlabel''')

        self.ExibirLimite = ttk.Label(self.TFrame1Exibir)
        self.ExibirLimite.place(relx=0.486, rely=0.572, height=26, width=217)
        self.ExibirLimite.configure(background="#d9d9d9")
        self.ExibirLimite.configure(foreground="#000000")
        self.ExibirLimite.configure(font="TkDefaultFont")
        self.ExibirLimite.configure(relief="flat")
        self.ExibirLimite.configure(anchor='w')
        self.ExibirLimite.configure(justify='left')
        self.ExibirLimite.configure(text='''Tlabel''')

        self.labelTaxa = ttk.Label(self.TFrame1Exibir)
        self.labelTaxa.place(relx=0.221, rely=0.674, height=26, width=110)
        self.labelTaxa.configure(background="#d9d9d9")
        self.labelTaxa.configure(foreground="#000000")
        self.labelTaxa.configure(font="-family {Yu Gothic} -size 12")
        self.labelTaxa.configure(relief="flat")
        self.labelTaxa.configure(anchor='n')
        self.labelTaxa.configure(justify='left')
        self.labelTaxa.configure(text='''Taxa de juros:''')

        self.ExibirTaxa = ttk.Label(self.TFrame1Exibir)
        self.ExibirTaxa.place(relx=0.486, rely=0.674, height=26, width=217)
        self.ExibirTaxa.configure(background="#d9d9d9")
        self.ExibirTaxa.configure(foreground="#000000")
        self.ExibirTaxa.configure(font="TkDefaultFont")
        self.ExibirTaxa.configure(relief="flat")
        self.ExibirTaxa.configure(anchor='w')
        self.ExibirTaxa.configure(justify='left')
        self.ExibirTaxa.configure(text='''Tlabel''')

        self.menubar = tk.Menu(root,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        root.configure(menu = self.menubar)

    def iniciar(self, nome, dataAbert, numAgencia, numConta, saldo, limite, taxaJuros):
        self.ExibirNome.configure(text=nome)
        self.ExibirDataAbert.configure(text=dataAbert)
        self.ExibirNumAgencia.configure(text=numAgencia)
        self.ExibirNumConta.configure(text=numConta)
        self.ExibirSaldo.configure(text=saldo)
        self.ExibirLimite.configure(text=limite)
        self.ExibirTaxa.configure(text=taxaJuros)     
        root.mainloop()

    def encerrar(self):
        root.destroy()