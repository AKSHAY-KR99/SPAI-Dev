function validateForm() {
    const email = document.getElementById('email');
    const username = document.getElementById('username');
    const firstName = document.getElementById('first_name');
    const lastName = document.getElementById('last_name');
    const state = document.getElementById('state');
    const password = document.getElementById('password');
    const confirmPassword = document.getElementById('confirm_password');

    let emailError = false;
    let usernameError = false;
    let passwordError = false;
    let firstNameError = false;
    let stateError = false;

    let errorCount = 0;

    if ((email == null) || (email == "")) {
        let errorText = document.querySelector("#noneEmail")
        errorText.innerHTML = "*Please provide email"
        errorText.style.visibility = "visible";
        errorCount += 1
    }
    
    if (!email.value.match(/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/)) {
        emailError = true;
        let errorText = document.querySelector("#invalidEmail")
        errorText.innerHTML = "*Please provide valid email id"
        errorText.style.visibility = "visible";
        errorCount += 1
    }

    if (username.value.length < 3) {
        usernameError = true;
        let errorText = document.querySelector("#noneUsername")
        errorText.innerHTML = '* Username must be at least 3 characters long'
        errorText.style.visibility = "visible";
        errorCount += 1
    }

    if ((firstName.value == null)||(firstName.value == "")){
        firstNameError = true;
        let errorText = document.querySelector("#noneFirstName")
        errorText.innerHTML = '* First name cannot be empty!'
        errorText.style.visibility = "visible";
        errorCount += 1
    }

    if (state.value == 'Select state'){
        stateError = true;
        let errorText = document.querySelector("#noneState")
        errorText.innerHTML = '* Select any state'
        errorText.style.visibility = "visible";
        errorCount += 1
    }
    
    if (password.value.length < 8 ||!password.value.match(/^(?=.*[A-Z])(?=.*[a-z])(?=.*[@#_!])/)) {
        passwordError = true;
        let errorText = document.querySelector("#invalidPassword")
        errorText.innerHTML = '* Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, and one of the following special characters: @, #, _,!'
        errorText.style.visibility = "visible";
        errorCount += 1
    }

    if (password.value!== confirmPassword.value) {
        passwordError = true;
        let errorText = document.querySelector("#noneMatch")
        errorText.innerHTML = '* Passwords do not match'
        errorText.style.visibility = "visible";
        errorCount += 1
    }

    if (emailError || usernameError || passwordError || firstNameError || stateError) {
        return false;
    }

    return true;
}

const formResult = validateForm()

if (formResult){
    document.getElementById('myForm').submit()
}