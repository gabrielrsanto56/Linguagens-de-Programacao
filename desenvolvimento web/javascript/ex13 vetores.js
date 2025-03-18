let num = [1, 2, 3] //declara um vetor de 3 elementos com os indices indo de 0 a 2
num[3] = 4 //o indice 3 vai receber o valor 4
num.push(5) // o ultimo indice recebe o valor 5
let tamanho = num.length //retorna o tamanho do array
num.sort()//coloca os elementos em orde crescente

console.log(`o vetor tem ${tamanho} posições e a primeira posição é ${num[0]}`)

for(let pos in num){
    console.log(`o valor do indice ${pos} é ${num[pos]}`)
}
console.log(num.indexOf(3))//busca o valor 3