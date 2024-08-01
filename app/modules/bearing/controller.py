from run import application, request
import json
from app.modules.bearing.helpers import get_bearing, locations



@application.route('/get_bearings', methods=['POST'])
def get_bearings():
    try:
        user_point = (request.json.get('latitude'), request.json.get('longitude'))
        lover_point = (locations[request.json.get('lover')])
        locations[request.json.get('user')] = user_point
        bearing = get_bearing(user_point, lover_point)
        response = {"bearing": bearing, "success": True}

    except Exception as e:
        response = {"success":False, "error": str(e)}  
    return application.response_class(response=json.dumps(response),
                                      status=200,
                                      mimetype='application/json')