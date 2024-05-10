document.getElementById('registrationForm').addEventListener('submit', function(event) {
    var password = document.getElementById('pass1').value;
    var confirmPassword = document.getElementById('pass2').value;
    var errorMessage = document.getElementById('error_message');

    if(password != confirmPassword) {
        event.preventDefault();
        errorMessage.style.display = 'block';
    } else {
        errorMessage.style.display = 'none';
    }
});