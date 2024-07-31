from run import application, request
import json
from app.modules.bearing.helpers import get_bearing



@application.route('/get_bearings', methods=['GET'])
def get_bearings():
    try:
        point1 = (39.891878,32.783405)
        point2 = (request.json.get('latitude'), request.json.get('longitude'))
        bearing = get_bearing(point1, point2)
        response = {"bearing": bearing, "success": True}

    except Exception as e:
        response = {"success":False, "error": str(e)}  
    return application.response_class(response=json.dumps(response),
                                      status=200,
                                      mimetype='application/json')