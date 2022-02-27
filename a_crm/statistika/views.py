from django.shortcuts import render
from django.db.models import Count
import datetime
from qsstats import QuerySetStats
from klients.models import Klients
import pdb


def view_func(request):
    end_date = datetime.date.today()
    start_date = end_date - datetime.timedelta(days=30)
    queryset = Klients.objects.all()
    qsstats = QuerySetStats(queryset, date_field='created', aggregate=Count('id'))
    values = qsstats.time_series(start_date, end_date, interval='days')
    return render(request,'statistika.html', {'values': values})
