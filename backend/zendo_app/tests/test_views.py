import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from ..models import Task


class TestTasksView(APITestCase):
    def setUp(self):
        self.url = reverse(viewname="task_views")

    def test_get_returns_200_OK_status_code_when_tasks_retrieved(self):
        Task.objects.create(title="Task 1", completed=True)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_returns_correct_field_data_when_called(self):
        Task.objects.create(title="Task 2", completed=True)
        response = self.client.get(self.url)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Task 2")
        self.assertEqual(response.data[0]["completed"], True)
        self.assertEqual(response["Content-Type"], "application/json")

    def test_post_returns_200_OK_status_code_when_no_tasks_found(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_returns_error_message_when_no_tasks_found(self):
        response = self.client.get(self.url)
        self.assertEqual(response.data, "No tasks found in list.")

    def test_post_returns_201_CREATED_status_code_when_task_created(self):
        request_data = {"title": "Task 2", "completed": True}
        response = self.client.post(path=self.url, data=request_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_returns_correct_field_data_when_task_created(self):
        request_data = {"title": "Task 3", "completed": True}
        response = self.client.post(path=self.url, data=request_data, format="json")
        self.assertEqual(response.data["title"], request_data["title"])
        self.assertEqual(response.data["completed"], request_data["completed"])

    def test_post_returns_400_BAD_REQUEST_status_code_when_task_data_invalid(self):
        request_data = {"title": "", "completed": False}
        response = self.client.post(
            self.url, data=json.dumps(request_data), content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_returns_error_message_when_task_data_invalid(self):
        request_data = {"title": "", "completed": False}
        response = self.client.post(
            self.url, data=json.dumps(request_data), content_type="application/json"
        )
        self.assertEqual(response.data, "This field may not be blank.")
