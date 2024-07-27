document.getElementById("order-form").addEventListener("submit", function(event) {
    event.preventDefault();
    
    var product = document.getElementById("product").value;
    var quantity = document.getElementById("quantity").value;
    
    // Example: Send order data to server for processing
    console.log("Product: " + product + ", Quantity: " + quantity);
    
    // You can further process the order here (e.g., send it to a backend API)
    
    // Reset form after submission
    document.getElementById("order-form").reset();
});

