from folhapagamento import FolhaPagamento
from tipomovimento import TipoMovimento
from colaborador import Colaborador
from movimentofolha import MovimentoFolha

# Primeira Questão
FP = FolhaPagamento(9, 2019, 0, 0)

# Segunda Questão
CL01 = Colaborador(100, 'Manoel Claudino', 'Av 13 de Maio 2081', '8867-1020', 'Benfica', '60020-060',
                   '124543556-89', 4500.00)
CL02 = Colaborador(200, 'Carmelina da Silva', 'Avenida dos Expedicionários 1200', '3035-1280', 'Aeroporto', '60530-020',
                   '301789435-54', 2500.00)
CL03 = Colaborador(300, 'Gurmelina Castro Saraiva', 'Av João Pessoa 1020', '3235-1089', 'Damas', '60330090',
                   '350245632-76', 3000.00)

# Terceira Questão
MF01 = MovimentoFolha(CL01, 'Gratificação', 4500.00, 1)
MF02 = MovimentoFolha(CL01, 'Plano Saúde', 1000.00, 1)
MF03 = MovimentoFolha(CL01, 'Pensão', 600.00, 2)
MF04 = MovimentoFolha(CL02, 'Gratificação', 2500.00, 1)
MF05 = MovimentoFolha(CL02, 'Plano Saúde', 1000.00, 1)
MF06 = MovimentoFolha(CL02, 'Faltas', 600.00, 2)
MF07 = MovimentoFolha(CL03, 'Gratificação', 4500.00, 1)
MF08 = MovimentoFolha(CL03, 'Plano Saúde', 1000.00, 1)
MF09 = MovimentoFolha(CL03, 'Pensão', 600.00, 2)

movimentos = [MF01, MF02, MF03, MF04, MF05, MF06, MF07, MF08, MF09]

# Sexta Questão
FP.inserirMovimentos(MF01)
FP.inserirMovimentos(MF02)
FP.inserirMovimentos(MF03)
FP.inserirMovimentos(MF04)
FP.inserirMovimentos(MF05)
FP.inserirMovimentos(MF06)
FP.inserirMovimentos(MF07)
FP.inserirMovimentos(MF08)
FP.inserirMovimentos(MF09)

# Sétima Questão
CL01.inserirMovimentos(MF01)
CL01.inserirMovimentos(MF02)
CL01.inserirMovimentos(MF03)
CL02.inserirMovimentos(MF04)
CL02.inserirMovimentos(MF05)
CL02.inserirMovimentos(MF06)
CL03.inserirMovimentos(MF07)
CL03.inserirMovimentos(MF08)
CL03.inserirMovimentos(MF09)

CL01.calcularSalario()
CL02.calcularSalario()
CL03.calcularSalario()

FP.calcularFolha()
