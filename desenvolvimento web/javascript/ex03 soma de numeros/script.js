var n1 = Number.parseInt(window.prompt("digite um numero ")); //o prompt normalmente é tratado como string, então se deve converter para inteiro
var n2 = Number.parseInt(window.prompt("digite outro numero ")); //pode-se colocar apenas number(n) que o jvascript converte
s = n1 + n2;
window.alert("a soma dos numeros " + n1 + " + " + n2 + "é " + s);