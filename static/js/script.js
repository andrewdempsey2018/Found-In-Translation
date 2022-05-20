// Client Side Form Validation is done with the Jquery Validate Plugin
// Credit https://jqueryvalidation.org

// Custom validator methods for the app's specifications

// Uses Regex to define email format
$.validator.methods.email = function( value, element ) {
    return this.optional( element ) || /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test( value );
};

// Calls the validate method on the signup form
$().ready(function() {
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
                required,
            },
            language: {
                required,
            }

        },

})
