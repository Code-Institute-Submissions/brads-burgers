var cart = document.querySelector('#cart');
var total = document.querySelector('#total');

function addDrink(pid){
    drinkId = '#dri' + pid;
    var name = document.querySelector(drinkId).innerHTML;
    priceId = '#pri' + pid;
    var price = document.querySelector(priceId).innerHTML;
    cart.innerHTML += '<li>'+ name + ': ' + price + '</li>';
}