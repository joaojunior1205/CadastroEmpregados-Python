from Banco import Banco

class Empregados(object):

    def __init__(self, idEmpregado = 0, nome="", telefone="", email="", usuario="", senha=""):
        self.info = {}
        self.idEmpregado = idEmpregado
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.usuario = usuario
        self.senha = senha

    def insertEmpregados(self):

        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("insert into empregados (nome, telefone, email, usuario, senha) values ('" + self.nome + "', '" + self.telefone + "', '" + self.email + "', '" + self.usuario + "', '" + self.senha + "' )")

            banco.conexao.commit()
            c.close()

            return "Usuário cadastrado com sucesso!"
        except:
            return "Ocorreu um erro na inserção de usuário"

    def updateEmpregados(self):

        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("update empregados set nome= '" + self.nome + "', telefone = '" + self.telefone + "', email= '" + self.email + "', usuario= '" + self.usuario + "', senha= '" + self.senha + "' where idEmpregado = " + self.idEmpregado + " ")

            banco.conexao.commit()
            c.close()

            return "Usuário atualizado com sucesso!"
        except:
            return "Ocorreu um erro na alteração do usuário"

    def deleteEmpregados(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()

            c.execute("delete from empregados where idEmpregado = " + self.idEmpregado + " ")

            banco.conexao.commit()
            c.close()

            return "Usuário excluído com sucesso!"
        except:
            return "Ocorreu um erro na exclusão do usuário"

    def selectEmpregados(self, idEmpregado):
        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("select * from empregados WHERE idEmpregado = " + idEmpregado + " ")

            for linha in c:
                self.idEmpregado = linha[0]
                self.nome = linha[1]
                self.telefone = linha[2]
                self.email = linha[3]
                self.usuario = linha[4]
                self.senha = linha[5]

            c.close()

            return "Busca feita com sucesso"
        except:
            return "Ocorreu um erro na busca de usuário"
