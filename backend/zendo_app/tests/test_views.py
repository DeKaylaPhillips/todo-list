from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from ..utilities.test_helpers import create_new_task


class TestTasksView(APITestCase):
    def setUp(self):
        self.url = reverse(viewname="task_views")

    def test_get_all_tasks_returns_200_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_tasks_returns_expected_fields(self):
        create_new_task({"title": "Task 1", "completed": False})
        create_new_task({"title": "Task 2", "completed": True})
        expected_data = [
            {"title": "Task 1", "completed": False},
            {"title": "Task 2", "completed": True},
        ]
        response = self.client.get(self.url)
        self.assertEqual(len(response.data), 2)
        for idx, task in enumerate(expected_data):
            self.assertEqual(response.data[idx]["title"], task["title"])
            self.assertEqual(response.data[idx]["completed"], task["completed"])
            self.assertEqual(response["Content-Type"], "application/json")

    def test_get_all_tasks_when_no_tasks_exist(self):
        response = self.client.get(self.url)
        self.assertEqual(response.data, [])

    def test_post_create_new_task(self):
        request_data = {"title": "Task 3", "completed": True}
        response = self.client.post(path=self.url, data=request_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], request_data["title"])
        self.assertEqual(response.data["completed"], request_data["completed"])
