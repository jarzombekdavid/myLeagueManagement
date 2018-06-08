from django.forms import ModelForm
from mlm.models import Season


class SeasonForm(ModelForm):
	class meta:
		model = Season
