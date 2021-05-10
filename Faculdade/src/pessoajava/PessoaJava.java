package pessoajava;
public class PessoaJava {

String nome;
String nascimento;
String endereco;

PessoaJava(String nome, String nascimento, String endereco){ 
this.nome = nome;
this.nascimento = nascimento;
this.endereco = endereco;
}
public String print(){
String dados;
dados = "Nome: " + (String) nome + "\nData de nascimento: " + (String) nascimento + "\nEndereço: " + (String) endereco;
return dados;
}
public static void main(String[] args) {
PessoaJava pessoa1 = new PessoaJava("Israel", "30/09/2002", "R.C Um, 254, Vila Velha");
PessoaJava pessoa2 = new PessoaJava("Pedro", "27/03/1995", "R. B, 202, Quintino Cunha");
System.out.println("Nome: " + pessoa1.nome + "\nData de nascimento: " + pessoa1.nascimento + "\nEndereço: " + pessoa1.endereco + "\n");
System.out.println(pessoa2.print()); 
}
}