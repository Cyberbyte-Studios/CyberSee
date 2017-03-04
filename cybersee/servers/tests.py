from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from cybersee.servers.models import Server, Game
from cybersee.users.models import User

class TestGameAPI(APITestCase, APIClient):
    fixtures = [
        './cybersee/servers/fixtures/servers.json',
        './cybersee/users/fixtures/users.json'
    ]

    def test_create_game(self):
        print ("Testing Game Creation")
        self.client.login(username='Test', password='testing123')

        data = {"name": "Rust", "description": "Rust Game"}
        response = self.client.post('/api/v1/games/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Game.objects.get(pk=response.data['pk']).name, "Rust")
        self.assertEqual(Game.objects.get(pk=response.data['pk']).description, "Rust Game")

    def test_list_games(self):
        print ("Testing Game List")
        self.client.login(username='Test', password='testing123')

        response = self.client.get('/api/v1/games/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 2)


class TestServerAPI(APITestCase, APIClient):
    fixtures = [
        './cybersee/servers/fixtures/servers.json',
        './cybersee/metrics/fixtures/metrics.json',
        './cybersee/users/fixtures/users.json'
    ]

    def test_create_server(self):
        print ("Testing Server Creation")
        self.client.login(username='Test', password='testing123')

        user = User.objects.get(username="Test").pk
        data = {"name": "Rust Server", "ip_address": "255.255.255.255", "description": "Rust Game", "owner": user, "metrics": [3, 5, 7], "game": 2}
        response = self.client.post('/api/v1/servers/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Server.objects.get(pk=response.data['pk']).name, "Rust Server")
        self.assertEqual(Server.objects.get(pk=response.data['pk']).game.name, "Arma 2")

    def test_create_server_fail(self):
        print ("Testing Server Creation Fail")
        self.client.login(username='Test', password='testing123')

        user = User.objects.get(username="Test").pk
        data = {"name": "Rust", "ip_address": "255.255.255.255", "description": "Rust Game", "owner": user, "game": 2, "owner": user}
        response = self.client.post('/api/v1/servers/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(str(response.data), "{'metrics': ['This field is required.']}")
