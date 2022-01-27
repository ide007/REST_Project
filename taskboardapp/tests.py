from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APITestCase
from usersapp.views import UserModelViewSet
from usersapp.models import User
from .models import WorkProject, TaskBoard
from mixer.backend.django import mixer


class TestViews(APITestCase):    #TestCase

    def setUp(self):
        self.admin = User.objects.create_superuser('admin', email='adm@gamil.com', password='123')

    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.post('/api/users/', {
            "user_name": "vanya",
            "first_name": "Ivan",
            "last_name": "Ivanov",
            "email": "ivanov@email.com",
            "password": "123"
        })
        force_authenticate(request, user=self.admin)
        view = UserModelViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        request = factory.get('/api/users/')
        force_authenticate(request, user=self.admin)
        view = UserModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_client_get_list(self):
        client = APIClient()
        client.force_authenticate(user=self.admin)
        project = mixer.blend(WorkProject)
        task = mixer.blend(TaskBoard)
        response = client.get('/api/project/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['repository_link'], project.repository_link)
        response = client.get('/api/taskboard/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['task_title'],
                         task.task_title)
        # response = client.post('/api/project/', {
        #     'name': 'теститрование',
        #     'repository_link': 'http://test.link.com',
        #     'project_user': 1,
        # })
        # self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        client.logout()
        response = client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
