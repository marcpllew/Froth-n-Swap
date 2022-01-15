from flask import Blueprint, request, redirect, render_template
from models.beer import get_beer, insert_beer, get_all_beer, update_beer
# from models.beer import delete_beer, 

beer_controller = Blueprint(
    "beer_controller", __name__, template_folder="../templates/beer")


@beer_controller.route('/beers')
def beers():
    beer_items = get_all_beer()

    return render_template('beerlist.html', beer_items=beer_items)

@beer_controller.route('/beers/create')
def create():
    return render_template('create.html')

@beer_controller.route('/beers/create', methods=["POST"])
def insert():
    # INSERT INTO DB
    insert_beer(
        request.form.get("user_id"),
        request.form.get("name"),
        request.form.get("image_url"),
        request.form.get("type"),
        request.form.get("miscellaneous"),
        request.form.get("style"),
    )

    return redirect('/')

@beer_controller.route('/beers/<id>')
def show(id):
    print(id)
    beer = get_beer(id)
    return render_template('show.html', beer=beer)

@beer_controller.route('/beers/<id>/edit')
def edit(id):
    beer = get_beer(id)
    return render_template('edit.html', beer=beer )

@beer_controller.route('/beers/<id>', methods=["POST"])
def update(id):
    name = request.form.get("name")
    style_1 = request.form.get("style_1")
    style_2 = request.form.get("style_2")
    style_3 = request.form.get("style_3")
    style_4 = request.form.get("style_4")
    miscellaneous = request.form.get("miscellaneous")
    image_url = request.form.get("image_url")

    # UPDATE
    update_beer(id, name, style_1, style_2, style_3, style_4, miscellaneous, image_url)