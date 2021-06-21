from movimentofolha import MovimentoFolha

class Colaborador:

    def __init__(self, codigo, nome, endereco, telefone, bairro, cep, cpf, salarioAtual):
        self._codigo = codigo
        self._nome = nome
        self._endereco = endereco
        self._telefone = telefone
        self._bairro = bairro
        self._cep = cep
        self._cpf = cpf
        self._salarioAtual = salarioAtual
        self._movimentos = []


    def get_salario(self):
        return self._salarioAtual

    # Quinta questão
    def inserirMovimentos(self, movi):
        if type(movi) == MovimentoFolha:
            self._movimentos.append(movi)

    # Nona questão
    def calcularSalario(self):
        totalProventos = 0
        totalDescontos = 0
        for movi in self._movimentos:
            if movi.get_tipomovi() == 1:
                totalProventos += movi.get_valor()
            elif movi.get_tipomovi() == 2:
                totalDescontos += movi.get_valor()
            else:
                return 'Tipo não reconhecido'

            salarioLiquido = self._salarioAtual + totalProventos - totalDescontos
            print(f'Código: {self._codigo} Nome: {self._nome}\nSalário: {self._salarioAtual} Total Proventos: {totalProventos} Total Descontos: {totalDescontos} Valor líquido a receber: {salarioLiquido} ')



