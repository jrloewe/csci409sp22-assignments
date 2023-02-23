from django.http import HttpResponse


def index(request):
    return HttpResponse('Hello from airports')


def airport_info(request, airport_code):
    return HttpResponse(f'Showing info for airport: {airport_code}')
