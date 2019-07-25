from django.shortcuts import render, redirect 
from django.http import HttpResponse
#from .models import Post
#from meet.forms import MeetingsForm
#from meet.models import Meetings

# Create your views here.


# meet is app name
def index(request):
	return render(request, 'meet/index.html')


def upload(request):
	print("hello")
	name = request.POST['name']
	mobile = request.POST['mobile']
	email = request.POST['email']
	title = request.POST['title']
	message = request.POST['message']
	#image = request.POST['image']
	created_on = request.POST['created_on']
	c= Post(name=name,mobile=mobile, email = emil, title = title, message = message, image = image, created_on = created_on)
	c.save()
 
	return render(request,'meet/index.html')


'''
def met(request):
	if request.method == "POST":
		form = MeetingsForm(request.POST)
		if form.is_valid():
			try:
				form.save()
				return redirect()
			except:
				pass

	else:
		form = MeetingsForm()
	return render(request, 'meet/index.html', {'form': form})


def show(request):
	meetings = Meetings.objects.all()
	return render(request, "meet/index.html", {'meetings': meetings})
'''