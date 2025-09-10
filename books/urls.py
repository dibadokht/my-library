from django.urls import path

from books.views import books_list

urlpatterns = [
    path('list/', books_list)
]