from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'testapp/메인화면.html', {})

def safety(request):
    return render(request, 'testapp/sobanganjeon.html', {})

def statics(request):
    return render(request, 'testapp/post_list.html', {})

def location(request):
    return render(request, 'testapp/location.html', {})

def setting(request):
    return render(request, 'testapp/setting.html', {})

def popup(request):
    return render(request, 'testapp/popup.html', {})