package pessoajava;

public class Aluno2 extends PessoaEncapsulamento {
public double nota;
public String turma;
Aluno2(String nome, String nascimento, String endereco, double nota,String turma){
super(nome, nascimento, endereco);
this.nota = nota;
this.turma = turma;
}
public double getNota(){
return nota;
}
public void setNota(double nota){
this.nota = nota;
}
public String getTurma(){
return turma;
}
public void setTurma(String turma){
this.turma = turma;
}
public String print(){
String dados;
dados = getNome() + getNascimento() + getEndereco() + getNota() +
getTurma();
return dados;
}
public static void main(String[] args) {
Aluno aluno1 = new Aluno("Israel Leite", "30/09/2002", "Rua C, 254, Vila Velha, Fortaleza - CE", 10, "P6 de Informática");
System.out.println(aluno1.print());
}
}