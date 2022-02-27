from django.shortcuts import render, redirect
from django.views.generic import ListView, View
from django.http import JsonResponse
from klients.models import Klients
from services.models import Servise
import pdb


class TableKlients(ListView):
    model = Klients
    template_name = 'klients.html'
    context_object_name = 'klients'

    def get_context_data(self, **kwargs):
        context = super(TableKlients, self).get_context_data(**kwargs)
        context['allservise'] = Servise.objects.all()
        return context


class AddKlient(View):
    def get(self, request):
        f_name1 = request.GET.get('f_name',None)
        l_name1 = request.GET.get('l_name',None)
        town1 = request.GET.get('town',None)
        school1 = request.GET.get('school',None)
        telephone1 = request.GET.get('telephone',None)
        servise1 = (request.GET.get('servise',None)).split(',') 
        status1 = request.GET.get('status',None)
        istochnik1 = request.GET.get('istochnik',None)
        
        obj = Klients.objects.create(
            f_name = f_name1,
            s_name = l_name1,
            town = town1,  
            school = school1,
            telephone = telephone1,
            status = status1,
            istochnik = istochnik1,
        )
        t1 = Servise.objects.filter(id__in = servise1)
        obj.servise.add(*t1)
        t_obj = ''
        for i in obj.servise.all():
            t_obj = t_obj + str(i) + '\n'
        klient = {'id':obj.id,'f_name':obj.f_name,'s_name':obj.s_name,'town':obj.town,'school':obj.school,'telephone':obj.telephone,'t_obj':t_obj,'status':obj.status,'istochnik':obj.istochnik}
        data = {
            'klient': klient
        }
        return JsonResponse(data)

class UpdateKlients(View):
    def get(self, request):
        id1 = request.GET.get('id', None)
        f_name1 = request.GET.get('f_name',None)
        l_name1 = request.GET.get('l_name',None)
        town1 = request.GET.get('town',None)
        school1 = request.GET.get('school',None)
        telephone1 = request.GET.get('telephone',None)
        servise1 = (request.GET.get('servise',None)).split(',') 
        status1 = request.GET.get('status',None)
        istochnik1 = request.GET.get('istochnik',None)
        obj = Klients.objects.get(id=id1)
        obj.f_name = f_name1
        obj.s_name = l_name1
        obj.town = town1
        obj.school = school1
        obj.telephone = telephone1
        obj.status = status1
        obj.istochnik = istochnik1
        obj.save()
        t_obj = ''
        if servise1 != ['']:
            t1 = Servise.objects.filter(id__in = servise1)
            obj.servise.clear()
            obj.servise.add(*t1)
            for i in obj.servise.all():
                t_obj = t_obj + str(i) + '\n'
        obj.save()
        klient = {'id':obj.id,'f_name':obj.f_name,'s_name':obj.s_name,'town':obj.town,'school':obj.school,'telephone':obj.telephone,'t_obj':t_obj,'status':obj.status,'istochnik':obj.istochnik}

        data = {
            'klient': klient
        }
        return JsonResponse(data)

class EditKlients(View):
    def get(self, request):
        id1 = request.GET.get('id', None)
        obj = Klients.objects.get(id=id1)
        klient = {'id':obj.id,'f_name':obj.f_name,'s_name':obj.s_name,'town':obj.town,'school':obj.school,'telephone':obj.telephone,'status':obj.status,'istochnik':obj.istochnik}

        data_edit = {
            'klient': klient
        }
        
        return JsonResponse(data_edit)

class DeleteKlients(View):
    def get(self, request):
        id1 = request.GET.get('id', None)
        Klients.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)




# def klients_table(request):
#     allklients = Klients.objects.all()
#     form_k = KlientForm()
#     if request.method == "POST":
#         form_k = KlientForm(request.POST)
#         if form_k.is_valid():
#             form_k.save()
#             return redirect('klients_table')
#     return render(request,'klients.html',
#                   {'allklients': allklients,
#                   'form_k' : form_k })

# def klients_form(request):
#     return render(request, "klients.html",{})