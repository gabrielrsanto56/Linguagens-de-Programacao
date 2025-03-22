function calculo(){
    var txtn1 = window.document.getElementById("numero1")
    var txtn2 = window.document.getElementById("numero2")
    var resultado = window.document.getElementById("resultado")
    var n1 = Number(txtn1.value)
    var n2 = Number(txtn2.value)
    var s = n1+n2
    resultado.innerHTML = s
}