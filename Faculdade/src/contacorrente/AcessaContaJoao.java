package contacorrente;

public class AcessaContaJoao extends ContaCorrente {
	
AcessaContaJoao(String banco, String agencia, String conta, String
	cliente, double saldo){
	super(banco,agencia,conta,cliente,saldo);
}
public static void main(String[] args) {
	System.out.println("========================\nDADOS DA CONTA\n========================");
	AcessaContaJoao joao = new AcessaContaJoao("Bradesco", "1032-4","31311-1", "João da Silva", 1000);
	System.out.println(joao.mostrarDados());
	joao.fazerSaque(135);
	System.out.println("========================\nDADOS APÓS SAQUE\n========================");
	System.out.println(joao.mostrarDados());
}
}