package java;
public class WhileEDo{
    public static void main(String[] args) {
        int num = 10;
        while(num<=100){ //enquanto o numero menor igual a 10
            num +=10; //faz incremento de 10 em 10. Se deve ter muito cuidado para não entrar em um laço de repetição inifita
            System.out.println(num);
        }
        while(num>=10){
            num +=10; //laço de repetição infinito
            System.out.println(num);
        }
        do{
            num+=10;
        }while(num<=100)//faça incremento de 10 em 10 enquanto num for menor igual a 100. O laço do executa pelo menos uma vez
    }
}