var diaSemana = new Date()
var diaAtual = diaSemana.getDay()
switch(diaAtual){
    case 0:
        console.log("domingo")
        break
    case 1:
        console.log("segunda")
        break
    case 2:
        console.log("terça")
        break
    case 3:
        console.log("quartaa")
        break
    case 4:
        console.log("quinta")
        break
    case 5:
        console.log("sexta")
        break
    case 6:
        console.log("sábado")
    default:
        console.log("ERRO!!! DIA INVALIDO")
        break
}