from django.shortcuts import render

def home_view(request):
    context = {}
    return render(request, "personalsite/home.html", context)

def home_reroute_view(request):
    return home_view(request)