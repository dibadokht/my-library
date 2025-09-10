from django.http.response import HttpResponse , JsonResponse

def books_list(request):
    books = ["book1" , "book2" , "book3"]
    books_str = " ".join(books)
    return HttpResponse(books_str)
