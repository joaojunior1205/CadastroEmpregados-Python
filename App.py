from Empregados import Empregados
from tkinter import *


class Application:
    def __init__(self, master=None):
        self.fonte = ("Arial", "11")

        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()

        self.container2 = Frame(master)
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.pack()

        self.container3 = Frame(master)
        self.container3["padx"] = 20
        self.container3["pady"] = 5
        self.container3.pack()

        self.container4 = Frame(master)
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.pack()

        self.container5 = Frame(master)
        self.container5["padx"] = 20
        self.container5["pady"] = 5
        self.container5.pack()

        self.container6 = Frame(master)
        self.container6["padx"] = 20
        self.container6["pady"] = 5
        self.container6.pack()

        self.container7 = Frame(master)
        self.container7["padx"] = 20
        self.container7["pady"] = 5
        self.container7.pack()

        self.container8 = Frame(master)
        self.container8["padx"] = 20
        self.container8["pady"] = 5
        self.container8.pack()

        self.container9 = Frame(master)
        self.container9["pady"] = 15
        self.container9.pack()

        self.titulo = Label(self.container1, text="Informe os dados:")
        self.titulo["font"] = ("Calibri", "11", "bold")
        self.titulo.pack()

        self.labelEmpregado = Label(self.container2, text="ID: ", font=self.fonte, width='10')
        self.labelEmpregado.pack(side=LEFT)

        self.txtIdEmpregado = Entry(self.container2)
        self.txtIdEmpregado["width"] = 10
        self.txtIdEmpregado["font"] = self.fonte
        self.txtIdEmpregado.pack(side=LEFT)

        self.btnBuscar = Button(self.container2, text="Buscar", font=self.fonte, width=10)
        self.btnBuscar["command"] = self.buscarEmpregado
        self.btnBuscar.pack(side=RIGHT)

        self.labelNome = Label(self.container3, text="Nome:", font=self.fonte,width=10)
        self.labelNome.pack(side=LEFT)

        self.txtNome = Entry(self.container3)
        self.txtNome["width"] = 25
        self.txtNome["font"] = self.fonte
        self.txtNome.pack(side=LEFT)

        self.labelTelefone = Label(self.container4, text="Telefone:", font=self.fonte, width=10)
        self.labelTelefone.pack(side=LEFT)

        self.txtTelefone = Entry(self.container4)
        self.txtTelefone["width"] = 25
        self.txtTelefone["font"] = self.fonte
        self.txtTelefone.pack(side=LEFT)

        self.labelEmail = Label(self.container5, text="E-mail:", font=self.fonte, width=10)
        self.labelEmail.pack(side=LEFT)

        self.txtEmail = Entry(self.container5)
        self.txtEmail["width"] = 25
        self.txtEmail["font"] = self.fonte
        self.txtEmail.pack(side=LEFT)

        self.labelUsuario = Label(self.container6, text="Usuário:", font=self.fonte, width=10)
        self.labelUsuario.pack(side=LEFT)

        self.txtUsuario = Entry(self.container6)
        self.txtUsuario["width"] = 25
        self.txtUsuario["font"] = self.fonte
        self.txtUsuario.pack(side=LEFT)

        self.labelSenha = Label(self.container7, text="Senha:", font=self.fonte, width=10)
        self.labelSenha.pack(side=LEFT)

        self.txtSenha = Entry(self.container7)
        self.txtSenha["width"] = 25
        self.txtSenha["show"] = "*"
        self.txtSenha["font"] = self.fonte
        self.txtSenha.pack(side=LEFT)

        self.bntInsert = Button(self.container8, text="Inserir", font=self.fonte, width=12)
        self.bntInsert["command"] = self.inserirEmpregado
        self.bntInsert.pack(side=LEFT)

        self.bntAlterar = Button(self.container8, text="Alterar", font=self.fonte, width=12)
        self.bntAlterar["command"] = self.alterarEmpregado
        self.bntAlterar.pack(side=LEFT)

        self.bntExcluir = Button(self.container8, text="Excluir", font=self.fonte, width=12)
        self.bntExcluir["command"] = self.excluirEmpregado
        self.bntExcluir.pack(side=LEFT)

        self.labelMsg = Label(self.container9, text="")
        self.labelMsg["font"] = ("Verdana", "11", "italic")
        self.labelMsg.pack()


    def inserirEmpregado(self):

        user = Empregados()

        user.nome = self.txtNome.get()
        user.telefone = self.txtTelefone.get()
        user.email = self.txtEmail.get()
        user.usuario = self.txtUsuario.get()
        user.senha = self.txtSenha.get()

        self.labelMsg["text"] = user.insertEmpregados()

        self.txtIdEmpregado.delete(0, END)
        self.txtNome.delete(0, END)
        self.txtTelefone.delete(0, END)
        self.txtEmail.delete(0, END)
        self.txtUsuario.delete(0, END)
        self.txtSenha.delete(0, END)

    def alterarEmpregado(self):

        user = Empregados()

        user.idEmpregado = self.txtIdEmpregado.get()
        user.nome = self.txtNome.get()
        user.telefone = self.txtTelefone.get()
        user.email = self.txtEmail.get()
        user.usuario = self.txtUsuario.get()
        user.senha = self.txtSenha.get()

        self.labelMsg["text"] = user.updateEmpregados()

        self.txtIdEmpregado.delete(0, END)
        self.txtNome.delete(0, END)
        self.txtTelefone.delete(0, END)
        self.txtEmail.delete(0, END)
        self.txtUsuario.delete(0, END)
        self.txtSenha.delete(0, END)


    def excluirEmpregado(self):

        user = Empregados()

        user.idEmpregado = self.txtIdEmpregado.get()

        self.labelMsg["text"] = user.deleteEmpregados()

        self.txtIdEmpregado.delete(0, END)
        self.txtNome.delete(0, END)
        self.txtTelefone.delete(0, END)
        self.txtEmail.delete(0, END)
        self.txtUsuario.delete(0, END)
        self.txtSenha.delete(0, END)


    def buscarEmpregado(self):

        user = Empregados()

        idEmpregado = self.txtIdEmpregado.get()

        self.labelMsg["text"] = user.selectEmpregados(idEmpregado)

        self.txtIdEmpregado.delete(0, END)
        self.txtIdEmpregado.insert(INSERT, user.idEmpregado)

        self.txtNome.delete(0, END)
        self.txtNome.insert(INSERT, user.nome)

        self.txtTelefone.delete(0, END)
        self.txtTelefone.insert(INSERT, user.telefone)

        self.txtEmail.delete(0, END)
        self.txtEmail.insert(INSERT, user.email)

        self.txtUsuario.delete(0, END)
        self.txtUsuario.insert(INSERT, user.usuario)

        self.txtSenha.delete(0, END)
        self.txtSenha.insert(INSERT, user.senha)


root = Tk()
Application(root)
root.mainloop()
