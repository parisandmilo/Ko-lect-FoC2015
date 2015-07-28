import sys_modules.database as db

def offer_add(request):
    coords = request.form.getlist('location')[0].split(',')
    coords_array=[coords[0],coords[1]]
    offer= {
        'title': request.form.getlist('title')[0],
        'description': request.form.getlist('description')[0],
        'username': request.form.getlist('username')[0],
        'ttl': request.form.getlist('ttl')[0],
        'location': coords_array
    }
    
    db.db_insert('offers',offer)
    
    return "offer add"

def offer_get_id(request):
    return "offer get id"

def offer_get_near_me(request, coords):
    coords = coords.split(',')

    lat = coords[0]
    lng = coords[1]

    return "get near me"