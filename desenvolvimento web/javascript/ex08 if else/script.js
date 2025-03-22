function verificaVelocidade(){
    var txtvelocidade = document.getElementById("velocidade")
    var velociade = Number(txtvelocidade.value)
    var texto = document.getElementById("texto")
    if(velociade > 80){
        texto.innerHTML = "multado"
    }else{
        texto.innerHTML = "velocidade compativel"
    }
}