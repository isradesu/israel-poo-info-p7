from tipomovimento import TipoMovimento

class MovimentoFolha:

    def __init__(self, colaborador, descricao, valor, tipomovimento):
        self._descricao = descricao
        self._valor = valor
        self._colaborador = colaborador
        self._tipomovimento = tipomovimento

    def get_valor(self):
        return self._valor

    def get_tipomovi(self):
        return self._tipomovimento


