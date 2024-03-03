#from django.http import HttpResponse
#from django.shortcuts import render


#def mess_tabeView(request):
#    return HttpResponse('مهدی')

#def mess_tabeView(request):
#    return render(request, 'home.html')
#______________________________________________

#from django.views import View



#class MessView(View):
#    def get(self, request):
#        return render(request, 'home.html')
    
#_______________________________________________
    
#from django.views.generic import TemplateView

#class MessView(TemplateView):
#    template_name = 'home.html'
#____________________________________________________
    
from django.views.generic import ListView
from .models import Mod_mess


class MessView(ListView):
    model = Mod_mess
    template_name = 'home.html'
    context_object_name = "Mod_mess_list"
