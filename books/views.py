from django.http.response import HttpResponse , JsonResponse

def books_list(request):
    books = ["book1" , "book2" , "book3"]
    books_str = " ".join(books)
    return HttpResponse(books_str)

def books_json(request):
    books = [{"title":"book1"},
             {"title":"book2"}]
    return JsonResponse({"books":books})
    