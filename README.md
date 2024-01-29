# todo-list
Django ToDo List

###### How to create items
from app.models import Item, ToDoList
print(ToDoList.objects.all()) 
print(list1.item_set.all())
list1.item_set.create(text="Go to the mall", complete=False)

removed:
psycopg2==2.9.9
psycopg2-binary==2.9.6

from django.contrib.auth.models import User
users = User.objects.all()
user = User.objects.filter(is_superuser=True)

