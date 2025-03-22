var a = window.document.getElementById('area')
a.addEventListener('click', clicar)
function clicar(){
    a.innerText = 'clicou'
    a.style.background = 'rgb(93, 93, 93)'
}