let imagens = [
    "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/html5/html5-original.svg",
    "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/css3/css3-original.svg",
    "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/javascript/javascript-original.svg"
];
let indice = 0;

function proximaImagem() {
    indice = (indice + 1) % imagens.length;
    document.getElementById("slider").src = imagens[indice];
}
function imagemAnterior() {
    if(indice >0){
        indice = (indice - 1) % imagens.length;
    document.getElementById("slider").src = imagens[indice];
    }else{
        indice = 3;
        indice = (indice - 1) % imagens.length;
        document.getElementById("slider").src = imagens[indice];
    }
}

setInterval(proximaImagem, 3000); 
