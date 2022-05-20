// Client Side Form Validation is done with the Jquery Validate Plugin
// Credit https://jqueryvalidation.org

// Custom validator methods for the app's specifications

// Uses Regex to define email format
$.validator.methods.email = function( value, element ) {
    return this.optional( element ) || /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test( value );
};

// Calls the validate method on the signup form
$('#signup_form').validate({
    // Validation Rules
    rules: {
        email: {
            required: true,
            email: true,
        },
        username: {
            required: true,
            minlength: 4,
        },
        password: {
            required: true,
        },
        password_conf: {
            required: true,
            equalTo: '#password',
        },
        terms: {
            required: true,
        },
        language: {
            required: true,
        }

    },
    // Custom messages for custom validator method
    messages: {
        username: {
            required: "Please choose a username"
        },
        email: {
            email: "Please enter a valid email address"
        },
        password_conf: {
            equalTo: "Passwords do not match",
        },
        terms: {
            required: "Please accept the terms and conditions to continue"
        },
        language: {
            required: "Please select your preferred language"
        },
    }
});
