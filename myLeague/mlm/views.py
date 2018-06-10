from django.shortcuts import render
from models import Season
from models import SeasonForm
from django.forms import modelformset_factory
from django.http import HttpResponse


def index(request):

    return HttpResponse("Hello, world. You're at the 2kleague.")


def seasons(request):

	season_list = Season.objects.all()


def create_season(request):

	SeasonFormSet = modelformset_factory(Season, fields=('name', 'draft_date'))
    if request.method == 'POST':
        formset = SeasonFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            # do something.
    else:
        formset = SeasonFormSet()
    return render(request, 'create_season.html', {'formset': formset})