/* horscroll.js handles avatar carousel 
   If he had his own heavy metal band, they'd be called:
   "The Fistpumps Of Death!" Also, hi Kera!
*/

/* Select the dropdown from the signup page */
let avatarselect = document.getElementById('carousel');

/* Get the list of ISO-639-1 languages & codes */
//const language_codes = language_list;

/* Each element of the selection dropdown*/
let avatarselectItem = null;
let image = null;

let imgurcodes = ["PVe0Rrj", "mmj6PGK", "Ig3gtUz", "34LbL0J", "gornF3o", "j1VdmLj", "LJJHG7w", "ceMTvvV"];

for (let i = 0; i < imgurcodes.length; i++) {

    /* Bootstrap dropdown expects the elements of be of type 'option' */
    avatarselectItem = document.createElement('carousel-item');

    /* Search the language codes for the relevant name */
    avatarselectItem.className = "d-inline-block w-25";

    /* Now get the appropriate ISO-639 code */
    image = document.createElement('img');
    image.referrerPolicy = "no-referrer"
    image.width = 20;
    image.height = 20;
    image.src = "https://imgur.com/" + imgurcodes[i] + ".png";

    avatarselectItem.appendChild(image);

    /* Add the option element to the dropdown list */
    avatarselect.appendChild(avatarselectItem);
}

/* Get the code and name from any dropdown element that is clicked */
avatarselect.addEventListener('click', event => {
    console.log("hello")
});