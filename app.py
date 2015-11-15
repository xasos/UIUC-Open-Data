from flask import Flask
from flask_restful import Api, Resource

from myapi.resources.dining import Dining
from resources.weather import Weather
#from myapi.resources.wifi import Wifi
from resources.laundry import Laundry

app = Flask(__name__)
api = Api(app)

api.add_resource(Main, '/')
api.add_resource(Weather, '/weather')
api.add_resource(Dining, '/dining/search/<query>', '/dining/<hall>/<dateFrom>/<dateTo>', '/dining/information', '/dining/balance')
api.add_resource(Wifi, '/wifi', '/wifi/<latitude>/<longitude>')
api.add_resource(Laundry, '/laundry')
#api.add_resource(Foo, '/Foo', '/Foo/<str:id>')
#api.add_resource(UniversityDirectory, '', '')
#api.add_resource(DailyIllini, '', '')
#api.add_resource(Buildings, '', '')
#api.add_resource(AthleticSchedule, '', '')
#api.add(Maintenance, '', '')

if __name__ == '__main__':
    app.run(debug=True)
