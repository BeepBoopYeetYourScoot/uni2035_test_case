from rest_framework.test import APITestCase, APIClient
from .request_bodies import REGION_POST_BODY


class RegionTestCase(APITestCase):
    fixtures = ['/regions/tests/fixtures.json']

    def setUp(self) -> None:
        self.client = APIClient()
        self.region_endpoint_path = '/api/v1/region'
        self.city_endpoint_path = '/api/v1/city'

    def test_list(self):
        self.client.get(self.region_endpoint_path)
        self.assertEqual()

    def test_retrieve(self):
        pass

    def test_create(self):
        self.client.login(username='admin', password='admin')
        response = self.client.post(self.region_endpoint_path, REGION_POST_BODY, format='json')
        self.assertEqual(response.status_code, 201)

    def test_create_unauthenticated(self):
        response = self.client.post(self.region_endpoint_path, REGION_POST_BODY, format='json')
        self.assertEqual(response.status_code, 401)

    def test_update(self):
        pass

    def test_delete(self):
        pass
