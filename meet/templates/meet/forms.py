
'''
from django import forms 
from meet.models import Meetings

class MeetingsForm(forms.ModelForm):
	class Meta:
		model = Meetings
		fields = "__all__"

		'''