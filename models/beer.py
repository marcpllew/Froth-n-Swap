import database

# INSERT BEERS INTO DB


def insert_beer(user_id, name, image_url, type, miscellaneous, style):
    database.sql_write("INSERT into beers (user_id, name, image_url, type, miscellaneous, style) VALUES (%s, %s, %s, %s, %s, %s);", [
        user_id,
        name,
        image_url,
        type,
        miscellaneous,
        style
        
    ])

# SELECT BEER FROM DB


def get_beer(id):
    results = database.sql_select(
        'SELECT * FROM beers WHERE id = %s', [id])
        #    'SELECT * FROM beers WHERE id = 1',[])
    result = results[0]
    return result

    #SELECT ALL BEER FROM DB


def get_all_beer():
    results = database.sql_select(
        "SELECT * FROM beers", [])

    return results

# UPDATE BEER IN DB

def update_beer(id, name, image_url, type, miscellaneous, style):
    database.sql_write("UPDATE beers set name = %s, image_url = %s, type = %s, miscellaneous = %s, style = %s  WHERE id = %s", [
        name,
        image_url,
        type,
        miscellaneous,
        style,
        id
        
    ])
    # DELETE BEER FROM DB
def delete_beer(id):
    database.sql_write("DELETE FROM beers WHERE id = %s", [id])