import java.util.Scanner;
public class EstruturaFor {
    public static void main(String[] args){
        int resultado;
        Scanner entrada = new Scanner(System.in);
        int numero = entrada.nextInt();
        for(int i = 1; i<=10; i++){ //para uma interação que vai de 1 até 10 incremente mais um
            resultado = numero*i; //resultado vai dar o numero digitado no teclado vezes a interação
            System.out.printf("%d x %d = %d", numero, i, resultado);
        }
    }
}
