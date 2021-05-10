package pessoajava;

public class PessoaEncapsulamento{

private String nome;
private String nascimento;
private String endereco;

PessoaEncapsulamento(String nome, String nascimento, String endereco){

this.nome = nome;
this.nascimento = nascimento;
this.endereco = endereco;
}
public void setNome (String nome){
this.nome = nome;
}
public String getNome () {
return nome;
}
public void setNascimento (String nascimento){
this.nascimento = nascimento;
}
public String getNascimento () {
return nascimento;
}
public void setEndereco (String endereco) {
this.endereco = endereco;
}
public String getEndereco () {
return endereco;
}
public String print(){ 
String dados;
dados = "Nome: " + (String) nome + "\nData de nascimento: " +
(String) nascimento + "\nEndereço: " + (String) endereco;
return dados;
}
public static void main(String[] args){
PessoaJava pessoa1 = new PessoaJava("Israel", "30/09/2002", "R.C Um, 254, Vila Velha");
PessoaJava pessoa2 = new PessoaJava("Pedro", "27/03/1995", "R. B, 202, Quintino Cunha");
System.out.println("Nome: " + pessoa1.nome + "\nData de nascimento: " + pessoa1.nascimento + "\nEndereço: " + pessoa1.endereco + "\n");
System.out.println(pessoa2.print());
}
}