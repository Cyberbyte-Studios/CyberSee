from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from cybersee.payments.models import Plan
from cybersee.users.models import User


class TestPlanAPI(APITestCase, APIClient):
    fixtures = [
        './cybersee/servers/fixtures/servers.json',
        './cybersee/metrics/fixtures/metrics.json',
        './cybersee/payments/fixtures/payments.json',
        './cybersee/users/fixtures/users.json'
    ]

    def test_create_plan(self):
        print ("\nTesting Plan Creation")
        self.client.login(username="Test", password="testing123")

        data = {"name": "Hype", "price": 35.99, "retention": "5", "metrics": [3, 5, 7], "hidden": False, "enabled": True}
        response = self.client.post('/api/v1/payments/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Plan.objects.get(pk=response.data['pk']).name, "Hype")
        self.assertEqual(Plan.objects.get(pk=response.data['pk']).retention, 5)

    def test_create_plan_fail(self):
        print ("\nTesting Plan Creation Fail")
        self.client.login(username="Test", password="testing123")

        data = {"name": "Hype", "retention": "5"}
        response = self.client.post('/api/v1/payments/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_plan(self):
        print ("\nTesting Delete Plan (2)")
        self.client.login(username='Test', password='testing123')

        response = self.client.delete('/api/v1/payments/2/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_plan_list(self):
        print ("\nTesting Plan List")
        self.client.login(username='Test', password='testing123')

        response = self.client.get('/api/v1/payments/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 2)
