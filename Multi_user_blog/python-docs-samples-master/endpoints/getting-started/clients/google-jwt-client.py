#!/usr/bin/env python

# Copyright 2016 Google Inc. All Rights Reserved.
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

"""Example of calling a Google Cloud Endpoint API with a JWT signed by
a Google API Service Account."""

import argparse
import time

import oauth2client.crypt
from oauth2client.service_account import ServiceAccountCredentials
import requests
from six.moves import urllib


def generate_jwt(service_account_file):
    """Generates a signed JSON Web Token using a Google API Service Account."""
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        service_account_file)

    now = int(time.time())

    payload = {
        'iat': now,
        'exp': now + credentials.MAX_TOKEN_LIFETIME_SECS,
        # aud must match 'audience' in the security configuration in your
        # swagger spec. It can be any string.
        'aud': 'echo.endpoints.sample.google.com',
        # iss must match 'issuer' in the security configuration in your
        # swagger spec. It can be any string.
        'iss': 'jwt-client.endpoints.sample.google.com',
        # sub and email are mapped to the user id and email respectively.
        'sub': '12345678',
        'email': 'user@example.com'
    }

    signed_jwt = oauth2client.crypt.make_signed_jwt(
        credentials._signer, payload, key_id=credentials._private_key_id)

    return signed_jwt


def make_request(host, api_key, signed_jwt):
    """Makes a request to the auth info endpoint for Google JWTs."""
    url = urllib.parse.urljoin(host, '/auth/info/googlejwt')
    params = {
        'key': api_key
    }
    headers = {
        'Authorization': 'Bearer {}'.format(signed_jwt)
    }

    response = requests.get(url, params=params, headers=headers)

    response.raise_for_status()
    return response.text


def main(host, api_key, service_account_file):
    signed_jwt = generate_jwt(service_account_file)
    response = make_request(host, api_key, signed_jwt)
    print(response)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        'host', help='Your API host, e.g. https://your-project.appspot.com.')
    parser.add_argument(
        'api_key', help='Your API key.')
    parser.add_argument(
        'service_account_file',
        help='The path to your service account json file.')

    args = parser.parse_args()

    main(args.host, args.api_key, args.service_account_file)
