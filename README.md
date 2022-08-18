# **FOUND IN TRANSLATION**

![Found in Translation site shown on multiple screen sizes](static/images/site-responsive.png)

![GitHub last commit](https://img.shields.io/github/last-commit/andrewdempsey2018/Found-In-Translation?color=red&style=for-the-badge)
![GitHub contributors](https://img.shields.io/github/contributors/andrewdempsey2018/Found-In-Translation?color=orange&style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/andrewdempsey2018/Found-In-Translation?color=yellow&style=for-the-badge)
![GitHub top language](https://img.shields.io/github/languages/top/andrewdempsey2018/Found-In-Translation?color=green&style=for-the-badge)

Found in Translation -Find your tribe, lose the language barrier!

Found in Translation may well be the first online community that has overcome the language barrier, allowing its users to spark up conversations with anyone from all over the globe!

Gone are the days of having to use annoying plugin translators - Found in Translation does all the hard work for you behind the scenes, leaving you with more time to make connections!

Simply create an account and chose your language (over 160 to choose from). You can then create and read posts in your chosen language, regardless of what language they were originally written in! Theres a topic for everyone at Found in Translation!

View deployed site: [Found in Translation](https://foundintranslationsodaci.herokuapp.com/)

- - -

## **Table of Contents**

1. [UX Development](#ux-development)
    * [PROJECT GOAL](#project-goal)

    * [USER STORIES](#user-stories)
        * [New User](#new-user)
        * [Registered Users/Returning Users](#registered-user-or-returning-users)
        * [Admin User](#admin-user)
        * [Target Audience](#target-audience)

    * [DESIGN](#design)
        * [Colour Scheme](#colour-scheme)
        * [Typography](#typography)
        * [Imagery](#imagery)
        * [Wireframes](#wireframes)
        * [Database Structure](#database-structure)

2. [Features](#features)  
    * [EXISTING FEATURES](#existing-features)
        * [General Features On All Pages](#general-features-on-all-pages)
        * [Features Of Each Page](#features-of-each-page)
        * [Features To Implement In Future](#features-to-implement-in-future)
        * [Privacy Page and Terms and Conditions Page](#privacy-page-and-terms-and-conditions-page)

3. [Technology Used](#technology-used)  
    * [Language Used](#language-used)
    * [Frameworks,libraries and Program Used](#frameworkslibraries-and-program-used)
    * [ISO 639-1 Language Codes](#iso-639)  
    * [Google Translation API](#google-translation-api)

4. [Testing](#testing)
    * [TESTING.md](#testing)

5. [Deployment](#deployment)  
    * [Deployment Heroku](#deployment-to-heroku)
    * [Steps To Use This Project](#steps-to-use-this-project)  

6. [Credits](#credits)  
    * [Content](#content)
    * [Media](#media)  

7. [Acknowledgements](#acknowledgements)  
    * [Team Members](#team-members)

- - -

## **UX Development**

### **PROJECT GOAL**

Found-In Translation is an online discussion board that aims to bridge individuals' language gaps. Its mission is to connect individuals from all over the world to discuss and share real-life experiences without any barriers.People of all ages are targeted by Found in Translation.

The user can easily search for a topic, language, or discussion to view its content and leave a comment; however, in order to add/edit a discussion, the user must login/register to the site. The site's goal is for users to be able to perform basic CRUD functionality (Create, Read, Update, and Delete) and interact with it intuitively while having a positive experience.  

## **User Stories**

### **New User**

* As a first time user, I want to be able to easily navigate the site
* As a first time user, I want to be able to sign up to the site and create a profile
* As a first time user, I want to receive feedback that my profile has successfully been created

### **Registered User/Returning Users**

* As a returning/registered user, I want to be able to log in to my account
* As a returning/registered user, I want to be able to create a new post
* As a returning/registered user, I want to be able to flag offensive posts
* As a returning/registered user, I want to be able to view all Threads
* As a returning/registered user, I want to be able to reply to posts

### **Admin User**

* As an admin user, I want to be able to view flagged posts.
* As an admin user, I want to be able to delete messages that have been flagged that are offensive.
* As an admin user, I want to be able to unflag posts that are not offensive.

### **Target Audience**

Found in Translation allows anyone to connect with others around the world with no language barrier. This means that the world is our target audience.

## **Design**

### **Colour Scheme**

Colors have a significant effect on our mood, through them, we simulate a series of emotions. Our main objective in choosing our color theme was to transmit peace, happiness and harmony.

![Found in Translation Color Palette](documentation/color-palette.png)

### **Typography**

As the main focus of the site is the messages that people are sending, we have only used one font throughout the site to prevent users becoming overwhelmed.

Quicksand was imported from google fonts. It is a sans-serif font which is accessible friendly.

![Quicksand Font](documentation/font_quicksand.png)

### **Wireframes**

The entire site's wireframe was done using [Figma](https://www.figma.com).This depicts the site on a desktop and a mobile device.

![Wireframe for 404 error](documentation/wireframes/404error.png)
![Wireframe for All threads page ](documentation/wireframes/allthreadspage.png)
![Wireframe for Home page ](documentation/wireframes/indexpage.png)
![Wireframe for Individual thread page ](documentation/wireframes/individualthread.png)
![Wireframe for Login page ](documentation/wireframes/loginpage.png)
![Wireframe for Log Out page ](documentation/wireframes/logoutpage.png)
![Wireframe for Profile page ](documentation/wireframes/signuppage.png)
![Wireframe for Sign Up page ](documentation/wireframes/startnewthread.png)

### **Database Structure**

MongoDB was chosen as the database for this project due to the flexibility it offers for non-relational data.

[Diagram.io](https://dbdiagram.io/home) was used to create the data schema for this project. Our schema had three collections:

* Users
* Threads
* Posts

![Database structure](documentation/database-schema.png)  

## **Features**

### **General Features On All Pages**

The site has been designed to be fully responsive, from mobile all the way up to desktop.

#### **Navbar**

The site has a fully responsive navbar.

![Navbar desktop](documentation/navbar-desktop.png)
![Navbar Small Screens](documentation/navbar-small.png)

#### **Footer**

The site has a fully responsive footer. The footer contains links to social media, the privacy policy and terms and conditions pages. It also features a call to action button asking users to join now.

![Footer Large](documentation/footer-large.png)
![Footer Small](documentation/footer-small.png)

#### **Favicon**

The Favicon was created using [Favicon.io](https://favicon.io/).
We have chosen this image as our site logo and have also used it as our favicon as it brings brand cohesion to the site.

![Favicon](documentation/rm-favicon.png)

####  **Site Logo**

We have chosen this image as our site logo as we feel it displays the core principle of our site in an icon which allows the site logo to be understood by anyone, regardless of their language. The image shows a globe with two speech bubbles, each with a different language character.

![Logo](documentation/rm-logo.png)

### **Privacy Page and Terms and Conditions Page**

We are aware that as we are asking users to create a username and a password to allow full interactivity with our site we need to also be mindful of how we are storing the data to ensure it remains private and secure. In the UK it is also important to be GDPR compliant.

As this site was created as part of a hackathon project, the privacy and terms & conditions pages have been created to demonstrate an understanding that we, as the site creators and custodians of peoples personal data have taken consideration about this and have provided the user with a terms and conditions and privacy policy page which lets the users know how their data is being used.
These documents were created on [RocketLawyer.com](https://www.rocketlawyer.com/gb/en?gclid=Cj0KCQjwm6KUBhC3ARIsACIwxBg54TtP8b529a5qduEkHY7u-D1hKr_I6qvoCuqtQM6VhwDUdpnR6fsaApToEALw_wcB), a site that creates documents.

As the site has been created for educational purposes only, please note that the following documents would not be legally binding, they are purely to demonstrate an understanding of the topic. We would like to however ensure users that all measures have been taken to ensure any data entered into the site is secure.

## **Technology Used**

### **iso-639**

To provide users with translated text on the pages, [ISO 639-1 codes](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) were used to classify the users’ language on the page. When a user signs up, they can choose a country to be their default language on their account. If a user replies to or starts a thread, the text posted will be translated.

### **Language Icons**

We wanted to be able to display an icon for a language, however while researching we didn't feel that we could use country flags, as someone may speak a language, but not identify with the country flag for that language, as many areas can speak the same language. We eventually came across [Language Icons by Anand Chowdhary](https://github.com/AnandChowdhary/language-icons) which fit our thinking perfectly.

### **Google translation api**

Translation API

Translation API Basic uses Google’s neural machine translation technology to instantly translate texts into more than one hundred languages. Translation API Advanced offers the same fast, dynamic results you get with Basic and additional customization features. Customization matters for domain- and context-specific terms or phrases, and formatted document translation.

Before you can start using the Cloud Translation API, you must have a project that has the Cloud Translation API enabled, and you must have a private key with the appropriate credentials. You can also install client libraries for common programming languages to help you make calls to the API. For more information, see the Setup page.

We created a class that takes two arguments, 'target' and 'text'. The target is the ISO 639 code of the language desired. The test is any text that we wish to translate. The two arguments are sent to the Google Translate API as a POST request. We hit Google's endpoint which returns a dictionary with the appropriate translated text.

If you wish to have further information about how we acheived the translation results, feel free to contact the team via Slack.

### **Language Used**

HTML, CSS, Javascript, Python, JQuery, Bootstrap, Heroku

### Frameworks, libraries & Program Used

* [Figma](https://www.figma.com/) - To create wireframes.
* [Git](https://git-scm.com/) - For version control.
* [Github](https://github.com/)- To save and store the files for the website.
* [Jinja](https://jinja.palletsprojects.com/en/3.1.x/) - Templating engine
* [Google Cloud Translate API](https://console.cloud.google.com/apis/library/translate.googleapis.com?project=wp-mail-smtp-322517) - Controls the translation of the site into the chosen language. Please see ** section for more information on this API
* [Bootstrap V5.2](https://getbootstrap.com/) - Used as CSS Framework
* [Bootstrap Icons V1.8.2](https://icons.getbootstrap.com/) - Used for the sites iconography
* [Google DevTools](https://developers.google.com/web/tools) - To troubleshoot and test features, solve issues with responsiveness and styling.
* [Birme](https://www.birme.net/) To compress images and convert to webP format.
* [Favicon.io](https://favicon.io/) To create favicon.
* [Am I Responsive?](http://ami.responsivedesign.is/) To show the website image on a range of devices.
* [Shields.io](https://shields.io/) To add badges to the README
* [Heroku](https://www.heroku.com/) To deploy the project.
* [Flask](https://pypi.org/project/Flask/) - Web Application Framework
* [MongoDB](https://www.mongodb.com/) - Non Relational Database
* [Google fonts](https://fonts.google.com/) - used to import the font used on the site.
* [TinyPNG](https://tinypng.com/) - used to compress images in the readme

## **Testing**

Please view our [TESTING.md](#testing) file for more information on the testing undertaken.

## **Deployment**

### **Deployment Heroku**

This project was deployed using Heroku:

1. Create a new app with the name found-in-translation.
2. Linked the found-in-translation app to its Github repository.
3. Verify that the project has an up to date Procfile and requirements.txt
4. Push the project to the Heroku remote.
5. Set the SECRET_KEY environmental variable in the Heroku config vars.
6. Set the IP to 0.0.0.0 and the PORT to 5000 in the Heroku config vars.
7. Set the MONGO_URI environmental variable in the Heroku config vars.
8. Restart all dynos.
9. Open the app on Heroku and check to ensure that it's working correctly.

### **How to clone**

1. Under the repository name on GitHub, click Clone or download.
2. In the Clone with HTTPs section, click the icon beside the URL to copy the clone URL for the repository.
3. Change the current working directory to the location where you want the cloned directory to be made.
4. Type git clone, and then paste the URL you copied in Step 2.
5. Press Enter. Your local clone will be created.
6. Set up a virtual environment.
7. Install the packages in requirements.txt by typing pip3 install -r requirements.txt in the CLI.
8. Set the IP address to 127.0.0.1 and the PORT to 5000.

### **How to Fork**

To fork the repository:

Log in (or sign up) to Github.
Go to the repository for this project, [Found in Translation](https://github.com/andrewdempsey2018/Found-In-Translation)
Click the Fork button in the top right corner.

## **Credits**

### **Media**

* [Home Page Hero Image](https://www.rawpixel.com/image/409810/free-illustration-image-connection-community-cartoon-person)  

  ![Home Page Hero](documentation/hero.png)

* [Error Page Hero Image](https://www.rawpixel.com/image/409809/free-illustration-image-guide-career-cartoon)

  ![Error Page Hero](documentation/hero1.png)

* [Logo and Favicon Image](https://www.flaticon.com/free-icons/language), sourced from Flatiron, created by Freepik

* [Avatars](https://speckyboy.com/free-cute-user-avatar-icon-set/), sourced from specyboy

  ![Logo](documentation/rm-logo.png)
  ![Favicon](documentation/rm-favicon.png)

## **Acknowledgements**

* Thank you to Code Institute and Soda Social for putting together this hackathon - we have had an amazing time taking part.
* A huge thank you to our families for once again putting up with us disappearing for another weeekend filled with hackathon fun.

## **Team Members**

* Andrew Dempsey [LinkedIn](https://www.linkedin.com/in/andrew-dempsey-20ab40180/) | [Github](https://github.com/andrewdempsey2018)

"_Thank you to Trust in Soda and Code Institute for giving me this wonderful opportunity to take part in Hackathon: May 22. The event was great fun, very helpful to me and the projects that all the teams produced were simply amazing! However, the best part of the past few days was working as part of team 'Gladiator' and making some AWESOME new friends!_"

* Cristian B. [LinkedIn](https://www.linkedin.com/in/cristianbuca/) | [Github](https://github.com/CristianBuca)

"_I was looking forward to participating in a Soda/Code Institute Hackaton ever since I started my development course but did not have the courage to register until after I finished studying. This was a great experience with an amazing team. Everyone pushed themselves for this coding sprint to deliver a project that we can be proud of!_"

* Didi [LinkedIn](https://www.linkedin.com/in/onyema-onyejekwe-492128102/) | [Github](https://github.com/Didisimmons)

"_Participating in the May 2022 Hackathon organized by Trust in Soda in collaboration with Code Institute was an incredible experience. Thank you for this wonderful opportunity; the last few days have been simply incredible; I got to work with and learn from talented individuals, build my network skills, improve my collaborative skills, and have fun with my new friends while working on our exciting project. I'm looking forward to participating in many more hackathons in the future._"

* Kera Cudmore [LinkedIn](https://www.linkedin.com/in/keracudmore/) | [Github](https://github.com/kera-cudmore)

"_Another whirlwind Hackathon weekend completed - spent creating an amazing site with some truly talented people! I love being able to take part in these events (Thanks Code Institute & Soda Social for putting this event together 😊), theres nothing better than being part of a community of people who are so generous with sharing their knowledge. Thanks Team Gladiator - you've been amazing!_"

* Paula Silva [LinkedIn](https://www.linkedin.com/in/paulacgsilva) | [Github](https://github.com/paulasdev)

"_Fantastic experience participating in my first Hackathon with Code Institute & Trust Soda. I had support from my entire Gladiator team and it was a great opportunity to gain more knowledge for my journey._"
