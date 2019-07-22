from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# meet is app name
def index(request):
	return render(request, 'meet/index.html')
