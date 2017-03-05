from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from cybersee.servers.models import Server, Game, ServerLog
from cybersee.users.models import User


class TestGameAPI(APITestCase, APIClient):
    fixtures = [
        './cybersee/servers/fixtures/servers.json',
        './cybersee/users/fixtures/users.json'
    ]

    def test_create_game(self):
        self.client.login(username='Test', password='testing123')

        data = {"name": "Rust", "description": "Rust Game"}
        response = self.client.post('/api/v1/games/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Game.objects.get(pk=response.data['pk']).name, "Rust")
        self.assertEqual(Game.objects.get(pk=response.data['pk']).description, "Rust Game")

    def test_list_games(self):
        self.client.login(username='Test', password='testing123')

        response = self.client.get('/api/v1/games/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 2)

    def test_game_delete(self):
        self.client.login(username='Test', password='testing123')

        response = self.client.delete('/api/v1/games/2/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class TestServerAPI(APITestCase, APIClient):
    fixtures = [
        './cybersee/servers/fixtures/servers.json',
        './cybersee/metrics/fixtures/metrics.json',
        './cybersee/users/fixtures/users.json'
    ]

    def test_create_server(self):
        self.client.login(username='Test', password='testing123')

        user = User.objects.get(username="Test").pk
        data = {"name": "Rust Server", "ip_address": "255.255.255.255", "description": "Rust Game", "owner": user, "game": 2}
        response = self.client.post('/api/v1/servers/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Server.objects.get(pk=response.data['pk']).name, "Rust Server")
        self.assertEqual(Server.objects.get(pk=response.data['pk']).game.name, "Arma 2")

    def test_create_server_fail(self):
        self.client.login(username='Test', password='testing123')

        user = User.objects.get(username="Test").pk
        data = {"name": "Rust", "ip_address": "255.255.255.255", "description": "Rust Game", "owner": user}
        response = self.client.post('/api/v1/servers/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(str(response.data), "{'game': ['This field is required.']}")

    def test_server_fetch(self):
        self.client.login(username='Test', password='testing123')

        response = self.client.get('/api/v1/servers/6749b1b0-39c1-4f79-babb-3092cb0dda22/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['game'], 1)
        self.assertEqual(response.data['owner'], 1)

    def test_server_delete(self):
        self.client.login(username='Test', password='testing123')

        response = self.client.delete('/api/v1/servers/8f93e773-cbaa-45f4-94c9-a4609af30164/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class TestSereverLogAPI(APITestCase, APIClient):
    fixtures = [
        './cybersee/servers/fixtures/servers.json',
        './cybersee/users/fixtures/users.json'
    ]

    def test_create_log(self):
        self.client.login(username='Test', password='testing123')

        data = {"server": "6749b1b0-39c1-4f79-babb-3092cb0dda22", "message": "Bob the Builder Can We Test It Yes We Can"}
        response = self.client.post('/api/v1/server-logs/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ServerLog.objects.get(pk=response.data['pk']).message, "Bob the Builder Can We Test It Yes We Can")

    def test_list_log(self):
        self.client.login(username='Test', password='testing123')

        response = self.client.get('/api/v1/server-logs/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 2)

    def test_log_delete(self):
        self.client.login(username='Test', password='testing123')

        response = self.client.delete('/api/v1/server-logs/2/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
