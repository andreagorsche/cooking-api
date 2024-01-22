![Welcome](/assets/img/Welcome_Api.png)

Welcome,

This is the cooking_api created to serve the front-end application "cooking around the world". The app itself is a social media platform that allows registered users to post recipes, rate and comment recipes of other users and follow other chefs from around the world. The back-end api "cooking-api" is programmed to handle the relevant data of the applications profiles (=chefs), recipes, comments, rating and followers. 

# Functionality of the cooking-api
Similar to a blog api, the cooking-api handles the interaction between user profiles (called chefs) and their posts (called recipes). Logged in chefs can:

* retrieve recipes, comments and other chef profiles
* like and comment on recipes
* follow other chefs
* filter recipes by special interest (e.g. type of cuisine)

In order the create this functionalities the following apps were created in the Django REST Framework:
* Profiles
* Recipes
* Comments
* Likes
* Followers

Each app was set up with according 
* models representing the database fields
* serializers to "translate" the code into JSON (for smooth data transion between backend and frontend)
* views for viewability in ListView and DetailListView
* and urls to connect everything together 

# Debugging and Testing

## Debugging
With the set up of each app, a debugging took place. Thereby the focus was on fixing bugs that showed in the terminal or in a the browser preview. 
Central debugging issues included:

### No module profiles found
After setting up my first app, the profiles app, I had a no module profiles found error.

![NoModule found](/assets/img/debugging/Error_nomodulefound.png)

The problem was that I wrote 'Profiles' in the installed Apps and the in the urls.py of the app I wrote views.profiles.as_view()) instead of: 
path('profiles/', views.ProfileList.as_view())

After fixing those typos everything was running smoothly.
With the recipes app this error happened to me again. In this case I had by mistake created a serializers file without the .py ending. 

### Operational Error at /recipes/
Because of the error caused by the serializers file with the missing .py file, I decided to delete the app completely and start from scratch (not seeing that .py was missing with the file name). In that new version of the recipes app I added a new field to the models.py file called "time effort". From then on I couldn't get past the operational error at /recipes. 

![Operational error recipes](/assets/img/debugging/OperationalError_TimeEffort.png)

The reason were migration issues. So I had to delete all previous migrations in all the project apps except for the __init__.py file and migrate once more.
That solved the issue.


## Manual Testing
With every finished app in place I did manual testing of the functionalities. The next app was only installed after the app showed no more issues in manual testing.
The central functionalities tested in the manual tests always took in consideration how the functionality should differ between logged in and logged out user. E.g. logged out users should be able to retrieve the list of profiles, recipes, comments, likes and followers. Only logged in users should be able to post recipes, like and comment them as well as follow other users. In order to test these functionalities 3 superusers and a couple of recipes were created. When creating new recipes I took an extra close look in the data fields and what happens if all of them are filled out or some of them are skipped. Also with the image upload I made sure that the size restrictions were working correctly and the error message was shown properly.

In the manual testing the following issues arose:

### Posting recipes in ListView and DetailView
When working with the get and post methods to put get a deeper understanding of this way of coding, I by mistake had definied the option to post a recipe in the ListView as well as in the DetailView. I managed to fix this by getting rid of the post method in the ListView. When switching to generic views for a cleaner code, this issue did not arise anymore.

### Likes functionality didn't work
When starting the likes app I was surprised to only find a button to create a like but no ability to choose which recipe to like (dropdown missing). I had overlooked to add the recipe field in the Meta class. After that the drop down menu showed and was functioning as expected.

### Recipe Filter didn't work properly
I had 4 filters set in the views.py file for the recipes:

* user feed
* posts a user liked
* user posts
* posts filtered by cuisine

The last filter was visible in the manual testing but didn't filter the recipes by cuisine category as expected. It turned out that I had created the wrong filterset (  'recipes__cuisine' instead of 'cuisine'). After fixing this error the filtering worked smoothly.

## Automated Testing
Automated tests were written to go one step deeper into the debugging process. Bugs found through with automated testing:

### Assertion Error with test_logged_in_user_can_create_recipe
When testing if a logged in user could create a recipe I got an unexpected assertion error: 2 != 1. 

![Assertion error](/assets/img/debugging/assertion.png)

It took me some time to figure out why 2 recipes were created when there should only be one. 
The problem was that I had copied the models code of my profiles app into the recipes app and modified the code accordingly. Thereby the createprofile function was adapted into a create recipe function, causing 2 recipes being created in the test altough it should only be one.
This test turned out to be super useful to find a mistake in my code that I otherwise most likely would have missed.

### Registration did not work properly
The error went unnoticed in the backend but showed itself when testing the front end registration. After entering the credintials and press register, nothing appearently happened. When pressing the register button again, it stated that the user already exists - implying that some data was indeed sent and saved. In the front end console it showed a 500 error, so I checked the backend and went to https://8000-andreagorsch-cookingapi-m1tec14t6l7.ws-eu105.gitpod.io/dj-rest-auth/registration/. I filled out a test registration in the backend and came across the connection refused error:

![connection refused error](/assets/img/debugging/ConnectionRefused.png)

On Stackoverflow the solution presented itself:
https://stackoverflow.com/questions/72073401/im-trying-to-connect-with-my-heroku-app-and-when-i-enter-my-email-and-password
https://stackoverflow.com/questions/21563227/django-allauth-example-errno-61-connection-refused

The problem was that upon successful registration Django tried to send a confirmation email but didn't find the according set up in the settings.py file. To fix the issue I inserted a code line that prints mails to the console.

# Deployment

## Pre-steps
Before starting the actual deployment the following pre-steps were taken:
* set up of the JWT tokens
* add root route to the api
* add pagination to all list views
* create a default JSON renderer for production
* create a date and time formatting for all the created_at and updated_at fields
    * For posts and profiles following the format date/month/year (with the month beeing a  	
      Locale’s abbreviation)
    * for comments and likes following the humanized naturaltime because they are more regularly changed or   created (telling us how long ago a comment was created or updated)

For the deployment of the cooking_api I took the following steps:
1. create a database through the Elephant SQL service
2. create a new app in Heroku
3. deployed a basic frontend in react
4. added the config vars in Heroku

## Debugging after deployment
In the deployed backend I had a 400 error and a 500 error. The 400 error could be resolved by adding the url of the preview into the allowed hosts of settings.py.
The 500 error was an issue with my permissions set in the backend. This also showed in accessing data issues in the frontend. By changing the field of the Profile model from chef to owner, the logic was more clear to me and I could erase the typos I had created in the permissions and views in the Profile and Recipes App.
Unfortunetely that whole process took me quite long and also lead to the need of deleting my initially generated database. I set up a new SQL Database with Elephant SQl and created a new sqlite database as well. Thus, my testing cases of the manual testing like created profiles and recipes, likes, followers and comments were erased in the process. 
Since this debugging cost me so much time and was finished not even 24 hours before deadline, I didn't re-test the backend, but moved right into frontend testing -figuring that if the backend was not working properly I would see it when registering users or posting recipes in the front end as well. 
When adding new data through the frontend I always checked if the data had arrived in the backend (through console.log in the console and manual testing in the deployed backend).

# Code Updates after first assessment

## Feedback on first submission:
The codebase contains new fields in the Recipe model but the rest of the models are dependent on the walkthrough project. We need to introduce such customizations that are markedly different from that project. 
Regarding the readme, it contains the testing and deployment sections. However, we need to include specific test cases and testing steps performed for API manual testing and the deployment section should include the stepwise details for creating, configuring, and deploying the backend application on Heroku.

## Added customizations

In order to distinct this project further from the walkthrough project, I took a critical look at the created apps and made significant adaptions, always having good usability and useful features for the frontend app in mind.

* The comments can now be marked as inappropriate by other users. I made sure that users can only mark comments as inappropriate if they are not their own. 

* In the profiles I integrated a counting of inappropriate comment. Users that constantly make inappropriate comments are set to inactive. I set the threshold of inappropriate comments to 5. This logic also requires a profile field that stores if a profile is currently active or not. In order to link the logic of inappropriate comments with the profiles I created signals in the profile app:
    * checking if the comment is marked as inappropriate
    * checking if the count exceeds 5 and set the profile as inactive
    * write an email to the user that the profile was set to inactive

* I deleted the like app. Instead I create a rating app that stores user ratings of 0 to 5 stars for each recipe
