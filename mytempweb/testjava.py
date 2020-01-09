from django.http import HttpResponse
def display(request):
    op = request.GET.get('t','default')
    print(op)
    return HttpResponse("thank you display")