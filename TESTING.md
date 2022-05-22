# Found in Translation -  Testing

Responsive site image to go here  

Visit the deployed site: [Found in Translation](https://foundintranslationsodaci.herokuapp.com/)

- - -

## CONTENTS

* [AUTOMATED TESTING](#AUTOMATED-TESTING)
  * [W3C Validator](#W3C-Validator)
  * [JavaScript Validator](#JavaScript-Validator)
  * [Python Validator](#Python-Validator)
  * [Lighthouse](#Lighthouse)
* [MANUAL TESTING](#MANUAL-TESTING)
  * [Testing User Stories](#Testing-User-Stories)
  * [Full Testing](#Full-Testing)

Testing was ongoing throughout the entire build. We utilised Chrome developer tools whilst building to pinpoint and troubleshoot any issues as we went along.

Each page has been inspected using google chrome developer tools & Firefox inspector tool to ensure that each page is fully responsive on a variety of different screen sizes and devices. We have also physically tested the responsiveness of the site on a number of different devices.

- - -

## AUTOMATED TESTING

### W3C Validator

[W3C](https://validator.w3.org/) was used to validate the HTML on all pages of the website. It was also used to validate the CSS.

* Insert testing results here

- - -

### JavaScript Validator

[jshint](https://jshint.com/) was used to validate the JavaScript.

*  

- - -

### Python Validator

[PEP8](http://pep8online.com/)was used to validate the python files.

* Insert testing results here

- - -

### Lighthouse

I used Lighthouse within the Chrome Developer Tools to test the performance, accessibility, best practices and SEO of the website.

### Desktop Results

### Mobile Results

- - -

## MANUAL TESTING

### Testing User Stories

`First Time Visitors`

| Goals | How are they achieved? |
| :--- | :--- | :--- |
| As a first time user, I want to be able to easily navigate the site | We have made every effort to make navigating the site easy for users, regardless of their language. We have achieved this by using icons to represent links. Links for navigation are included in the navbar.  | :--- |
| As a first time user, I want to be able to sign up to the site and create a profile | Users can create their own profile for the site by using the sign up page. Links to the sign up page are included on the navbar, and there is also a button to redirect users to the sign up page on the 404 page if they are not logged into an account on the site. | :--- |
| As a first time user, I want to receive feedback that my profile has successfully been created | :--- | :--- |

`Registered/Returning Visitors`

|  Goals | How are they achieved? | :--- |
| :--- | :--- | :--- | :--- |
| As a returning/registered user, I want to be able to log in to my account | :--- | :--- | :--- |
| As a returning/registered user, I want to be able to view all Threads | :--- | :--- | :--- |
| As a returning/registered user, I want to be able to create a new post  | :--- | :--- | :--- |
| As a returning/registered user, I want to be able to flag offensive posts | :--- | :--- | :--- |
| As a returning/registered user, I want to be able to reply to posts | :--- | :--- | :--- |
| :--- | :--- | :--- | :--- |

`Admin User`

| Goals | How are they achieved? | :--- |
| :--- | :--- | :--- |
| :--- | :--- | :--- |
| :--- | :--- | :--- |

- - -

### Full Testing

Full testing was performed on the following devices:

* Laptop:
  * Macbook Pro 2021 14 inch screen
* Mobile Devices:
  * iPhone 13 pro.
  * iPhone 11 pro.
  * Phone X.

Each device tested the site using the following browsers:

* Google Chrome
* Safari
* Firefox

Additional testing was taken by friends and family on a variety of devices and screen sizes.  

`Home Page`

Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Navbar - Site logo | Reloads home page | Click logo |  Reloads home page | - |
| Navbar - Site Name | Reloads home page | Click site name | Reloads home page | Pass |
| Navbar - Home Link | Reloads home page | Click home link | Reloads home page | Pass |
| Navbar - Login Link (user not logged in) | Redirect to Login page | Click log in link | Redirected to log in page | Pass |
| Navbar - Sign up Link (user not logged in)  | Redirect to Sign up page | Click sign up link | Redirected to sign up page | Pass |

`Login Page`

Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Navbar - Site logo | Redirects to home page | Click logo |  Redirected to home page | Pass |
| Navbar - Site Name | Redirects to home page | Click site name | Redirected to home page | Pass |
| Navbar - Home Link | Redirects to home page | Click home link | Redirected to home page | Pass |
| Navbar - Login Link (user not logged in) | Reloads Login page | Click log in link | Reloads log in page | Pass |
| Navbar - Sign up Link (user not logged in)  | Redirect to Sign up page | Click sign up link | Redirected to sign up page | Pass |

`Signup Page`

Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Navbar - Site logo | Redirects to home page | Click logo |  Redirects to home page | Pass |
| Navbar - Site Name | Redirects to home page | Click site name | Redirected to home page | Pass |
| Navbar - Home Link | Redirects to home page | Click home link | Redirected to home page | Pass |
| Navbar - Login Link (user not logged in) | Redirect to Login page | Click log in link | Redirected to log in page | Pass |
| Navbar - Sign up Link (user not logged in)  | Reloads Sign up page | Click sign up link | Reloads sign up page | Pass |

`New Post Page`

Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |


`New Thread Page`

Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |


`Threads Page`

Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |


`Admin Posts Page`

Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |


`Privacy Policy Page`

Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Navbar - Site logo | Redirects to home page | Click logo |  Redirects to home page | Pass |
| Navbar - Site Name | Redirects to home page | Click site name | Redirected to home page | Pass |
| Navbar - Home Link | Redirects to home page | Click home link | Redirected to home page | Pass |
| Navbar - Login Link (user not logged in) | Redirect to Login page | Click log in link | Redirected to log in page | Pass |
| Navbar - Sign up Link (user not logged in)  | Redirect to Sign up page | Click sign up link | Redirected to sign up page | Pass |

`Terms and Conditions Page`

Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Navbar - Site logo | Redirects to home page | Click logo |  Redirect to home page | Pass |
| Navbar - Site Name | Redirects to home page | Click site name | Redirected to home page | Pass |
| Navbar - Home Link | Redirects to home page | Click home link | Redirected to home page | Pass |
| Navbar - Login Link (user not logged in) | Redirect to Login page | Click log in link | Redirected to log in page | Pass |
| Navbar - Sign up Link (user not logged in)  | Redirect to Sign up page | Click sign up link | Redirected to sign up page | Pass |

`404 Page`

Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Navbar - Site Logo | Redirects to home page | Click logo | Redirected to home page | Pass |
| Navbar - Site Name | Redirects to home page | Click site name | Redirected to home page | Pass |
| Navbar - Home Link | Redirects to home page | Click home link | Redirected to home page | Pass |
| Navbar - Login Link (user not logged in) | Redirect to Login page | Click log in link | Redirected to log in page | Pass |
| Navbar - Sign up Link (user not logged in)  | Redirect to Sign up page | Click sign up link | Redirected to sign up page | Pass |
| Navbar - View all posts link | Redirect to the view all posts page | Click view all posts link | Redirected to the All Threads page | Pass |
| Navbar - Logout (user logged in) | Logs the user out of their profile, and redirects to the home page | Click logout link | --- | --- |




Back to [README.md](README.md)