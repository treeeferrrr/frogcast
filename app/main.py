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
import jinja2
import webapp2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
# [END imports]


API_KEY = "22669008d62b0d56b886cc4f14f24f99"

def get_temperature(lat, lon):
    forecast = forecastio.load_forecast(API_KEY, lat, lon, units = "si")

    return forecast.currently().temperature

class MainPage(webapp2.RequestHandler):
    def get(self):
        lat = self.request.get('lat', 0)
        lon = self.request.get('lon', 0)
        temp = get_temperature(lat,lon)
        template_values = {
            'lat' : lat,
            'lon' : lon,
            'temp' : temp,
        };
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))
    def post(self):
        lat = self.request.POST.get('lat')
        lon = self.request.POST.get('lon')
        temp = get_temperature(lat,lon)
        template_values = {
            'lat' : lat,
            'lon' : lon,
            'temp' : temp,
        };
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))
        



app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/input', MainPage),
], debug=True)
