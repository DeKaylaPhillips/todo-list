from django.test import TestCase

from .models import Task


class TestTaskModel(TestCase):
    def setUp(self):
        """Creates a new task."""
        self.task = Task.objects.create(title="Test task.")

    def test_title_creation(self):
        """Tests that a new task item has been successfully added to the todo list."""
        self.assertEqual(self.task.title, "Test task.")

    def test_task_completed_value(self):
        """Tests that a task is NOT complete by default on creation."""
        self.assertFalse(self.task.completed)
        
    def test_task_string_representation(self):
        """Tests the string representation of a task in a todo list."""
        self.assertEqual(str(self.task), "Test task.")