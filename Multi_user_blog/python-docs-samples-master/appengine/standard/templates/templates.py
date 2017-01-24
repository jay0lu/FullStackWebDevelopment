"""
Learning templates
"""

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

import os

import jinja2
import webapp2

import rot13
import signup


template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),
                               autoescape=True)


class Handler(webapp2.RequestHandler):
    """docstring for handler. handler"""
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))


class MainPage(Handler):
    def get(self):
        items = self.request.get_all("food")
        self.render("shopping_list.html", items=items)


class FizzBuzzHandler(Handler):
    def get(self):
        n = self.request.get('n', 0)
        n = n and int(n)
        '''equals to
                    if n:
                        n = int(n)
        '''
        self.render("fizzbuzz.html", n=n)


class Rot13Handler(Handler):
    def get(self):
        self.render("rot13.html")

    def post(self):
        text = self.request.get('text')
        text = str(text)
        self.render("rot13.html", text=rot13.rot13Trans(text))


class SignupHandler(Handler):
    def get(self):
        self.render("signup.html")

    def post(self):
        username = self.request.get('username', None)
        password = self.request.get('password', None)
        verify = self.request.get('verify')
        email = self.request.get('email', None)
        username_verify = signup.valid_username(username)
        password_verify = signup.valid_password(password)
        email_verify = signup.valid_email(email)
        retype_password = signup.password_retype(password, verify)

        if not(username_verify and password_verify and retype_password and email_verify):
            self.render("signup.html", username=username,
                                       email=email,
                                       username_verify=username_verify,
                                       password_verify=password_verify,
                                       email_verify=email_verify,
                                       retype_password=retype_password)
        else:
            self.redirect('/loged?username=' + username)


class LogedinHandler(Handler):
    def get(self):
        username = self.request.get('username')
        self.render("loged.html", username=username)


app = webapp2.WSGIApplication([('/', MainPage),
                               ('/fizzbuzz', FizzBuzzHandler),
                               ('/rot13', Rot13Handler),
                               ('/signup', SignupHandler),
                               ('/loged', LogedinHandler),
                               ], debug=True)
