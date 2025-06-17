from django.shortcuts import render

def home_view(request):
    images = ["1.JPG", "2.JPG", "3.JPG", "4.JPG", "5.JPG", "6.JPG"]
    return render(request, 'base.html', {'images': images})