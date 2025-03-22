window.document.write(window.navigator.appName + "<br>")
window.document.write(window.document.URL)
var p1 = document.getElementsByTagName('p')[0]
document.write('<br> Está escrito assim ' + p1.innerText)// innerText replica algo e o innerHTML replica o texto e a formatação
p1.innerText = 'ola'
p1.style.color = 'blue'