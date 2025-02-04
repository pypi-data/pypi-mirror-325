import time
from base64 import b64encode
from unittest import TestCase

from .. import AdressApi, SearchResponse


WAIT_TIME = 0.2

class TestAdress(TestCase):
    def setUp(self) -> None:
        self.api = AdressApi()
        return super().setUp()
    
    def test_issue_marseille(self):
        time.sleep(WAIT_TIME)
        r = self.api.search(q="marseille")
        self.assertTrue(r.status_code == 200)

        data = r.json()
        print(data)
        SearchResponse(**data)
    
    def test_issue_metz(self):
        time.sleep(WAIT_TIME)
        r = self.api.search(q="metz")
        self.assertTrue(r.status_code == 200)

        data = r.json()
        print(data)
        SearchResponse(**data)

    def test_issue_marseille(self):
        time.sleep(WAIT_TIME)
        r = self.api.search(q="MARSEILLE")
        self.assertTrue(r.status_code == 200)

        data = r.json()
        print(data)
        SearchResponse(**data)