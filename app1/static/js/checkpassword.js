document.getElementById('change_password').addEventListener('submit', function(event) {
    var password = document.getElementById('new').value;
    var confirmPassword = document.getElementById('newagain').value;
    var errorMessage = document.getElementById('error_message');

    if(password != confirmPassword) {
        event.preventDefault();
        errorMessage.style.display = 'block';
    } else {
        errorMessage.style.display = 'none';
    }
});