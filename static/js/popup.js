// Show the modal
// static/js/popup.js

function showModal() {
    document.getElementById('authModal').style.display = 'block';
}

function closeModal() {
    document.getElementById('authModal').style.display = 'none';
}


// Show Sign In form
function showSignIn() {
    document.getElementById('signInForm').style.display = 'block';
    document.getElementById('forgetPasswordForm').style.display = 'none';
    document.getElementById('signUpForm').style.display = 'none';
}

// Show Forget Password form
function showForgetPassword() {
    document.getElementById('signInForm').style.display = 'none';
    document.getElementById('forgetPasswordForm').style.display = 'block';
    document.getElementById('signUpForm').style.display = 'none';
}

// Show Sign Up form
function showSignUp() {
    document.getElementById('signInForm').style.display = 'none';
    document.getElementById('forgetPasswordForm').style.display = 'none';
    document.getElementById('signUpForm').style.display = 'block';
}
