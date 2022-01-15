import database

# INSERT BEERS INTO DB


def insert_beer(id, name, image_url, type, miscellaneous, style):
    database.sql_write("INSERT into beers (name, image_url, type, miscellaneous, style) VALUES (%s, %s, %s, %s, %s);", [
        name,
        image_url,
        type,
        miscellaneous,
        style,
        
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

# UPDATE FOOD IN DB

def update_beer(id, name, image_url, type, miscellaneous, style):
    database.sql_write("UPDATE beers set name = %s, image_url = %s, type = %s, miscellaneous = %s, style = %s,  WHERE id = %s", [
        id,
        name,
        image_url,
        type,
        miscellaneous,
        style
        
    ])