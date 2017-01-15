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

import webapp2

form_html="""
    <form>
      <h2>Add a Food</h2>
      <input type="text" name="food">
      <button>Add</button>
    </form>

"""

class handler(webapp2.RequestHandler):
    """docstring for handler."""
    def write(self, *a, **kw):
        self.response.outwrite(*a, **kw)


class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(form_html)


app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)