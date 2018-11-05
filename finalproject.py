from flask import Flask
app = Flask(__name__)


@app.route('/')
@app.route('/restaurants')
def showRestaurants():
    message="<html><body>This page will show all my restaurants</body></html>"
    return message

@app.route('/restaurant/new')
def newRestaurants():
    message="<html><body>This page will be for making a new one</body></html>"
    return message

@app.route('/restaurant/<int:restaurant_id>/edit')
def editRestaurants(restaurant_id):
    message="<html><body>This page will be for editing restaurant %s</body></html>" % restaurant_id
    return message

@app.route('/restaurant/<int:restaurant_id>/delete')
def deleteRestaurants(restaurant_id):
    message="<html><body>This page will be for deleting restaurant %s</body></html>" %restaurant_id
    return message

@app.route('/restaurant/<int:restaurant_id>')
@app.route('/restaurant/<int:restaurant_id>/menu')
def showMenu(restaurant_id):
    message="<html><body>This page is the menu for restaurant %s</body></html>" %restaurant_id
    return message

@app.route('/restaurant/<int:restaurant_id>/menu/new')
def newMenuItem(restaurant_id):
    message="<html><body>This page is for making a new menu item for restaurant %s</body></html>" %restaurant_id
    return message

@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit')
def editMenuItem(restaurant_id,menu_id):
    message="<html><body>This page is for editng menu item %s</body></html>" %menu_id
    return message

@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete')
def deleteMenuItem(restaurant_id,menu_id):
    message="<html><body>This page is for deleting menu item %s</body></html>" %menu_id
    return message

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
