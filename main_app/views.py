from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from . models import Finch
from . forms import FeedingForm

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
    feeding_form = FeedingForm()
    return render(request, 'finches/detail.html', {'finch': finch, 'feeding_form': feeding_form})



class FinchCreate(CreateView):
    model = Finch
    fields = '__all__'
    success_url = '/finches'

class FinchUpdate(UpdateView):
    model = Finch
    fields = ['species', 'classification', 'region']

class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches'


def add_feeding(request, finch_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.finch_id = finch_id
        new_feeding.save()
    return redirect('detail', finch_id=finch_id)