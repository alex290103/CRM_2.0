from django.shortcuts import render,redirect
from django.views.generic import ListView, View, DetailView
from django.http import JsonResponse
from services.models import Servise
from teachers.models import Teachers
import pdb

class ServiseView(ListView):
    model = Servise
    template_name = 'servises.html'
    context_object_name = "servises"

    def get_context_data(self, **kwargs):
        context = super(ServiseView, self).get_context_data(**kwargs)
        context['teachers'] = Teachers.objects.all()
        return context


class CreateServise(View):
    def get(self, request):
        name1 = request.GET.get('name',None)
        type1 = request.GET.get('type',None)
        teacher1 = (request.GET.get('teacher',None)).split(',') 
        obj = Servise.objects.create(
            name = name1,
            type = type1,
        )
        t1 = Teachers.objects.filter(id__in = teacher1)
        obj.teacher.add(*t1)
        t_obj = ''
        for i in obj.teacher.all():
            t_obj = t_obj + str(i) + '\n'
        servise = {'id':obj.id,'name':obj.name,'type':obj.type, 't_obj':t_obj}
        data = {
            'servise': servise
        }
        return JsonResponse(data)

class UpdateServise(View):
    def get(self, request):
        id1 = request.GET.get('id', None)
        name1 = request.GET.get('name', None)
        type1 = request.GET.get('type', None)
        teacher1 = (request.GET.get('teacher',None)).split(',') 
        obj = Servise.objects.get(id=id1)
        obj.name = name1
        obj.type = type1
        obj.save() 
        t_obj=''
        if teacher1 != ['']:
            t1 = Teachers.objects.filter(id__in = teacher1)
            obj.teacher.clear()
            obj.teacher.add(*t1)
            for i in obj.teacher.all():
                t_obj = t_obj + str(i) + '\n'
        obj.save()
        
        servise = {'id':obj.id,'name':obj.name,'type':obj.type,'t_obj':t_obj}

        data = {
            'servise': servise
        }
        return JsonResponse(data)

class DeleteServise(View):
    def get(self, request):
        id1 = request.GET.get('id', None)
        Servise.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)

class AddTeachers(View):
    def get(self, request):
        f_name = request.GET.get('f_name',None)
        s_name = request.GET.get('s_name',None)
        obj = Teachers.objects.create(
            f_name = f_name,
            s_name = s_name,
        )
        teacher = {'id':obj.id,'f_name':obj.f_name,'s_name':obj.s_name}
        data = {
            'teacher': teacher
        }
        return JsonResponse(data)
