from django.shortcuts import render

def  index(request):
    return render(request, 'index.html')
def  predict(request):
    return render(request, 'predict.html')