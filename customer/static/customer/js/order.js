var bcart = document.querySelector('#bcart');
var btotal = document.querySelector('#btotal');

function addBurger(bid) {
    burgerId = '#bur' + bid;
    var name = document.querySelector(burgerId).innerHTML;

    burgerId = '#burger' + bid;
    var price = document.querySelector(burgerId).innerHTML;

    btotal.innerHTML = 'Total: € ' + total;
    bcart.innerHTML += '<li>'+ name + ' ' + price +'</li>';
}