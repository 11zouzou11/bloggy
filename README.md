<h1 align="center">Bloggy</h1>

<span id="bloggy"></span>

![Portfolio website](/readme/images/ms3-am-i-responsive.png)

After a long day at work, school or just doing you shores and homeworks your mind
needs the stimulation so you can rense and refresh it,

Bloggy is a social website where you can spill all or your thought after a long day.

Bloggy is where you turn to chat with your registered friends and family that shares 
the same intrest as you!.

This project is the third out of four Milestone Projects in the Full Stack Web Development Program I am attending at The Code Institute.

**[View the live project here.](https://flask-boggy-ci.herokuapp.com/login?next=%2Findex)**


---

## Index 


- <a href="#ux">1. User experience (UX)</a>
  - <a href="#ux-goals">1.1. Project goals</a>
  - <a href="#ux-stories">1.2 User stories</a>
  - <a href="#ux-design">1.3 Design</a>
  - <a href="#ux-architecture">1.4 Information architecture</a>
  - <a href="#ux-mockup">1.5 Mockup designs</a>
- <a href="#features">2. Features</a>
  - <a href="#features-existing">2.1 Existing features</a>
  - <a href="#features-future">2.2 Features left to implement in the future</a>
- <a href="#technologies">3. Technologies used</a>
- <a href="#testing">4. Testing</a>
- <a href="#deployment">5. Deployment</a>
- <a href="#credits">6. Credits</a>


---


<span id="ux"></span>

<h1>1. User experience (UX)</h1>

<span id="ux-goals"></span>

### 1.1 Project goals 

- Making a full-stack site that  allows its users to comunicate with each other without a filter.

- Making a full-stack site that uses HTML, CSS, JavaScript, Python+Flask.

- The users of the website can make use of CRUD (create, read, update and delete) for their profiles and posts

- the users can follow each other to see their latest posts 

<span id="ux-stories"></span>

### 1.2 User stories 

**First-time visitor goals:**

1. As a first time visitor, I want to be able to visit the website on every device, so that I can look at the website on desktop, mobile and tablet. 
2. As a first time visitor, I want to be able to navigate easily through the website, so I can find everything easily. 
3. As a first time visitor, I want to register an account on the website, so I can share my recipes on Breaktasty.
4. As a first time visitor, i want to find friends and family members.


**Site member goals:** 

All the goals of first-time visitors also apply for site members. There are additional user stories to the site members because they have more access to the website. See the additional user stories below.
1. As a site member, I want to find my friends easily.
2. As a site member, I want to be able to post stuff on the website freely.
3. As a site member, I want to be able to remove my posts if i want to.
4. As a site member, I want to be able to cusomize my profile

### 1.3 Design 

- #### Colour scheme 

The four colours that are used for the recipe website are very neutral and simple. I have chosen these colours because the colours give a sleek and uncluttered appearance. 

![Colour scheme](/readme/images/colors-ms3.png)

- #### Fonts

The **Source Sans Pro**are used throughout the whole website. Sans serif and cursive are the fallbacks in case the main font isn’t being imported to the site correctly. 


- #### Interactive design 

    - The website has to be easy to navigate. 
    - The user can quickly find the information he/she wants to find.

![Interactive design](/readme/images/New%20Project%201.png)

### 1.4 Information architecture

The database is structured as follows:

![Information architecture](/readme/images/data-structure-for-ms3-follow%20.png)

### 1.5 Mockup designs


Wireframe mockups were created in a [Balsamiq]((https://balsamiq.com/ "Link to baslsamiq")


website: 

![Website Wireframe](/readme/images/ms3-wireframes.png "Website Wireframe")


### 2.1 Existing features 

#### 1. Design 
- An attractive and simple layout with consistency.
- Simple navigation throughout the website by using the navigation bar. 
- Showing the posts simple and clearly

#### 2. General 
- The index page shows an introduction in the shape of a header and a login form. And the page shows a link to registration.
- People can sign up for a new account.

#### 3. Home
- The user can creat a post and submit it.
- The user can see the post they created and the users that they follow.
- The user can click on another user's name and access their profile.

#### 4. profile

- The user can see their own profile and edit some of the info.
- The user can easily logout of the account with a navbar link.


### 2.2 Features left to implement in the future 
- Adding a like and a comment sections to the posts.
- Giving the user the ability to uppload their own picture whithin the profile.
- Adding paginaotion to the wall.
- Add form validation on the backend.
- The user can delete their profile.


#### Languages used
- [HTML5](https://en.wikipedia.org/wiki/HTML5)
    - HTML5 provides the structure and the content for my project. 
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
    - CSS3 provides the style of the HTML5 elements.
- [jQuery](https://jquery.com/)
    - jQuery used as the JavaScript functionality.
- [Python](https://www.python.org/)
    - Python provides the backend of the project.


#### Frameworks, libraries & Other
- [Gitpod](https://www.gitpod.io/) 
    - The GitPod is used to develop the project.
- [Git](https://git-scm.com/)
    - The Git was used for version control to commit to Git and push to GitHub.
- [GitHub](https://github.com/)
    - The GitHub is used to host the project.
- [Google Fonts](https://fonts.google.com/)
    - Google Fonts is used to provide the font roboto for all the text that is used in the project. 
- [Balsamiq](https://balsamiq.com/)
    - Balsamiq is used to create the mockup designs for the project.
- [Bootstrap](https://getbootstrap.com/docs/5.2/getting-started/introduction/)
    - Bootstrap is used for the design framework.
- [Postgres](https://www.postgresql.org)
    - Postgres is the fully managed cloud database service used for the project.
- [Heroku](https://dashboard.heroku.com/)
    - Heroki is the cloud platform to deploying the app.
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
    - Flask is the web framework used to provide libraries, tools and technologies for the app.
- [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)
    - Jinja is used for templating Python
- [Werkzeug](https://werkzeug.palletsprojects.com/en/1.0.x/)
    - Werkzeug is used for password hashing and authentication and autohorization.


#### Testing tools used 
- [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools/open) is used to detect problems and test responsiveness.
- [Autoprefixer](https://autoprefixer.github.io/)
    - Autoprefixer is used to parse the CSS and to add vendor prefixes to CSS rules. 
- [W3C Markup Validation Service](https://validator.w3.org/)
    - The W3C Markup Validation Service is used to check whether there were any errors in the HTML5 code. 
- [W3C CSS validator](https://jigsaw.w3.org/css-validator/)
    - The W3C CSS validator is used to check whether there were any errors in the CSS3 code.
- [JShint](https://jshint.com/)
    - JShint is a JavaScript validator that is used to check whether there were any errors in the JavaScript code. 
- [PEP8](http://pep8online.com/)
    - The PEP8 validator is used to check whether there were any errors in the Python code.


<span id="testing"></span>

<h1>4. Testing</h1>

The testing process can be found [here](TESTING.md).

<span id="deployment"></span>

<h1>5. Deployment</h1>

#### Requirements 
- Python3 
- Github account 
- Heroku account

#### Clone the project 
To make a local clone, follow the following steps. 
1. Log in to GitHub and go to the repository. 
2. Click on the green button with the text **“Code”.**
3. Click on **“Open with GitHub Desktop”** and follow the prompts in the GitHub Desktop Application or follow the instructions from **[this link](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop)** to see how to clone the repository in other ways. 


#### Working with the local copy
1. Install all the requirements: Go to the workspace of your local copy. In the terminal window of your IDE type: **pip3 install -r requirements.txt**.

2. Run the app: Open your terminal window in your IDE. Type python3 bloggy.py and run the app.

#### Heroku Deployment  
1. Set up local workspace for Heroku 
    - In terminal window of your IDE type: **pip3 freeze -- local > requirements.txt.** (The file is needed for Heroku to know which filed to install.)
    - In termial window of your IDE type: **python bloggy.py > Procfile** (The file is needed for Heroku to know which file is needed as entry point.)
2. Set up Heroku: create a Heroku account and create a new app and select your region. 
3. Deployment method 'Github'
    - Click on the **Connect to GitHub** section in the deploy tab in Heroku. 
        - Search your repository to connect with it.
        - When your repository appears click on **connect** to connect your repository with the Heroku. 
    - Go to the settings app in Heroku and go to **Config Vars**. Click on **Reveal Config Vars**.
        - Enter your config vars.
4. Push the requirements.txt and Procfile to repository. 
     ```
    $ git add requirements.txt
    $ git commit -m "Add requirements.txt"
    $ git add Procfile 
    $ git commit -m "Add Procfile"
    ```
5. Automatic deployment: Go to the deploy tab in Heroku and scroll down to **Aotmatic deployments**. Click on **Enable Automatic Deploys**. By **Manual deploy** click on **Deploy Branch**.

Heroku will receive the code from Github and host the app using the required packages. 
Click on **Open app** in the right corner of your Heroku account. The app wil open and the live link is available from the address bar. 

<span id="credits"></span>

<h1>6. Credits</h1>

### Content
- The game idea was implemented based on the developers insight

## Code 

The following sites were used on a more regular basis to help implement and build this responsive website : 

- [Stack Overflow](https://stackoverflow.com/ "Link to Stack Overflow page")
- [W3Schools](https://www.w3schools.com/ "Link to W3Schools page")
- [Bootstrap](https://getbootstrap.com/ "Link to BootStrap page")
- [Google](https://www.google.com/ "Link to Google page")
- [Youtube](https://www.youtube.com/ "Link to Youtube page")

- Note:
    - the video contect were used to get a better understanding of the elements and everything got modified to meet the websites goals. 


<a href="#Bloggy">Back to top!</a>