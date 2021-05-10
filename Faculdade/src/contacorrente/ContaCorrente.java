package contacorrente;

public class ContaCorrente {
public String banco;
public String agencia;
public String conta;
public String cliente;
public double saldo;
ContaCorrente(String banco, String agencia, String conta, String
	cliente, double saldo){
		this.banco = banco;
		this.agencia = agencia;
		this.conta = conta;
		this.cliente = cliente;
		this.saldo = saldo;
}
public void fazerSaque(double qtRetirada) {
	double res = saldo - qtRetirada;
	this.saldo = res;
}
public String mostrarDados() {
	String res = "Banco: " + banco + "\nAgência: " + agencia + "\nConta: " + conta + "\nCliente: " + cliente + "\nSaldo: " + saldo;
return res;
}
}