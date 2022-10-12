class No:
    def __init__(self, valor):
        self.primeiro = valor
        self.proximo = None

    def mostra_no(self):
        print(self.primeiro)

class FilaEncadeada:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def __fila_vazia(self):
        return self.primeiro == None

    def primeiro_fila(self):
        if self.__fila_vazia():
            print('A fila está vazia')
            return
        else:
            return self.primeiro

    def insere_inicio_fila(self, valor):
        novo = No(valor)
        if self.__fila_vazia():
            self.ultimo = novo
        novo.proximo = self.primeiro
        self.primeiro = novo

    def insere_final_fila(self, valor):
        novo = No(valor)
        if self.__fila_vazia():
            self.primeiro = novo
        else:
            self.ultimo.proximo = novo
        self.ultimo = novo

    def excluir_inicio_fila(self):
        if self.__fila_vazia():
            print('A lista está vazia.')
            return

        temp = self.primeiro
        if self.primeiro.proximo == None:
            self.ultimo = None
        self.primeiro = self.primeiro.proximo
        return temp

    def mostrar_fila(self):
        if self.__fila_vazia():
            print('A lista está vazia.')
            return
        atual = self.primeiro
        while atual != None:
            atual.mostra_no()
            atual = atual.proximo

    def girar_fila(self, qtd):
        if self.__fila_vazia():
            print('A fila está vazia.')
            return
        if self.primeiro.proximo == None:
            print('A fila só contém 1 elemento.')
            return
        else:
            while qtd != 0:
                ultimo_elemento = self.excluir_inicio_fila()
                self.insere_final_fila(ultimo_elemento)
                qtd -= 1


fila = FilaEncadeada()
fila.insere_inicio_fila(2)
fila.insere_inicio_fila(3)
fila.insere_inicio_fila(4)
fila.insere_inicio_fila(5)
fila.girar_fila(4)
fila.mostrar_fila()