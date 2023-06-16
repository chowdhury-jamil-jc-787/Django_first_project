from django.http import HttpResponse


def employee(request):
    return HttpResponse("This is Employee module home Page")
def profile(request):
    return HttpResponse("This is Employee profile module home Page")

