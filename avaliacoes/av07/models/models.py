import datetime


class Cliente:
    __tablename__ = 'cliente'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150))
    codigo = db.Column(db.Integer)
    cnpjcpf = db.Column(db.String(150))
    tipo = db.Column(db.String(150))

    def __init__(self, id, nome, codigo, cnpjcpf, tipo):
        self.id = id
        self.nome = nome
        self.codigo = codigo
        self.cnpjcpf = cnpjcpf
        self.tipo = tipo

    def to_json(self):
        return {"id": self.id, "nome": self.nome, "codigo": self.codigo, "cnpjcpf": self.cnpjcpf}

    def str(self):
        string = f"\nId={self.id} Codigo={self.codigo} Nome={self.nome} CNPJ/CPF={self.cnpjcpf} Tipo{self.tipo}"
        return string


class Produto:
    __tablename__ = 'produto'

    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.Integer)
    descricao = db.Column(db.String(150))
    valorUnitario = db.Column(db.Float)

    def __init__(self, id, codigo, descricao, valorUnitario):
        self.id = id
        self.codigo = codigo
        self.descricao = descricao
        self.valorUnitario = valorUnitario

    def to_json(self):
        return {"id": self.id, "codigo": self.codigo, "descricao": self.descricao, "valorUnitario": self.valorUnitario}

    def str(self):
        string = f"\nId={self.id} Codigo={self.codigo} Descricao={self.descricao} Valor Unitario={self.valorUnitario}"
        return string


class NotaFiscal:
    __tablename__ = 'notafiscal'

    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(150))

    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'))
    itens = db.relationship("ItemNotaFiscal")

    def __init__(self, id, codigo, cliente, lista_itens=None):
        self.id = id
        self.codigo = codigo
        self.cliente = cliente
        self.lista_itens = lista_itens
        self.itens = []
        self.data = datetime.datetime.now()
        self.valorNota = 0.0

    def str_itens(self):
        if self.lista_itens is None:
            itens_json = [item for item in self.itens]
            return itens_json
        else:
            return self.lista_itens

    def to_json(self):
        return {"id": self.id, "codigo": self.codigo, "cliente": self.cliente, "itens": self.str_itens(),
                "data": self.data_nota(), "valorNota": self.valorNota}

    def set_cliente(self, cliente):
        if isinstance(cliente, Cliente):
            self.cliente = cliente

    def data_nota(self):
        lista_data_e_hora = str(self.data).split()
        data_lista = lista_data_e_hora[0].split('-')
        data_final_nota = f'{data_lista[2]}/{data_lista[1]}/{data_lista[0]}'
        return data_final_nota

    def add_item(self, item):
        self.itens.append(item)

    def calcular_total_nota(self, controle=False):
        valor = 0.0
        for item in self.itens:
            valor = valor + item["valorItem"]
        self.valorNota = valor
        if controle is True:
            return valor

    def get_sequencial(self, item):
        seq = str(item['sequencial'])
        if len(seq) > 2:
            return seq

        elif len(seq) > 1:
            return f'0{seq}'

        return f'00{seq}'

    def imprimir_nota_fiscal(self):

        json_nota = {
        'NOTA FISCAL': self.data_nota(),
        'Cliente': self.cliente['codigo'],
        'Nome': self.cliente['nome'],
        'CPF/CNPJ': self.cliente['cnpjcpf'],
        'ITENS': '',
        }
        lista_itens_nota = [json_nota]

        if len(self.itens) > 0:
            for item_nota in self.itens:
                string_item = {
                'SEQ': self.get_sequencial(item_nota),
                'Descricao': item_nota['descricao'],
                'Quantidade': item_nota['quantidade'],
                'ValorUnitario': item_nota['valorUnitario'],
                'ValorItem': item_nota['valorItem']
                }
                lista_itens_nota.append(string_item)

        string_final = {
            'Valor total': self.valorNota
        }
        lista_itens_nota.append(string_final)
        return lista_itens_nota


class ItemNotaFiscal:
    __tablename__ = 'itensnf'

    id = db.Column(db.Integer, primary_key=True)
    sequencial = db.Column(db.Integer)
    quantidade = db.Column(db.Integer)

    produtos = db.relationship("Produto")
    nota_id = db.Column(db.Integer, db.ForeignKey('notas.id'))


    def __init__(self, id, sequencial, quantidade, produto):
        self.id = id
        self.sequencial = sequencial
        self.quantidade = quantidade
        self.produto = produto
        self.descricao = self.produto['descricao']
        self.valorUnitario = self.produto['valorUnitario']
        self.valorItem = float(self.quantidade * self.valorUnitario)

    def to_json(self):
        return {"id": self.id, "sequencial": self.sequencial, "quantidade": self.quantidade,
                "produto": self.produto, "descricao": self.descricao, "valorUnitario": self.valorUnitario,
                "valorItem": self.valorItem}

    def str(self):
        string = f"\nId={self.id} Sequencial={self.sequencial} Quantidade={self.quantidade} Produto={self.descricao} Valor Unitario={self.valorUnitario} Valor Item={self.valorItem}"   
        return string

    def get_sequencial(self):
        seq = str(self.sequencial)
        if len(seq) > 2:
            return seq

        elif len(seq) > 1:
            return f'0{seq}'

        return f'00{seq}'



