import datetime
import threading
import time
from tkinter import messagebox

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox
from easygui.boxes.fileopen_box import tk

from ui_file import Ui_MainWindow

import sqlite3
import pyexcel_ods


class AppController(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  

        self.init_ui()

    def atualizar_tabela(self):
        self.ui.tableWidget_logs.setRowCount(0) 
        self.init_ui()  

    def deletar_id(self):
        ids_para_deletar = self.ui.lineEdit_data_2.text().split(",")
        ids_para_deletar = [int(id.strip()) for id in ids_para_deletar if
                            id.strip()]  

        ids_excluidos = []  
        ids_nao_excluidos = []  

        for id in ids_para_deletar:
            try:
                self.deletar_registro(id)
                ids_excluidos.append(id)  
            except Exception as e:
                ids_nao_excluidos.append(id)  
                print(f"Erro ao excluir ID {id}: {str(e)}")  

        if ids_excluidos:
            self.mensagem_id_excluido()

        if ids_nao_excluidos:
            self.mensagem_id_nao_excluido()

        self.atualizar_tabela()  

    def preencher_linha_tabela(self, row, id, nome, placa, cpf, data, tipo):
        id = QTableWidgetItem(str(id))

        item_nome = QTableWidgetItem(nome)
        placa = QTableWidgetItem(placa)
        cpf = QTableWidgetItem(cpf)
        data = QTableWidgetItem(data)
        tipo = QTableWidgetItem(tipo)

        # Centralizar o texto em cada QTableWidgetItem
        item_nome.setTextAlignment(Qt.AlignCenter)
        placa.setTextAlignment(Qt.AlignCenter)
        cpf.setTextAlignment(Qt.AlignCenter)
        data.setTextAlignment(Qt.AlignCenter)
        tipo.setTextAlignment(Qt.AlignCenter)

        # Define a cor do texto para os itens desejados
        item_nome.setForeground(QColor(255, 255, 255))  # BRANCO
        placa.setForeground(QColor(255, 255, 255))  # BRANCO
        cpf.setForeground(QColor(255, 255, 255))  # BRANCO
        data.setForeground(QColor(255, 255, 255))  # BRANCO
        tipo.setForeground(QColor(255, 255, 255))  # BRANCO
        id.setForeground(QColor(255, 255, 255))  # BRANCO

        # Defina os itens nas colunas correspondentes
        self.ui.tableWidget_logs.setItem(row, 0, id)  # Coluna 1
        self.ui.tableWidget_logs.setItem(row, 1, item_nome)  # Coluna 1
        self.ui.tableWidget_logs.setItem(row, 2, placa)
        self.ui.tableWidget_logs.setItem(row, 3, cpf)
        self.ui.tableWidget_logs.setItem(row, 4, data)
        self.ui.tableWidget_logs.setItem(row, 5, tipo)

    def selecionar_tipo(self):
        if self.ui.comboBox.currentIndex() == 0:
            self.tipo = 'CARRETA'
            print('TIPO DE CARRO =', self.tipo)

            return self.tipo

        elif self.ui.comboBox.currentIndex() == 1:
            self.tipo = 'TRUCK'
            print('TIPO DE CARRO =', self.tipo)
            return self.tipo

        elif self.ui.comboBox.currentIndex() == 2:
            self.tipo = 'FIORINO'
            print('TIPO DE CARRO =', self.tipo)
            return self.tipo


        elif self.ui.comboBox.currentIndex() == 3:
            self.tipo = 'HR'
            print('TIPO DE CARRO =', self.tipo)
            return self.tipo

    def inserir_dados(self, nome, placa, cpf, data, tipo):
        connection = sqlite3.connect("controle_acesso.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO controle_acesso (nome, placa, cpf, data,tipo) VALUES (?, ?, ?, ?, ?)",
                       (nome, placa, cpf, data, tipo))

        connection.commit()
        novo_id = cursor.lastrowid  # Obtém o ID do registro recém-inserido
        connection.close()
        return novo_id  # Retorna o novo ID

    def redefinir_ids(self):
        connection = sqlite3.connect("controle_acesso.db")
        cursor = connection.cursor()

        # Excluir todos os registros da tabela
        cursor.execute("DELETE FROM controle_acesso")

        # Redefinir a sequência de ID para começar em 1
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='controle_acesso'")

        connection.commit()
        connection.close()

        
        msg = ""

        root = tk.Tk()
        root.withdraw() 

        # Exibir a mensagem de informações usando messagebox
        mensagem = f"Banco de dados resetados. {msg}\n"
        messagebox.showinfo("", mensagem)
        root.destroy()
        self.atualizar_tabela()

    def adicionar_dados(self):
        nome = str(self.ui.lineEdit_nome.text())  
        placa = str(self.ui.lineEdit_placa.text())  
        cpf = str(self.ui.lineEdit_cpf.text())  
        data = str(self.ui.lineEdit_data.text())  
        tipo = str(
            self.selecionar_tipo())  

        if nome and placa and cpf and data and tipo:
            novo_id = self.inserir_dados(nome, placa, cpf, data, tipo)


            row_count = self.ui.tableWidget_logs.rowCount()

            self.ui.tableWidget_logs.setRowCount(row_count + 1)

            self.preencher_linha_tabela(row_count, novo_id, nome, placa, cpf, data, tipo)
            self.salvar_dados_ods()

            msg = ""

            root = tk.Tk()
            root.withdraw()  

            # Exibir a mensagem de informações usando messagebox
            mensagem = f"Veiculo inserido no banco de dados. {msg}\n"
            messagebox.showinfo("", mensagem)
            root.destroy()


    def atualizar_hora(self):
        data_hora_atual = datetime.datetime.now()

        data_hora_formatada = data_hora_atual.strftime("%d-%m-%Y %H:%M:%S")

        self.ui.lineEdit_data.setText(data_hora_formatada)

        time.sleep(1)

    def mensagem_id_excluido(self):
        # Informações sobre o software
        msg = ""

        # Criar uma janela principal (Tk)
        root = tk.Tk()
        root.withdraw()  # Oculta a janela principal

        # Exibir a mensagem de informações usando messagebox
        mensagem = f"Id excluido com sucesso. {msg}\n"
        messagebox.showinfo("", mensagem)
        root.destroy()

    def mensagem_id_nao_excluido(self):

        msg = ""

        root = tk.Tk()
        root.withdraw()  

        mensagem = f"Erro, vc não informou o id. {msg}\n"
        messagebox.showinfo("", mensagem)
        root.destroy()
        self.atualizar_hora()



    def procurar_cpf_e_exibir_mensagembox(self, cpf_procurado):
        # Conectar ao banco de dados
        connection = sqlite3.connect("controle_acesso.db")
        cursor = connection.cursor()

        # Verificar se foram inseridos 3 ou mais dígitos do CPF
        if len(cpf_procurado) >= 3:
            # Se forem inseridos 3 ou mais dígitos, realize a busca no banco de dados
            cursor.execute("SELECT id, cpf, data FROM controle_acesso WHERE cpf LIKE ? || '%'", (cpf_procurado,))
        else:
            # Caso contrário, não faça a busca e exiba uma mensagem informativa
            QMessageBox.information(None, "Busca não realizada",
                                    "Insira pelo menos 3 dígitos do CPF para realizar a busca.")
            connection.close()
            # self.atualizar_hora()
            return  # Retorna imediatamente se não houver dígitos suficientes

        # Buscar todos os registros correspondentes
        registros_encontrados = cursor.fetchall()

        # Contar o número de registros correspondentes
        numero_registros = len(registros_encontrados)

        # Fechar a conexão com o banco de dados
        connection.close()

        if numero_registros == 0:
            QMessageBox.information(None, "CPF não encontrado",
                                    "Nenhum registro correspondente encontrado no banco de dados.")
        else:
            # Preparar a mensagem com os registros encontrados
            mensagem = f"Total de entregas ( {numero_registros}  ):\n"
            for registro in registros_encontrados:
                id_registro, cpf, data = registro  # Extrair os campos do registro
                mensagem += f"ID: {id_registro}, CPF: {cpf}, Data: {data}\n"

            # Exibir a messagebox com os registros encontrados
            QMessageBox.information(None, "Registros Encontrados", mensagem)
            self.atualizar_hora()

    def search_cpf(self):
        # Chame a função com o CPF que você deseja procurar
        cpf_procurado = self.ui.lineEdit_procurar_cpf.text()

        self.procurar_cpf_e_exibir_mensagembox(cpf_procurado)


    def deletar_registro(self, id):
        connection = sqlite3.connect("controle_acesso.db")
        cursor = connection.cursor()
        cursor.execute("DELETE FROM controle_acesso WHERE id=?", (id,))
        connection.commit()
        connection.close()

        salvar = threading.Thread(target=self.salvar_dados_ods)
        salvar.daemon = True
        salvar.start()
        salvar.join()

        att_hora = threading.Thread(target=self.atualizar_hora)
        att_hora.daemon = True
        att_hora.start()
        att_hora.join()

    def salvar_dados_ods(self):
        connection = sqlite3.connect("controle_acesso.db")
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM controle_acesso")
        data = cursor.fetchall()

        connection.close()

        if not data:
            print("Nenhum dado para salvar.")
            return

        arquivo_ods = "Relatorio_banco_dados.ods"

        carreta_count = 0
        truck_count = 0
        fiorino_count = 0
        hr_count = 0

        # Analisar os dados e contar os tipos
        for row in data:
            tipo = row[5]
            print("Tipo:", tipo)  # Adicione esta linha para depurar
            if tipo == "CARRETA":
                carreta_count += 1
            elif tipo == "TRUCK":
                truck_count += 1
            elif tipo == "FIORINO":
                fiorino_count += 1
            elif tipo == "HR":
                hr_count += 1

        # Criar o conteúdo do relatório com os números contados
        content = [
            [],  # Linha em branco
            ['⬛️⬛️⬛' * 5],  # Linha em branco

            ["◾◾️◾️◾️️️◾   ►Relatório do Banco de Dados◄   ◾◾◾️◾️◾️"],

            ["ID", "NOME", "PLACA", "CPF", "DATA", "TIPO"],  # Cabeçalho
        ]

        # Adicionar os dados do banco de dados
        content += data

        # Adicionar informações sobre a contagem de tipos
        content += [
            [],  # Linha em branco
            ['⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️' * 2],  
            ['◾️◾️◾️◾️  ►Total de carros◄  ◾ ️◾️◾️◾️'],  
            ["   CARRETA:    ", carreta_count],
            ["   TRUCK:    ", truck_count],
            ["   FIORINO:    ", fiorino_count],
            ["   HR:    ", hr_count],
            ['⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️' * 2],  
        ]

        # Salvar os dados no formato ODS
        pyexcel_ods.save_data(arquivo_ods, {"Relatório": content})

        print("Relatório do banco de dados salvo em", arquivo_ods)
        self.atualizar_hora()

    def sobre(self):
        try:
            criador = "Felipe Samuel"
            telefone_suporte = "+55 (11) 91912-7954"
            email_suporte = "lipinhodesign@live.com"
            versao = "1.0"

            root = tk.Tk()
            root.withdraw()  

            # Exibir a mensagem de informações usando messagebox
            mensagem = f"Software criado por: {criador}\n" \
                       f"Telefone de suporte: {telefone_suporte}\n" \
                       f"Email de suporte: {email_suporte}\n" \
                       f"Versão do software: {versao}"

            messagebox.showinfo("Informações do Software", mensagem)
            root.destroy()
            self.atualizar_hora()
        except RuntimeError as e:
            print(e)

    def init_ui(self):
        self.ui.tableWidget_logs.setRowCount(0)

        self.thread_atualizacao = threading.Thread(target=self.atualizar_hora)
        self.thread_atualizacao.start()

        # Busca os dados da base de dados
        connection = sqlite3.connect("controle_acesso.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM controle_acesso")
        data = cursor.fetchall()
        connection.close()
        # Analisar os dados e contar os tipos
        self.ui.pushButton_sobre.clicked.connect(self.sobre)
        self.ui.pushButton_addveiculo.clicked.connect(self.adicionar_dados)
        self.ui.pushButton_deletar_id.clicked.connect(self.deletar_id)
        self.ui.comboBox.activated.connect(self.selecionar_tipo)
        self.ui.pushButton_procurar_cpf.clicked.connect(self.search_cpf)
        self.ui.pushButton_novobotao.clicked.connect(self.redefinir_ids)

        if not data:
            print("A tabela está vazia.")
        else:
            # Configura o número de linhas e colunas do QTableWidget
            self.ui.tableWidget_logs.setRowCount(len(data))
            self.ui.tableWidget_logs.setColumnCount(6)  # Cinco colunas (id, nome, placa, cpf, data, tipo)

            # Preenche a tabela com os dados da base de dados
            for row_index, row_data in enumerate(data):
                id = row_data[0]
                nome = row_data[1]
                placa = row_data[2]
                cpf = row_data[3]
                data = row_data[4]
                tipo = row_data[5]

                self.preencher_linha_tabela(row_index, id, nome, placa, cpf, data, tipo)


if __name__ == "__main__":
    app = QApplication([])
    controller = AppController()
    controller.show()
    app.exec_()
