from django.shortcuts import render
from django.views.generic.edit import CreateView
from . models import Finch

# Create your views here.
# finches = [
#     {
#         'breed': 'yellow',
#         'region': 'North America',
#     },
#     {
#         'breed': 'brown',
#         'region': 'Southern US'
#     }
# ]

def home(request):
    #unlike with EJS, we need our .html file extension
    return render(request, "home.html")

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', {'finches': finches})

def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    return render(request, 'finches/detail.html', {'finch': finch})

class FinchCreate(CreateView):
    model = Finch
    fields = '__all__'
    success_url = '/finches'