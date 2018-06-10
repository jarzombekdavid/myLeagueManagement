from django.forms import ModelForm
from mlm.models import Season
from mlm.models import Team


class SeasonForm(ModelForm):
	class meta:
		model = Season
		fields = ['name','draft_date']

class TeamForm(ModelForm):
	class meta:
		model = Team
		fields = ['name','Season','user1','user2','multi_user']
