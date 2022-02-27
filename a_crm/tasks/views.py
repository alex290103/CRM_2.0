from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, View
from django.http import JsonResponse
from tasks.models import Tasks
from klients.models import Klients
from datetime import date, datetime
from django.utils import dateformat
from a_crm import settings
import pdb

class TaskView(ListView):
    model = Tasks
    template_name = 'tasks.html'

    def get_context_data(self, **kwargs):
        context = super(TaskView, self).get_context_data(**kwargs)
        print(date.today())
        if self.request.user.is_authenticated:
            context['tasks']= Tasks.objects.filter(hr_manager=self.request.user)
            context['nowdata'] = date.today()
        context['allklients'] = Klients.objects.all()
        return context




class CreateTask(View):
    def get(self, request):
        klient1 = request.GET.get('klient',None)
        task1 = request.GET.get('task',None)
        deadline1 = request.GET.get('deadline',None)
        obj = Tasks.objects.create(
            klient = Klients.objects.get(id=klient1),
            task = task1,
            deadline = deadline1,
            hr_manager = request.user,
        )
        date = datetime.strptime(obj.deadline,"%Y-%m-%d")
        date_obj = dateformat.format(date, settings.DATE_FORMAT)
        task = {'id':obj.id,'f_name':obj.klient.f_name,'s_name':obj.klient.s_name, 'task':obj.task, 'deadline':date_obj,'checked':'False'}
        data = {
            'task': task
        }
        return JsonResponse(data)

class OnCheck(View):
    def get(self, request):
        id1 = request.GET.get('id', None)
        obj = Tasks.objects.get(id=id1)
        if obj.checked == False:
            obj.checked = True
        else:
            obj.checked = False
        obj.save()
        return HttpResponse('All is ok')

class EditTask(View):
    def get(self, request):
        id1 = request.GET.get('id', None)
        obj = Tasks.objects.get(id=id1)
        task = {'id':obj.id,'date':obj.deadline,}
        data = {
            'task': task
        }
        return JsonResponse(data)



class UpdateTask(View):
    def get(self, request):
        id1 = request.GET.get('id', None)
        klient1 = request.GET.get('klient',None)
        task1 = request.GET.get('task',None)
        deadline1 = request.GET.get('deadline',None)
        obj = Tasks.objects.get(id=id1)
        obj.klient = Klients.objects.get(id=klient1)
        obj.task = task1
        obj.deadline = deadline1
        obj.save()
        task = {'id':obj.id,'f_name':obj.klient.f_name,'s_name':obj.klient.s_name,'task':obj.task,'deadline':obj.deadline}
        data = {
            'task': task
        }
        return JsonResponse(data)

class DeleteTask(View):
    def get(self, request):
        id1 = request.GET.get('id', None)
        Tasks.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)