let quantity = document.getElementById("quantity").value;

function increment(){
    quantity++;
    document.getElementById("quantity").value = quantity;
}

function decrement(){
    if(quantity > 1)
    {
        quantity--;
        document.getElementById("quantity").value = quantity;
    }
    
}