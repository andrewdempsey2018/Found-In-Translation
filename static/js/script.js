// Client Side Form Validation is done with the Jquery Validate Plugin
// Credit https://jqueryvalidation.org

// Custom validator methods for the app's specifications

// Uses Regex to define email format
$.validator.methods.email = function( value, element ) {
    return this.optional( element ) || /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test( value );
};

