/* dropdown.js handles dropdown menu on signup page 
   They say if you speak her name aloud three times, 
   the Accessibility Wizardress will appear and grant 
   all of your UX wishes!
*/

/* Select the dropdown from the signup page */
let dropdown = document.getElementById('language');

/* Get the list of ISO-639-1 languages & codes */
const language_codes = language_list;

/* Each element of the selection dropdown*/
let dropdownItem = null;

for (let i = 0; i < language_codes.length; i++) {

    /* Bootstrap dropdown expects the elements of be of type 'option' */
    dropdownItem = document.createElement('option');

    /* Search the language codes for the relevant name */
    dropdownItem.textContent = language_codes[i].name;

    /* Now get the appropriate ISO-639 code */
    dropdownItem.value = language_codes[i].code;

    /* Add the option element to the dropdown list */
    dropdown.appendChild(dropdownItem);
}

/* Get the code and name from any dropdown element that is clicked */
dropdown.addEventListener('change', event => {
    document.getElementById("symbol").src = "https://unpkg.com/language-icons/icons/" + event.target.value + ".svg";
});