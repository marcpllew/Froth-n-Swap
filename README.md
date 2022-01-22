# Froth'n Swap

Game can be accessed by following link:

https://marcpllew.github.io/'.........'/

or github, search for marcpllew/'.......'

## Tech Used

-   HTML
-   CSS
-   Python
-   Flask
-   Heroku
-   SQL
-   Bootstrap
-   Splide (CDN)

## Issues

-   After renaming Git repo, Heroku and local file, app would not lauch, giving an error of the current file could not be found. I eventualy solved this by removing the apostrophe from name, froth'n swap to froth-n-swap.

## Planning

Froth'n Swap

-   user data base

    -   2 tables Users and Beers

-   Users have ability to sign up/log in/log out

-   for 'style's' will need to create specific parametres for each 'style' then add an if statemnet to check if style parameters are true or false for selected choice

    -   have a way to categorise the items (beers) in styles for easier searching based on preference. (for later)

-   a user can trade beers by posting what they have.(these will be added to the data base) these will need to be linked to the user that posted them.

    -   to do this when an item is added it could be linked to user id?

-   Add like(for later)/next/previous buttons to image displayed

-   Have ability to scroll through data base with next and previous buttons

-   a logged in user can scroll through the list of items and and ‘like’ something. this could then check if another user has liked something in this users list and create a match?(for later)

-   users will then be directed to trading page(for later)

## 15/1

-   Add authentication functionality
-   Add in tables to data base
-   add a nave bar using bootsrap
-   add in some basic CSS styling

## 17/1

-   Add edit, delete and edit functionality
-   start to research how i can display 1 picture on page and manualy scroll through pictures one at a time

## 19/1

-   Add Carosel funtionality to the app using 'Splide'
-   Add functionality to loop through all pictures
-   After getting this to function pictures where all squashed, which required some styling in CSS
-   Centre pictures on page
-   remove edit from homepage
-   remove show from show page

## 20/1

-   Create a sign in page
-   add functionality where only logged in user can edit items posted by them

## 22/1

-   style edit and create pages

## Questions

-   how can i access these values without displaying them?(completed)
-   accesing background color in css (completed)
-   accessing heading in css (completed)
-   picture changed when in show (completed)

-   More explination on ENUM and putting into practice
does the following commands need to be in beerlist.html or show.html. <h3>{{ beer['user_id'] }}</h3>
 <h3>{{ user_id }}</h3>

## to do's

-   Can only delete items when logged in
-   Make a home page
-   create a back button
-   displayer user on screen
-   start styling,
    -   options, give everything a class name
-
