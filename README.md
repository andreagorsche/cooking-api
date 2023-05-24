![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome,

This is the cooking_api created to serve the front-end application "cooking around the world". The app itself is a social media platform that allows registered users to post recipes, like and comment recipes of other users and follow other chefs from around the world. The back-end api "cooking-api" is programmed to handle the relevant data of the applications profiles (=chefs), recipes, comments, likes and followers. 

# Functionality of the cooking-api
Similar to a blog api, the cooking-api handles the interaction between user profiles (called chefs) and their posts (called recipes). Logged in chefs can:

* retrieve recipes, comments and other chef profiles
* like and comment on recipes
* follow other chefs
* filter recipes by special interest (e.g. type of cuisine)

In order the create this functionalities the following apps were created:
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

# Debugging
With the set up of each app, a debugging took place. The next app was only installed after the app showed no more bugs. Thereby the focus was on fixing bugs that showed in the terminal or in a the browser preview. Manual Testing (refered to in the next session) took place after all apps were set up and ready for interaction.
Central debugging issues included:

##


## Testing

For each app manual tests were written to test the functionality of each app and go one step deeper into the debugging process.

### Testing Recipes App



# Deployment
For the deployment of the cooking_api I took the following steps:
1. create a database through the Elephant SQL service
2. create a new app in Heroku
