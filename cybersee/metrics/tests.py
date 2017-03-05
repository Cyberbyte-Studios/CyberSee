from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from cybersee.metrics.models import Metric, Reading
from cybersee.users.models import User


class TestMetricAPI(APITestCase, APIClient):
    fixtures = [
        './cybersee/servers/fixtures/servers.json',
        './cybersee/metrics/fixtures/metrics.json',
        './cybersee/users/fixtures/users.json'
    ]

    def test_create_metric(self):
        print ("\nTesting Metric Creation")
        self.client.login(username="Test", password="testing123")

        data = {"name": "Hype", "description": "The ammount of Hype"}
        response = self.client.post('/api/v1/metrics/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Metric.objects.get(pk=response.data['pk']).name, "Hype")
        self.assertEqual(Metric.objects.get(pk=response.data['pk']).description, "The ammount of Hype")

    def test_create_metric_fail(self):
        print ("\nTesting Metric Creation Fail")
        self.client.login(username="Test", password="testing123")

        data = {}
        response = self.client.post('/api/v1/metrics/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_metric(self):
        print ("\nTesting Delete Metric (4)")
        self.client.login(username='Test', password='testing123')

        response = self.client.delete('/api/v1/metrics/4/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_metric_list(self):
        print ("\nTesting Metric List")
        self.client.login(username='Test', password='testing123')

        response = self.client.get('/api/v1/metrics/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 9)

class TestReadingAPI(APITestCase, APIClient):
    fixtures = [
        './cybersee/servers/fixtures/servers.json',
        './cybersee/metrics/fixtures/metrics.json',
        './cybersee/users/fixtures/users.json'
    ]

    def test_create_reading(self):
        print ("\nTesting Reading Creation")
        self.client.login(username="Test", password="testing123")

        data = {"metric": 3, "value": "35", "server": "48850ef1-6d19-4b14-8d93-18b60f0157fa"}
        response = self.client.post('/api/v1/readings/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Reading.objects.get(pk=response.data['pk']).value, 35.0)

    def test_create_reading_fail(self):
        print ("\nTesting Reading Creation Fail")
        self.client.login(username="Test", password="testing123")

        data = {"value": "35", "server": "48850ef1-6d19-4b14-8d93-18b60f0157fa"}
        response = self.client.post('/api/v1/readings/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_metric(self):
        print ("\nTesting Delete Metric (4)")
        self.client.login(username='Test', password='testing123')

        response = self.client.delete('/api/v1/readings/4/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_reading_list(self):
        print ("\nTesting Reading List")
        self.client.login(username='Test', password='testing123')

        response = self.client.get('/api/v1/readings/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 11)
