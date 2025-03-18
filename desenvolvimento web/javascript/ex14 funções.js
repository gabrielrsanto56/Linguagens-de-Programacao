function parOuImpar(n){ //declara uma função onde "n" é passado como parâmetro
    if(n%2==0){
        return "par"
    }else{
        return "impar"
    }
}// se o numero passado por parametro for par a função retorna o valor "par", caso contrário retorna "impar"
let numero = parOuImpar(12)
console.log(numero)

//outro exemplo
function soma(a=0, b=0){ //o a e o b recebem 0 por padrão, mas serão alterados com a passagem de parâmetros
    return a+b
}
let resultado = soma(5, 7)
console.log(resultado)