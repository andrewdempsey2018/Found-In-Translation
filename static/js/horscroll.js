/* horscroll.js handles avatar carousel 
   If he had his own heavy metal band, they'd be called:
   "The Fistpumps Of Death!" Also, hi Kera!
*/

/* Select the avatar carousel from signup page */
let avatarselect = document.getElementById('carousel');

/* We will use these variables to add all of the elements to the carousel*/
let avatarselectItem = null;
let image = null;

/* Our avatars are hosted on imgur, this array holds the unique URL code for each image */
let imgurcodes = ["PVe0Rrj", "mmj6PGK", "Ig3gtUz", "34LbL0J", "gornF3o", "j1VdmLj", "LJJHG7w", "ceMTvvV", "zJOBDqr", "roDWkKX", "EhJOV0E",
    "hDbqrma", "pfUsXVU", "DUW9Laq", "oOzPthq", "t1nnGj9", "OF0xvVW", "g9132Pw", "1cYwGzK", "cztrLBD", "wlwDib1", "yZyoUCZ", "Q9HA3Hd", "OZbX2fo",
    "YIh79Ya", "PsmudlJ", "cnIqGQc", "yK8Vzb7", "XIqjw2E", "hH7auGs", "fIsObzM", "z4Qbyip", "8yB5LaV", "aPkkaTR", "V65zySU", "unZPGYC", "1Uvifmb",
    "db6Jp64", "Wz0Vqph", "OBmfZJx", "avz9FDZ", "rrwVXPg", "vY2QzTV", "t6aDWCA", "deX0CM2", "9YO8mfV", "lu9560a", "U0Elh9h", "21j7bnK", "Xe5nqSf"];

for (let i = 0; i < imgurcodes.length; i++) {

    /* carousels are built from divs with class carousel-item */
    avatarselectItem = document.createElement('div');
    avatarselectItem.classList.add("carousel-item")

    // create radio input for avatar selection
    avatarinput = document.createElement('input');
    avatarinput.setAttribute("type", "radio");
    avatarinput.setAttribute("name", "profile_img");
    avatarinput.className="form-check-input";

    /* set the initial item to active, otherwise just leave it as a standard carousel item */
    if (i == 0) {
        avatarselectItem.classList.add('active')
    // first radio input checked by default
        avatarinput.checked = true
    }

    /* make the appropriate styling preferences for each item */
    image = document.createElement('img');
    image.className = "d-inline-block"
    image.classList.add("w-25")
    image.referrerPolicy = "no-referrer"
    
    /* Grab the approprite image from imgur */
    avatarinput.setAttribute("value", imgurcodes[i])
    image.src = "https://imgur.com/" + imgurcodes[i] + ".png";

    /* Add the image to the carousel element */
    avatarselectItem.appendChild(avatarinput)
    avatarselectItem.appendChild(image)

    /* Add the generated carousel item to the carousel */
    avatarselect.appendChild(avatarselectItem);
}

/* get the index of the selected item every time the user clicks the carousel */
$('.carousel').bind('slid.bs.carousel', function (e) {
    var index = $(this).find('.active').index();
    console.log(index);
});