from django.test import TestCase

from ..models import Task


class TestTaskModel(TestCase):
    def setUp(self):
        self.task = Task.objects.create(title="Test task.")

    def test_task_has_title_attribute(self):
        self.assertEqual(self.task.title, "Test task.")

    def test_task_has_default_false_completed_value(self):
        self.assertFalse(self.task.completed)

    def test_task_has_string_representation(self):
        self.assertEqual(str(self.task), "Test task.")
