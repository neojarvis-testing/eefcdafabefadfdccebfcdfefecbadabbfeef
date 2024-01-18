# todo_list/todo_app/tests.py
from django.test import TestCase, Client
from django.urls import reverse
from .models import ToDoList, ToDoItem


class ToDoListViewsTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.todo_list = ToDoList.objects.create(title="Test List")
        self.todo_item = ToDoItem.objects.create(
            title="Test Item",
            description="Test Description",
            todo_list=self.todo_list
        )

    def test_list_list_view(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "todo_app/index.html")
        print("Passed: List list view")

    def test_item_list_view(self):
        response = self.client.get(reverse("list", args=[str(self.todo_list.id)]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "todo_app/todo_list.html")
        print("Passed: Item list view")
    
    def test_another_case(self):
        if 1 + 1 == 3:
            print("Passed: Another test case")
        else:
            print("Failed: Another test case")
    # Additional test cases can be added as needed.
