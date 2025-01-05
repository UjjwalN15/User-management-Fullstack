let edit_password = document.getElementById('edit_password');
edit_password.addEventListener('click', function() {
    const edit_password_box = document.querySelector('.edit_password_box');
    const password = document.getElementById('password');
    
    // Get the computed style of the element
    const currentOpacity = window.getComputedStyle(edit_password_box).opacity;

    // Check the computed opacity value and toggle
    if (currentOpacity === '0') {
        edit_password_box.style.opacity = '1';
        edit_password_box.style.zIndex = '1';
        password.style.opacity = '0';
    } else {
        edit_password_box.style.opacity = '0';
        edit_password_box.style.zIndex = '-10';
        password.style.opacity = '1';
    }
});





const new_password = document.getElementById('new_password');
const confirm_password = document.getElementById('confirm_password');
const change_profile_form = document.getElementById('change_profile_form');

change_profile_form.addEventListener('submit', (event) => {
    if (new_password.value !== confirm_password.value) {
        alert("Passwords do not match");
        event.preventDefault(); // Prevent form submission
    }
});

