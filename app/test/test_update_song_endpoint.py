import random
from unittest import TestCase
import unittest 
import requests
import json
from datetime import datetime

test_instance_number = random.randint(0, 200000)
base_url = 'http://127.0.0.1:5000' # can be changed to real server domain later


class Test_For_Update_Endpoint(TestCase):

    def test_update_song_new_valid_entry(self):
        # Ensures valid input means 200
        data = {
            'name_of_song': "play python" + str(test_instance_number),
            'duration_of_song': 4,
            'uploaded_time': str(datetime.utcnow())
        }
        response = requests.put(base_url + '/song/2',
                                    headers={'Content-Type': 'application/json'}, data=json.dumps(data))
        res = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res['msg'], "Song updated successfully")

    def test_update_song_invalid_id(self):
        #Ensures wrong transaction id inputs gives 
        data = {
            'name_of_song': "play python" + str(test_instance_number),
            'duration_of_song': 4,
            'uploaded_time': str(datetime.utcnow())
        }
        response = requests.put(base_url + '/song/33333',
                                    headers={'Content-Type': 'application/json'}, data=json.dumps(data))
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()