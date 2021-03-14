import unittest
import random
from unittest import TestCase
import requests
import json
from datetime import datetime

test_instance_number = random.randint(0, 200000)
base_url = 'http://127.0.0.1:5000' # can be changed to real server domain later
valid_entry_id = 2


class TestsForDeleteSongEndpoint(TestCase):

    def test_song_delete_valid_id(self):
        # Ensures valid ID gives 200
        response = requests.delete(base_url + '/song/{}'.format(valid_entry_id))
        self.assertEqual(response.status_code, 200)
        
    def test_delete_song_with_wrong_entry_type(self):
        #Ensures wrong string id id gives 404 
        response = requests.delete(base_url + '/song/dwg')
        self.assertEqual(response.status_code,404)

    def test_delete_song_with_wrong_entry2(self):
        #Ensures wrong id id gives 404 
        response = requests.delete(base_url + '/song/222222')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main() 
        