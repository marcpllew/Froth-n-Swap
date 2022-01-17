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

## Issues

-   After renaming Git repo, Heroku and local file, app would not lauch, giving an error of the current file could not be found. I eventualy solved this by removing the apostrophe from name, froth'n swap to froth-n-swap.

## Planning

TinTins/Froth'n Swap

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

## Questions

-   How do i add drop down tabs for styles?

-   create page is not creating

-   edit page is throwing anerror (update_beer() takes 6 positional arguments but 8 were given)

-   Do i store actual code inside readme file? LIke JPEG?

-   id numbers are random, and user_id are all the same?

## to do's

-   abilty to add new beers to data base vier the app (this is currently throwing an error when attemted (Method not allowed))
    -   this was solved by changing request.form.get("name") to session.get("user_id") in beer_controller
-   Add ability to edit and delete items from DB( throwing same as above error)
    -   Delete was solved by re-typing the command - @beer_controller.route('/beers/<id>/delete', methods=["POST"]) in beer_controller, possible copy and paste bug?
    -   Edit was throwing to this error - takes 5 positional arguments but 6 were given. Solved by adjusting and matching all arguments. I then had another error, which was solved my deleting comma.
-   make arrow buttons functional
-   arrow buttons should scroll through the data base 1 pic at a time
-   style and move arrow buttons
-   look into drop down boxes with 'style' name for creating new items
-   arrow buttons next to pictures to scroll though pics on database
-   only show the edit button insude that particular item

## for displaying pictures

-   limit and offset (database query to display pictures)
-   a gallery/carousel in bootstrap (using java script) to display pictures
