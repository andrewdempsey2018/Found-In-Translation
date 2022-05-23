/* horscroll.js handles avatar carousel 
   If he had his own heavy metal band, they'd be called:
   "The Fistpumps Of Death!" Also, hi Kera!
*/

/* Select the dropdown from the signup page */
let avatarselect = document.getElementById('carousel');
console.log(avatarselect)
/* Get the list of ISO-639-1 languages & codes */
//const language_codes = language_list;

/* Each element of the selection dropdown*/
let avatarselectItem = null;
let image = null;

let imgurcodes = ["PVe0Rrj", "mmj6PGK", "Ig3gtUz", "34LbL0J", "gornF3o", "j1VdmLj", "LJJHG7w", "ceMTvvV", "zJOBDqr", "roDWkKX", "EhJOV0E",
    "hDbqrma", "pfUsXVU", "DUW9Laq", "oOzPthq", "t1nnGj9", "OF0xvVW", "g9132Pw", "1cYwGzK", "cztrLBD", "wlwDib1", "yZyoUCZ", "Q9HA3Hd", "OZbX2fo",
    "YIh79Ya", "PsmudlJ", "cnIqGQc", "yK8Vzb7", "XIqjw2E", "hH7auGs", "fIsObzM", "z4Qbyip", "8yB5LaV", "aPkkaTR", "V65zySU", "unZPGYC", "1Uvifmb",
    "db6Jp64", "Wz0Vqph", "OBmfZJx", "avz9FDZ", "rrwVXPg", "vY2QzTV", "t6aDWCA", "deX0CM2", "9YO8mfV", "lu9560a", "U0Elh9h", "21j7bnK", "Xe5nqSf"];

for (let i = 0; i < imgurcodes.length; i++) {

    /* Bootstrap dropdown expects the elements of be of type 'option' */
    avatarselectItem = document.createElement('div');
    avatarselectItem.classList.add("carousel-item")

    if (i == 0) {
        avatarselectItem.classList.add('active')
    }

    /* Now get the appropriate ISO-639 code */
    image = document.createElement('img');
    image.className = "d-inline-block"
    image.classList.add("w-25")
    image.referrerPolicy = "no-referrer"
    //image.width = 60;
    //image.height = 60;
    image.src = "https://imgur.com/" + imgurcodes[i] + ".png";

    avatarselectItem.appendChild(image)



    /* Add the option element to the dropdown list */
    avatarselect.appendChild(avatarselectItem);
}

$('.carousel').bind('slid.bs.carousel', function (e) {
    var index = $(this).find('.active').index();
    console.log(index);
});