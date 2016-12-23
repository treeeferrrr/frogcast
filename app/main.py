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
import urllib


import jinja2
import webapp2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
# [END imports]


class MainPage(webapp2.RequestHandler):
    def get(self):
        lat = self.request.get('lat', 0)
        lon = self.request.get('lon', 0)
        template_values = {
            'lat' : lat,
            'lon' : lon
        };
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))
    def post(self):
        lat = self.request.POST.get('lat')
        lon = self.request.POST.get('lon')
        template_values = {
            'lat' : lat,
            'lon' : lon
        };
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))
        



app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/input', MainPage),
], debug=True)
