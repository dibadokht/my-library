from django.urls import path

from books.views import books_list,books_json


urlpatterns = [
    path('list/', books_list),
    path('json/' , books_json),
]