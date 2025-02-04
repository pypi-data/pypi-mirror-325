import time
from unittest import TestCase

import requests

from .. import RegionApi, RegionsResponse

WAIT_TIME = 0.2


class TestRegion(TestCase):
    def setUp(self) -> None:
        self.api = RegionApi()
        return super().setUp()

    def test_regions(self) -> requests.Response:
        time.sleep(WAIT_TIME)

        r = self.api.regions(limit=5)
        self.assertTrue(r.status_code == 200)
        r = self.api.regions(nom="Mar", limit=5)
        self.assertTrue(r.status_code == 200)
        return r

    def test_regions_by_code(self) -> None:
        time.sleep(WAIT_TIME)
        r = self.api.regions_by_code(code=75)
        self.assertTrue(r.status_code == 200)

    def test_regions_response(self) -> None:
        results = [RegionsResponse(**r) for r in self.test_regions().json()]
        assert len(results) > 0

    def test_regions_by_domtom(self) -> None:
        time.sleep(WAIT_TIME)
        r = self.api.regions_by_code(code=6)
        self.assertTrue(r.status_code == 200)
