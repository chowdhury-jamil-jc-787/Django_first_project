from django.http import HttpResponse


def home(request):
    return HttpResponse("This is home Page")

# def about(request):
#     data = "Database theke data retrieve kora hoise"
#     return HttpResponse(f"This is about Page {data}")

# def contact(request):
#     return HttpResponse("This is contact Page")
