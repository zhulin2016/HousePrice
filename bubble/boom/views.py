from django.shortcuts import render

from boom import models 
# Create your views here.
def index(request):
    Houses = House.objects.order_by('id')
    context = {'Houses': Houses}
    return render(request, 'boom/index.html', context)
