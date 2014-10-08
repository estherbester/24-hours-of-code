from django.shortcuts import render

def placeholder(request):
  return render(request, "teaser/placeholder.html")
