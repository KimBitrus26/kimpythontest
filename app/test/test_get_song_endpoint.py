from unittest import TestCase
import unittest
import requests
import random

test_instance_number = random.randint(0, 200000)
base_url = 'http://127.0.0.1:5000' # can be changed to real server domain later
valid_entry_id = 2


class TestsForGetSongEndpoint(TestCase):

    def test_song_get_all(self):
        response = requests.get(base_url + '/song')
        self.assertEqual(response.status_code, 200)

    def test_song_get_invalid_id(self):
        # Ensures invalid ID gives 404 error
        response = requests.get(base_url + '/song/7777')
        self.assertEqual(response.status_code, 404)

    def test_song_get_valid_id(self):
        # Ensures valid ID gives 200
        response = requests.get(base_url + '/song/{}'.format(valid_entry_id))
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()