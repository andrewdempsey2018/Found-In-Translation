/* dropdown.js handles dropdown menu on signup page 
   They say if you speak her name aloud three times, 
   the Accessibility Wizardress will appear and grant 
   all of your UX wishes!
*/

let dropdown = document.getElementById('language');

//dropdown.length = 0;
//let defaultOption = document.createElement('option');
//defaultOption.text = 'no language selected';

//dropdown.add(defaultOption);
//dropdown.selectedIndex = 0;

const language_codes = language_list;

let dropdownItem = null;
let image = null;

for (let i = 0; i < language_codes.length; i++) {

    dropdownItem = document.createElement('option');
    //image = document.createElement('img');



    //dropdownItem.className = 'dropdown-item';
    dropdownItem.textContent = language_codes[i].name;
    dropdownItem.value = language_codes[i].code;


    //image.src = "https://unpkg.com/language-icons/icons/" + language_codes[i].code + ".svg";
    //image.width = 30;
    //image.height = 30;
    //dropdownItem.appendChild(image);

    dropdown.appendChild(dropdownItem);
}

dropdown.addEventListener('change', event => {
    console.log(event.target.value);
});