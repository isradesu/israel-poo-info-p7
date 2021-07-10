from flask import Flask, Response, request
from models.models import Cliente, Produto, NotaFiscal, ItemNotaFiscal
import json


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = True

cliente_list = [
    Cliente(1, 'Israel', 100, '56366574495', 'P. Física'),
    Cliente(2, 'Vitoria', 200, '12345678987', 'P. Jurídica')
]

produto_list = [
    Produto(1, 10, 'Leite', 5.50),
    Produto(2, 20, 'Ovo', 1.00),
    Produto(3, 30, 'Peixe', 15.00)
]

nota_list = [
    NotaFiscal(1, 1, cliente_list[0].to_json()),
    NotaFiscal(2, 2, cliente_list[1].to_json())
]

item_list = [
    ItemNotaFiscal(1, 1, 3, produto_list[0].to_json()),
    ItemNotaFiscal(2, 2, 8, produto_list[1].to_json()),
    ItemNotaFiscal(3, 3, 24, produto_list[2].to_json())
]


# Ler todos os clientes
@app.route("/clientes", methods=["GET"])
def ler_clientes():
    clientes_json = [cliente.to_json() for cliente in cliente_list]
    return gera_response(200, "clientes", clientes_json)


# Ler um cliente
@app.route("/cliente/<id>", methods=["GET"])
def ler_cliente(id):

    for cliente in cliente_list:
        if str(cliente.id) == str(id):
            cliente_objeto = cliente
            cliente_json = cliente_objeto.to_json()

            return gera_response(200, "cliente", cliente_json)


# Criar cliente
@app.route("/cliente", methods=["POST"])
def criar_cliente():
    body = request.get_json()

    try:
        cliente = Cliente(id=body["id"], nome=body["nome"], codigo=body["codigo"],
                          cnpjcpf=body["cnpjcpf"], tipo=body["tipo"])

        cliente_list.append(cliente)

        return gera_response(201, "cliente", cliente.to_json(), "Criado com sucesso")
    except Exception as e:
        print('Erro', e)
        return gera_response(400, "cliente", {}, "Você está sendo hackeado")


#Atualizar Cliente
@app.route("/cliente/<id>", methods=["PUT"])
def atualizar_cliente(id):
    cliente_objeto = None
    for cliente in cliente_list:
        if str(id) == str(cliente.id):
            cliente_objeto = cliente
    body = request.get_json()

    try:
        if 'id' in body:
            cliente_objeto.id = body['id']
        if 'nome' in body:
            cliente_objeto.nome = body['nome']
        if 'codigo' in body:
            cliente_objeto.codigo = body['codigo']
        if 'cnpjcpf' in body:
            cliente_objeto.cnpjcpf = body['cnpjcpf']
        if 'tipo' in body:
            cliente_objeto.tipo = body['tipo']

        cliente_list.append(cliente_objeto)
        return gera_response(200, "cliente", cliente_objeto.to_json(), "Cliente atualizado!")

    except Exception as e:
        print('Erro', e)
        return gera_response(400, "cliente", {}, "Você está sendo hackeado")


# Deletar CLiente
@app.route("/cliente/<id>", methods=["DELETE"])
def deletar_cliente(id):
    try:
        cliente_objeto = None
        for cliente in cliente_list:
            if str(id) == str(cliente.id):
                cliente_objeto = cliente

        for posicao_cliente in range(0, len(cliente_list)):
            if cliente_list[posicao_cliente] == cliente_objeto:
                del(cliente_list[posicao_cliente])

        return gera_response(200, "cliente", cliente_objeto.to_json(), "Cliente deletado!")

    except Exception as e:
        print('Erro', e)
        return gera_response(400, "cliente", {}, "Você está sendo hackeado")


# Selecionar todos os produtos
@app.route("/produtos", methods=["GET"])
def seleciona_produtos():
    produtos_json = [produto.to_json() for produto in produto_list]

    return gera_response(200, "produtos", produtos_json)


# Selecionar um produto
@app.route("/produto/<id>", methods=["GET"])
def selecionar_produto(id):
    produto_objeto = None
    for produto in produto_list:
        if str(id) == str(produto.id):
            produto_objeto = produto
    produto_json = produto_objeto.to_json()

    return gera_response(200, "produto", produto_json)



# Criar produto
@app.route("/produto", methods=["POST"])
def criar_produto():
    body = request.get_json()

    try:
        produto = Produto(id=body["id"], codigo=body["codigo"],
                          descricao=body["descricao"], valorUnitario=body["valorUnitario"])

        produto_list.append(produto)

        return gera_response(201, "produto", produto.to_json(), "Criado com sucesso")
    except Exception as e:
        print('Erro', e)
        return gera_response(400, "produto", {}, "Você está sendo hackeado")


# Atualizar produto
@app.route("/produto/<id>", methods=["PUT"])
def atualizar_produto(id):
    produto_objeto = None
    for produto in produto_list:
        if str(id) == str(produto.id):
            produto_objeto = produto
    body = request.get_json()

    try:
        if 'id' in body:
            produto_objeto.id = body['id']
        if 'codigo' in body:
            produto_objeto.codigo = body['codigo']
        if 'descricao' in body:
            produto_objeto.descricao = body['descricao']
        if 'valorUnitario' in body:
            produto_objeto.valorUnitario = body['valorUnitario']

        produto_list.append(produto_objeto)
        return gera_response(200, "produto", produto_objeto.to_json(), "Atualizado com sucesso")
    except Exception as e:
        print('Erro', e)
        return gera_response(400, "produto", {}, "Erro ao atualizar")

# Deletar produto
@app.route("/produto/<id>", methods=["DELETE"])
def deletar_produto(id):
    try:
        produto_objeto = None
        for produto in produto_list:
            if str(id) == str(produto.id):
                produto_objeto = produto

        for posicao_produto in range(0, len(produto_list)):
            if produto_list[posicao_produto] == produto_objeto:
                del (produto_list[posicao_produto])

        return gera_response(200, "produto", produto_objeto.to_json(), "Produto deletado!")

    except Exception as e:
        print('Erro', e)
        return gera_response(400, "produto", {}, "Você está sendo hackeado")


# Ler todas as notas
@app.route("/notas", methods=["GET"])
def ler_notas():
    notas_json = [nota.to_json() for nota in nota_list]
    return gera_response(200, "notas", notas_json)


# Ler uma nota
@app.route("/nota/<id>", methods=["GET"])
def ler_nota(id):
    for nota in nota_list:
        if str(nota.id) == str(id):
            nota_objeto = nota
            nota_json = nota_objeto.to_json()

            return gera_response(200, "nota", nota_json)


# Criar nota
@app.route("/nota", methods=["POST"])
def criar_nota():
    body = request.get_json()

    try:
        nota = NotaFiscal(id=body["id"],
                          codigo=body["codigo"],
                          cliente=body["cliente"],
                          lista_itens=body['itens'])

        nota_list.append(nota)

        return gera_response(201, "nota", nota.to_json(), "Nota cadastrada!")
    except Exception as e:
        print('Erro', e)
        return gera_response(400, "nota", {}, "Falha ao criar")


# Atualizar nota
@app.route("/nota/<id>", methods=["PUT"])
def atualizar_nota(id):
    nota_objeto = None
    for nota in nota_list:
        if str(id) == str(nota.id):
            nota_objeto = nota
    body = request.get_json()

    try:
        if 'id' in body:
            nota_objeto.id = body['id']
        if 'codigo' in body:
            nota_objeto.codigo = body['codigo']
        if 'descricao' in body:
            nota_objeto.cliente = body['cliente']
        if 'valorUnitario' in body:
            nota_objeto.lista_itens = body['itens']

        nota_list.append(nota_objeto)
        return gera_response(200, "nota", nota_objeto.to_json(), "Nota atualizada!")
    except Exception as e:
        print('Erro', e)
        return gera_response(400, "nota", {}, "Erro ao atualizar")


# Deletar nota
@app.route("/nota/<id>", methods=["DELETE"])
def deletar_nota(id):
    try:
        nota_objeto = None
        for nota in nota_list:
            if str(id) == str(nota.id):
                nota_objeto = nota

        for posicao_nota in range(0, len(nota_list)):
            if nota_list[posicao_nota] == nota_objeto:
                del (nota_list[posicao_nota])

        return gera_response(200, "nota", nota_objeto.to_json(), "Nota deletada!")

    except Exception as e:
        print('Erro', e)
        return gera_response(400, "produto", {}, "Você está sendo hackeado")


# Calcular nota
@app.route("/calculanf/<id>", methods=["GET"])
def calcular_nota(id):
    try:
        nota_objeto = None
        for nota in nota_list:
            if str(id) == str(nota.id):
                nota_objeto = nota

        total_nota = nota_objeto.calcular_total_nota(True)

        return gera_response(200, "calculanf", f'Total: {total_nota}', "Calculado com sucesso")
    except Exception as e:
        print('Erro', e)
        return gera_response(400, "calculanf", {}, "Falha ao calcular")


# Imprimir nota
@app.route("/imprimenf/<id>", methods=["GET"])
def imprime_nota(id):
    try:
        nota_objeto = None
        for nota in nota_list:
            if str(id) == str(nota.id):
                nota_objeto = nota
        nota_objeto.calcular_total_nota()
        nota_impressa = nota_objeto.imprimir_nota_fiscal()

        return gera_response(200, "imprimenf", nota_impressa, "Impressão realizada com sucesso!")
    except Exception as e:
        print('Erro', e)
        return gera_response(400, "imprimenf", {}, "Falha ao imprimir")


# Selecionar todos os itens
@app.route("/itens", methods=["GET"])
def ler_itens():
    itens_json = [item.to_json() for item in item_list]
    return gera_response(200, "notas", itens_json)


# Selecionar um item
@app.route("/item/<id>", methods=["GET"])
def ler_item(id):
    for item in item_list:
        if str(item.id) == str(id):
            item_objeto = item
            item_json = item_objeto.to_json()

            return gera_response(200, "item", item_json)


# Cadastrar um item
@app.route("/item/", methods=["POST"])
def criar_item():
    body = request.get_json()

    try:
        item = ItemNotaFiscal(id=body["id"],
                              sequencial=body["sequencial"],
                              quantidade=body["quantidade"],
                              produto=body['produto'])

        item_list.append(item)

        return gera_response(201, "item", item.to_json(), "item cadastrado!")
    except Exception as e:
        print('Erro', e)
        return gera_response(400, "item", {}, "Falha ao criar")


# Atualizar item
@app.route("/item/<id>", methods=["PUT"])
def atualizar_item(id):
    item_objeto = None
    for item in item_list:
        if str(id) == str(item.id):
            item_objeto = item
    body = request.get_json()

    try:
        if 'id' in body:
            item_objeto.id = body['id']
        if 'sequencial' in body:
            item_objeto.sequencial = body['sequencial']
        if 'quantidade' in body:
            item_objeto.quantidade = body['quantidade']
        if 'produto' in body:
            item_objeto.produto = body['produto']

        item_list.append(item_objeto)
        return gera_response(200, "item", item_objeto.to_json(), "Item atualizado!")
    except Exception as e:
        print('Erro', e)
        return gera_response(400, "item", {}, "Erro ao atualizar")


# Deletar nota
@app.route("/item/<id>", methods=["DELETE"])
def deletar_item(id):
    try:
        item_objeto = None
        for item in item_list:
            if str(id) == str(item.id):
                item_objeto = item

        for posicao_item in range(0, len(item_list)):
            if item_list[posicao_item] == item_objeto:
                del (item_list[posicao_item])

        return gera_response(200, "nota", item_objeto.to_json(), "Item deletado!")

    except Exception as e:
        print('Erro', e)
        return gera_response(400, "produto", {}, "Você está sendo hackeado")


# Método retirado da Aula de Crud com o Programando com Roger
def gera_response(status, nome_do_conteudo, conteudo, mensagem=False):
    body = {}
    body[nome_do_conteudo] = conteudo

    if mensagem:
        body["mensagem"] = mensagem

    return Response(json.dumps(body), status=status, mimetype="application/json")
