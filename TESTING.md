<h1 align="center">Testing</h1>

---

## Index 

- <a href="#validators">1. Code validators</a>
- <a href="#responsiveness">2. Responsiveness</a>
- <a href="#browser-compatibility">3. Browser compability</a>
- <a href="#user-stories">4. Testing user stories </a>
- <a href="#defensive-design">5. Defensive design</a>
- <a href="#bugs">5. Bugs</a>

---



## 1. Code validators
- **[HTML Validator](https://validator.w3.org/):** No errors to show.
   - With testing the HTML code, I had some syntax issues on all pages I build with jinja and bootstrap templating.
   - I tested the HTML code deployed to heroku.
   - There is 6 erros on every page because of the bootstrap classes.

   ![HTML-calidation](testing/images/html-validation.png)

- **[CSS Validator](https://jigsaw.w3.org/css-validator/):** 15 error related to bootstrap.
   ![CSS Validator](testing/images/index-css-validation.png)


- **[Python validator | PEP8](http://pep8online.com/):** No errors found

   ![python validator](testing/images/python-validation.png)

---

<span id="responsiveness"></span>

## 2. Responsiveness 
- Responsiveness of the game is tested with [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools) and [Responsive Design Checker](https://www.responsivedesignchecker.com/).
- The game is tested on the following devices: 
    - Desktop: 1024px, 1366px, 1440px, 1600px and 1680px. 
    - Mobile & Tablet: Galaxy S5, iPhone 5/SE, iPhone 6/7/8, iPhone 6/7/8 plus, iPhone x, iPad and  iPad Pro

![Responsiveness testing](testing/images/index-vid_AdobeExpress.gif)
![Responsiveness testing](testing/images/home-vid_AdobeExpress.gif)
![Responsiveness testing](testing/images/profile-vid_AdobeExpress.gif)
![Responsiveness testing](testing/images/wall-vid_AdobeExpress.gif)
![Responsiveness testing](testing/images/register-vid_AdobeExpress.gif)


---

## 3. Browser compatibility
![Browser compatibility](testing/images/browsers.png)

---

<span id="user-stories"></span>

## 4. Testing user stories 

### First-time visitor goals:
1. As a first time visitor, I want to be able to visit the website on every device, so that I can look at the website on desktop, mobile and tablet. 
   - The first time visitor can visite the website on a computer, laptop, tablet and phone.
2. As a first time visitor, I want to be able to navigate easily through the website, so I can find everything easily. 
   - The first time visitor can navigate through the website with the navbar. The navbar is on top of the website.
3. As a first time visitor i want to be able to register for an account.
   -The first time visitor can regiter for an account from the index page.
4. As a first time visitor i want to be able to see the posts of other users.
   - The first time visitor can see other users posts on the website's wall.


### Site member goals

1. As a user i want to be able to edit my profile,
   - The first time user can enter and edit their username display and the description about them.
2. As a user i want to be abel to delete my posts if i want to.
   - The first time visitor can delete their post at any giving time.
3. As a user i want to be able to edit and delete my profile description.
   - The user can edit and remove thei data.
4. As a user i want to be able to logout easily.
   - The user can find the logout button in the menu.


---

## 5. Defensive design 

1. The user is not able to break the site by clicking on buttons. 

**Answer 1:** All buttons on the website work. The buttons on the website consist buttons that lead to other pages or submit buttons to add, edit or delete something from the database.

2. The signup form: 
   - 2.1 The user has to provide a unique username.
   - 2.2 The user has to provide an email.
   - 2.3 The user has to double check the password.

--- 

<span id="bugs"></span>

## 6. Bugs | Solved

1. The developer faced a bug where he couldn’t make migration to the db, after looking through stack overflow and documentations the developer found a solution where he added an import of the models to the env.py within the migrations folder. 
[Stack Overflow](https://github.com/miguelgrinberg/Flask-Migrate/issues/203)

2. The developer faced a bug where the app crashed after migrating the db with a : RuntimeError: UNIQUE constraint failed: users.username . 
the developer fixed the bug relying on stackoverflow.
[Stack Overflow](https://cs50.stackexchange.com/questions/38498/finance-unique-constraint-failed-users-username)

3. The developer had a bug where th app crashed when deployed tp Heroku, the problem was related to github branches. The developer fixed the issue relying on stackoverflow. 
[Stack Overflow](https://stackoverflow.com/questions/9794413/failed-to-push-some-refs-to-githeroku-com)