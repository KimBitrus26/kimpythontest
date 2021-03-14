import random
from unittest import TestCase
import unittest 
import requests
import json
from datetime import datetime

test_instance_number = random.randint(0, 200000)
base_url = 'http://127.0.0.1:5000' # can be changed to real server domain later
url = base_url + '/song'

class TestCreateEndpoint(TestCase):

    def test_song_new_no_entry(self):
        # Ensures no input means 400 Error
        response = requests.post(url, headers={'Content-Type': 'application/json'})
        res = response.json()
        self.assertEqual(response.status_code, 400)

    def test_song_new_valid_entry(self):
        # Ensures valid input means 201
        data = {
            'name_of_song': "love python" + str(test_instance_number),
            'duration_of_song': 3,
            'uploaded_time': str(datetime.utcnow())
            
        }
        response = requests.post(url, headers={'Content-Type': 'application/json'}, data=json.dumps(data))
        self.assertEqual(response.status_code, 201)

    def test_zc_song_new_entry_exist(self):
        #Ensures existed transaction inputs gives transaction already exists message
        data = {
            'name_of_song': "love python" + str(test_instance_number),
            'duration_of_song': 3,
            'uploaded_time': str(datetime.utcnow())
        }
        response = requests.post(url, headers={'Content-Type': 'application/json'}, data=json.dumps(data))
        res = response.json()
        self.assertEqual(response.status_code, 409)
        self.assertEqual(res['message'], "Song already exist")


if __name__ == '__main__':
    unittest.main()