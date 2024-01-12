from django.shortcuts import render

# Create your views here.
finches = [
    {
        'breed': 'yellow',
        'region': 'North America',
    },
    {
        'breed': 'brown',
        'region': 'Southern US'
    }
]

def home(request):
    #unlike with EJS, we need our .html file extension
    return render(request, "home.html")

def about(request):
    return render(request, 'about.html')