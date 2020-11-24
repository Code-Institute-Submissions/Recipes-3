
# Mile-3 

## Milestone Three Project
This project represents a Flask application which is backed by MongoDB database, it uses HTML, CSS, and Python languages to make it function.  It is a recipe app which follows strictly all CRUD requirements set by Code Institute. The user is able to add, read, edit, and delete recipes and categories from the frontend interface of the app through python routes directly to MongoDB database. Novice cooking ideas or elaborate recipes can be shared just with a couple of clicks. The app target is literally everyone who is fascinated by cooking and needs a cooking book where he or she can exchange ideas or add to already existing recipes. 
By default, the project comes with six recipes for a Shrimps Soup, Pan-Seared Salmon with Baby Bok Choy and Shiitake Mushrooms, Flank Steak with Charred Vidalia Onion Salad, Classic Roast Beef, Chocolate Peppermint Cheesecake, and Oreo Truffles. There’re also three categories such as soups, meals, and deserts.
The project is fully based on Code Institute’s videos which are to be removed on 30th of November 2020. For me personally, it would be quite impossible to complete this project without the help of these videos. The mere fact that so much new technology in terms of languages (python), framework (Flask), database (mongoDB), materialize and deployment through heroku was very overwhelming. Again, pressurized by time, I am working full time, I managed to make it fully functional without focusing too much on style and design. Even with the help of the videos, tutors, and my mentor linking all that new to me technology was a hassle which took months of developing.
## UX and Design
As I already specified, did not focus too much on the design, but making python working with HTML and the database properly.
Of course, mobile first approach has been leading 

#### Skeleton
* [DesktopI]( https://github.com/Web-Cookie/Recipes/blob/main/assets/Milestone_3%20Desctop%20I.PNG)
* [DesktopII]( https://github.com/Web-Cookie/Recipes/blob/main/assets/Milestone%203%20Desctop%20II.PNG)
* [DesktopIII]( https://github.com/Web-Cookie/Recipes/blob/main/assets/Milestone%203%20Desctop%20III.PNG)
* [MobileVersionI]( https://github.com/Web-Cookie/Recipes/blob/main/assets/Milestone%203%20Mobile%20I.PNG)
* [MobileVersionII]( https://github.com/Web-Cookie/Recipes/blob/main/assets/Milestone%203%20Mobile%20II.PNG)
* [MobileVersionIII]( https://github.com/Web-Cookie/Recipes/blob/main/assets/Milestone%203%20Mobile%20III.PNG)



## Technologies

* HTML- HTML5

* CSS - used for styling purpose 

* Python – imperative language has been used to pass data through the backend to the database and to the frontend HTML

* [VSCode] ((https://code.visualstudio.com/) – is text editor that I am currently using)
* [Materialize]( https://materializecss.com/) – has been used big time to create the desired framework of my web-site

* [Git & Github](https://github.com/) – for storing and backing up externally 

* [Gitpod]( https://www.gitpod.io/) – for sharing my workspace with Code Institute’s tutors, so the latter would be able to help better and faster

* [Heroku] (https://dashboard.heroku.com/apps) – hosting platform to store the code, you can run the app from that platform, something that github cannot do. Github cannot run python files 


* [Mockflow]( https://www.mockflow.com/) – to sketch my wireframe, free wireframe resource 

## Testing and Debugging

Did really helpful testing and debugging on my select drop down menu. Of course, with the help of my mentor. Basically, the select drop down was not dropping and giving different categories as options. Hence, placing # import pdb ; pdb.set_trace() after the line you want to test, it breaks the code. The function gave back that my categories are 0, instead of 3. That’s how I found that I have a typo in declaring that collection in MongoDB. Screenshots are attached below. 

* [DebuggingI](https://github.com/Web-Cookie/Recipes/blob/main/assets/Debugging%20Python%201.PNG)
* [DebuggingII](https://github.com/Web-Cookie/Recipes/blob/main/assets/debugging%20py%202.PNG)
* [DebuggingIII](https://github.com/Web-Cookie/Recipes/blob/main/assets/debugging%20py%203.PNG)


The rest of the code html code was tested through [W3C Validator](https://validator.w3.org/)

## Deployment Write-up

I have to admit that installing flask and deploying to heroku was quite difficult for me. I’ve done it by undertaking the below actions. All commands are run from the terminal:

Deployed project can be found on https://recipe-manager-3.herokuapp.com/

* Pip install Flask
* Created a virtual environment 
* Pip install pipenv
* Created a folder .venv
* Run pipenv install
* Pipenv shell 
* Pip install PACKAGE_NAME
* Put the env.py and .venv in gitignore, so passwords would not be visible 
* pip install dnspython
* pip install flask-pymongo
* Deploying to heroku 
* Created a requirements.txt file 
* Creating a procfile: echo web python app.py > Procfile
* Git add . 
* Git commit –m “Message”
* Created a new application from Heroku platform 
* Configured the variables in heroku from settings
* Set IP to 0.0.0.0
* MONGO_URI is the username and password you’ve used
* Set PORT to 5000
* Make first push to heroku
* Git add.
* Git commit –m “”
* Git push heroku master

Git and github version control steps do not differ from previous projects:
* Go to https://github.com/Web-Cookie/Recipes to find my GitHub repository

* Go to 'clone or download' button

* Copy the link

* Open a bash terminal 

* Change the current working directory to the location you want to have the cloned repository saved

* Type 'git clone', and paste the link that you copied earlier

*	Then all the files that the website uses will be saved on your local machine

* You can launch the website by opening up the index.html file from your newly created folder

## Credits

Special shout outs to my mentor Guido and to all of Code Institute tutors.
During one of our sessions Guido asked to share my screen and walk me through some of the code which was troublesome at that time for me. I would never forget that help, I did not even ask for it. Did thank him thousand times, because I was seriously stuck with the drop down select menu.
Again many hours spent, luckily tutors were available even on weekends which enabled progressing and completing this project. I would like to add more functionality and style (images) into the project, but simple I’m very limited in terms of time. I think, I’ve learned more or less how to use python routes which link the back-end with the frontend and database which matters the most for this project.









