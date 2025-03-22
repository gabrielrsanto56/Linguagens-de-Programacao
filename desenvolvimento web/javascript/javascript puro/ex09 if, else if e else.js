var hora = new Date()
var horaAtual = hora.getHours()
var minuto = hora.getMinutes()
if(horaAtual < 12){
    console.log(`bom dia, são ${horaAtual}:${minuto} horas`)
}else if(horaAtual <= 18){
    console.log(`boa tarde, são ${horaAtual}:${minuto} horas`)
}else{
    console.log(`boa noite, são ${horaAtual}:${minuto} horas`)
}