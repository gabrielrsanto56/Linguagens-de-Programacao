package java;
import java.util.Scanner; //importa a biblioteca que faz a leitura da mensagem
public class RecebendoValores {
    Scanner entrada = new Scanner(System.in); //cria um objeto que recebe informações do teclado
    System.out.println("digite seu nome: ");
    String nome = entrada.nextLine(); //atribue a variável nome uma entrada do tipo String
    System.out.printf("muito prazer %s" + nome);
}
