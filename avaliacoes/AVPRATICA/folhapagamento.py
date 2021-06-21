from movimentofolha import MovimentoFolha


class FolhaPagamento:


    def __init__(self, mes, ano, totalDescontos, totalProventos):
        self._mes = mes
        self._ano = ano
        self._totalDescontos = totalDescontos
        self._totalProventos = totalProventos
        self._colaboradores = []
        self._movimentos = []

        # Método q retorna soma dos salários

    def salarioTotal(self):
        salarioTotal = 0
        for colaborador in self._colaboradores:
            salarioTotal += colaborador.get_salario()
        return salarioTotal

    # Oitava Questão
    def calcularFolha(self):
        for movi in self._movimentos:
            if movi.get_tipomovi() == 1:
                self._totalProventos += movi.get_valor()
            elif movi.get_tipomovi() == 2:
                self._totalDescontos += movi.get_valor()
            else:
                return 'Tipo não reconhecido'

        total = (self.salarioTotal() + self._totalProventos) - self._totalDescontos
        print(f'Total de Salário = {total} Total de Proventos = {self._totalProventos} Total de Descontos = {self._totalDescontos} Total a Pagar = {total + self._totalProventos}')




    # Quarta questão
    def inserirMovimentos(self, movi):
        if type(movi) == MovimentoFolha:
            self._movimentos.append(movi)

    def set_inserirColaboradores(self, colaborador):
        self._colaboradores.append(colaborador)

