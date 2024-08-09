import tkinter as tk
from tkinter import ttk
import crud as crud


class PrincipalBD:
    def __init__(self, win):
        self.objBD = crud.AppBD()
        # componentes
        self.lblId = tk.Label(win, text='ID:')
        self.lblTatuador = tk.Label(win, text='Nome do Tatuador')
        self.lblCliente = tk.Label(win, text='Nome do Cliente')
        self.lblWhatsapp = tk.Label(win, text='WhatsApp')
        self.lblDescricao = tk.Label(win, text='Descrição')
        self.lblValor = tk.Label(win, text='Valor')

        self.txtId = tk.Entry(bd=3)
        self.txtTatuador = tk.Entry()
        self.txtCliente = tk.Entry()
        self.txtWhatsapp = tk.Entry()
        self.txtDescricao= tk.Entry()
        self.txtValor = tk.Entry()
        self.btnCadastrar = tk.Button(win, text='Cadastrar', command=self.fCadastrarProduto)
        self.btnAtualizar = tk.Button(win, text='Atualizar', command=self.fAtualizarProduto)
        self.btnExcluir = tk.Button(win, text='Excluir', command=self.fExcluirProduto)
        self.btnLimpar = tk.Button(win, text='Limpar', command=self.fLimparTela)
        # ----- Componente TreeView --------------------------------------------
        self.dadosColunas = ("Id", "Tatuador", "Cliente", "Whatsapp", "Descricao", "Valor")

        self.treeProdutos = ttk.Treeview(win,
                                         columns=self.dadosColunas,
                                         selectmode='browse')

        self.verscrlbar = ttk.Scrollbar(win,
                                        orient="vertical",
                                        command=self.treeProdutos.yview)
        self.verscrlbar.pack(side='right', fill='x')

        self.treeProdutos.configure(yscrollcommand=self.verscrlbar.set)

        self.treeProdutos.heading("Id", text="Id")
        self.treeProdutos.heading("Tatuador", text="Tatuador")
        self.treeProdutos.heading("Cliente", text="Cliente")
        self.treeProdutos.heading("Whatsapp", text="Whatsapp")
        self.treeProdutos.heading("Descricao", text="Descricao")
        self.treeProdutos.heading("Valor", text="Valor")

        self.treeProdutos.column("Id", minwidth=0, width=60)
        self.treeProdutos.column("Tatuador", minwidth=0, width=60)
        self.treeProdutos.column("Cliente", minwidth=0, width=60)
        self.treeProdutos.column("Whatsapp", minwidth=0, width=60)
        self.treeProdutos.column("Descricao", minwidth=0, width=60)
        self.treeProdutos.column("Valor", minwidth=0, width=60)

        self.treeProdutos.pack(padx=5, pady=5)

        self.treeProdutos.bind("<<TreeviewSelect>>",
                               self.apresentarRegistrosSelecionados)
        # ---------------------------------------------------------------------
        # posicionamento dos componentes na janela
        # ---------------------------------------------------------------------
        self.lblId.place(x=100, y=10)
        self.txtId.place(x=250, y=10)

        self.lblTatuador.place(x=100, y=50)
        self.txtTatuador.place(x=250, y=50)

        self.lblCliente.place(x=100, y=90)
        self.txtCliente.place(x=250, y=90)

        self.lblWhatsapp.place(x=100, y=130)
        self.txtWhatsapp.place(x=250, y=130)

        self.lblDescricao.place(x=100, y=170)
        self.txtDescricao.place(x=250, y=170)

        self.lblValor.place(x=100, y=210)
        self.txtValor.place(x=250, y=210)
#aqui atençao
        self.btnCadastrar.place(x=100, y=250)
        self.btnAtualizar.place(x=200, y=250)
        self.btnExcluir.place(x=300, y=250)
        self.btnLimpar.place(x=400, y=250)

        self.treeProdutos.place(x=100, y=300)
        self.verscrlbar.place(x=605, y=300, height=225)
        self.carregarDadosIniciais()

    # -----------------------------------------------------------------------------
    def apresentarRegistrosSelecionados(self, event):
        self.fLimparTela()
        for selection in self.treeProdutos.selection():
            item = self.treeProdutos.item(selection)
            ident, tatuador, cliente, whatsapp, descricao, valor = item["values"][0:6]
            self.txtId.insert(0, ident)
            self.txtTatuador.insert(0, tatuador)
            self.txtCliente.insert(0, cliente)
            self.txtWhatsapp.insert(0, whatsapp)
            self.txtDescricao.insert(0, descricao)
            self.txtValor.insert(0, valor)
        # -----------------------------------------------------------------------------

    def carregarDadosIniciais(self):
        try:
            self.id = 0
            self.iid = 0
            registros = self.objBD.selecionarDados()
            print("************ dados dsponíveis no BD ***********")
            for item in registros:
                ident = item[0]
                tatuador = item[1]
                cliente = item[2]
                whatsapp = item[3]
                descricao = item[4]
                valor = item[5]
                print("Id = ", ident)
                print("Tatuador = ", tatuador)
                print("Cliente = ", cliente)
                print("Whatsapp = ", whatsapp)
                print("Descrição = ", descricao)
                print("Valor  = ", valor, "\n")

                self.treeProdutos.insert('', 'end',
                                         iid=self.iid,
                                         values=(ident, tatuador, cliente, whatsapp, descricao, valor))
                self.iid = self.iid + 1
                self.id = self.id + 1
            print('Dados da Base')
        except:
            print('Ainda não existem dados para carregar')
        # -----------------------------------------------------------------------------

    # LerDados da Tela
    # -----------------------------------------------------------------------------
    def fLerCampos(self):
        try:
            print("************ dados disponíveis ***********")
            ident = int(self.txtId.get())
            print('id', ident)
            tatuador = self.txtTatuador.get()
            print('tatuador', tatuador)
            cliente = self.txtCliente.get()
            print('cliente', cliente)
            whatsapp = self.txtWhatsapp.get()
            print('whatsapp', whatsapp)
            descricao = self.txtDescricao.get()
            print('descricao', descricao)
            valor = float(self.txtValor.get())
            print('valor', valor)
            print('Leitura dos Dados com Sucesso!')
        except:
            print('Não foi possível ler os dados.')
        return ident, tatuador, cliente, whatsapp, descricao, valor

    # -----------------------------------------------------------------------------
    # Cadastrar Produto
    # -----------------------------------------------------------------------------
    def fCadastrarProduto(self):
        try:
            print("************ dados disponíveis ***********")
            ident, tatuador, cliente, whatsapp, descricao, valor = self.fLerCampos()
            self.objBD.inserirDados(tatuador, cliente, whatsapp, descricao, valor)
            self.treeProdutos.insert('', 'end',
                                     iid=self.iid,
                                     values=(ident, tatuador, cliente, whatsapp, descricao, valor))
            self.iid = self.iid + 1
            self.id = self.id + 1
            self.fLimparTela()
            print('Produto Cadastrado com Sucesso!')
        except:
            print('Não foi possível fazer o cadastro.')

    # -----------------------------------------------------------------------------
    # Atualizar Produto
    # -----------------------------------------------------------------------------
    def fAtualizarProduto(self):
        try:
            print("************ dados dsponíveis ***********")
            ident, tatuador, cliente, whatsapp, descricao, valor = self.fLerCampos()
            self.objBD.atualizarDados(tatuador, cliente, whatsapp, descricao, valor)
            # recarregar dados na tela
            self.treeProdutos.delete(*self.treeProdutos.get_children())
            self.carregarDadosIniciais()
            self.fLimparTela()
            print('Produto Atualizado com Sucesso!')
        except:
            print('Não foi possível fazer a atualização.')

    # -----------------------------------------------------------------------------
    # Excluir Produto
    # -----------------------------------------------------------------------------
    def fExcluirProduto(self):
        try:
            print("************ dados dsponíveis ***********")
            ident, tatuador, cliente, whatsapp, descricao, valor = self.fLerCampos()
            self.objBD.excluirDados(id)
            # recarregar dados na tela
            self.treeProdutos.delete(*self.treeProdutos.get_children())
            self.carregarDadosIniciais()
            self.fLimparTela()
            print('Produto Excluído com Sucesso!')
        except:
            print('Não foi possível fazer a exclusão do produto.')

    # -----------------------------------------------------------------------------
    # Limpar Tela
    # -----------------------------------------------------------------------------
    def fLimparTela(self):
        try:
            print("************ dados dsponíveis ***********")
            self.txtID.delete(0, tk.END)
            self.txtTatuador.delete(0, tk.END)
            self.txtCliente.delete(0, tk.END)
            self.txtWhatsapp.delete(0, tk.END)
            self.txtDescricao.delete(0, tk.END)
            self.txtValor.delete(0, tk.END)
            print('Campos Limpos!')
        except:
            print('Não foi possível limpar os campos.')


# -----------------------------------------------------------------------------
# Programa Principal
# -----------------------------------------------------------------------------
janela = tk.Tk()
principal = PrincipalBD(janela)
janela.title('Bem Vindo a Aplicação de Banco de Dados')
janela.geometry("720x600+10+10")
janela.mainloop()
# -----------------------------------------------------------------------------




