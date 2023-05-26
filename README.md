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

# Debugging and Testing

## Debugging
With the set up of each app, a debugging took place. Thereby the focus was on fixing bugs that showed in the terminal or in a the browser preview. 
Central debugging issues included:

### No module profiles found
After setting up my first app, the profiles app, I had a no module profiles found error.

![NoModule found](/assets/images/debugging/Error_nomodulefound.png)

The problem was that I wrote 'Profiles' in the installed Apps and the in the urls.py of the app I wrote views.profiles.as_view()) instead of: 
path('profiles/', views.ProfileList.as_view())

After fixing those typos everything was running smoothly.
With the recipes app this error happened to me again. In this case I had by mistake created a serializers file without the .py ending. 

### Operational Error at /recipes/
Because of the error caused by the serializers file with the missing .py file, I decided to delete the app completely and start from scratch (not seeing that .py was missing with the file name). In that new version of the recipes app I added a new field to the models.py file called "time effort". From then on I couldn't get past the operational error at /recipes. 

![Operational error recipes](/assets/images/debugging/OperationalError_TimeEffort.png)

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

![Assertion error](/assets/images/debugging/assertion.png)

It took me some time to figure out why 2 recipes were created when there should only be one. 
The problem was that I had copied the models code of my profiles app into the recipes app and modified the code accordingly. Thereby the createprofile function was adapted into a create recipe function, causing 2 recipes being created in the test altough it should only be one.
This test turned out to be super useful to find a mistake in my code that I otherwise most likely would have missed.


### Testing Recipes App
test_can_list_posts
test_logged_in_user_can_create_post
test_user_not_logged_in_cant_create_post
test_can_retrieve_post_using_valid_id
test_cant_retrieve_post_using_invalid_id
test_user_can_update_own_post
test_user_cant_update_another_users_post

### Testing Profiles APP
test_can_list_profiles
test_can_retrieve_profile_using_valid_id
test_cant_retrieve_profile_using_invalid_id
test_user_can_update_own_profile
test_user_cant_update_another_users_profile


### Testing Comments App
test_can_list_comments
test_logged_in_user_can_create_comment
test_user_not_logged_in_cant_create_comment
test_can_retrieve_comment_using_valid_id
test_cant_retrieve_comment_using_invalid_id
test_user_can_update_own_comment
test_user_cant_update_another_users_comment

### Testing Likes App
test_can_list_likes
test_logged_in_user_can_create_like
test_user_not_logged_in_cant_create_like
test_can_retrieve_like_using_valid_id
test_cant_retrieve_like_using_invalid_id
test_user_can_update_own_like
test_user_cant_update_another_users_like
test_user_can’t_like_recipe_twice


### Testing Followers App
test_can_list_followers
test_logged_in_user_become_a_follower
test_user_not_logged_in_cant_become_a_follower
test_can_retrieve_follower_using_valid_id
test_cant_retrieve_follower_using_invalid_id
test_user_can_unfollow_other_users
test_user_cant_unfollow_another_users_following
test_user_can’t_follow_other_user_twice

# Deployment

## Pre-steps
Before starting the actual deployment the following pre-steps were taken:
* set up of the JWT tokens
* add root route to the api
* add pagination to all list views
* crete a default JSON renderer for production
* create a date and time formatting for all the created_at and updated_at fields
    * For posts and profiles following the format date/month/year (with the month beeing a  	
      Locale’s abbreviation)
    * for comments and likes following the humanized naturaltime because they are more regularly changed or   created (telling us how long ago a comment was created or updated)

For the deployment of the cooking_api I took the following steps:
1. create a database through the Elephant SQL service
2. create a new app in Heroku
