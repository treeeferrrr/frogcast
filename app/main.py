# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


# [START imports]
import os
import sys
sys.path.insert(0, 'lib')
import forecastio
import json
import jinja2
import webapp2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
# [END imports]


API_KEY = "22669008d62b0d56b886cc4f14f24f99"

##def get_temperature(lat, lng):
##    forecast = forecastio.load_forecast(API_KEY, lat, lng, None, "si")
##    return forecast.currently().temperature

def get_current_weather(lat, lng):
    forecast = forecastio.load_forecast(API_KEY, lat, lng, None, "si")
    result = forecast.currently()
    result.d['timezone'] = forecast.json['timezone']
    return result


class MainPage(webapp2.RequestHandler):
    def get(self):
        lat = self.request.get('lat', 0)
        lng = self.request.get('lng', 0)
##        temp = get_temperature(lat,lng)
        template_values = {
            'lat' : lat,
            'lng' : lng,
##            'temp' : temp,
        };
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))



class Results(webapp2.RequestHandler):
    def post(self):
        data = json.loads(self.request.body)
        #temp = get_temperature(data['lat'], data['lng'])
        weather_info = get_current_weather(data['lat'], data['lng'])
        temp = weather_info.temperature
        icon = weather_info.icon
        wind = weather_info.windSpeed
        rain_chance = weather_info.precipProbability
        humidity = weather_info.humidity
        timezone = weather_info.timezone
        self.response.out.write(json.dumps(({'temp': temp,
                                             'icon': icon,
                                             'wind': wind,
                                             'rain_chance': rain_chance,
                                             'humidity': humidity,
                                             'timezone': timezone})))
        



app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/results', Results),
], debug=True)
