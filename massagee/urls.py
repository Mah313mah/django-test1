from django.urls import path
#from .views import mess_tabeView
#urlpatterns = [
#    path('',mess_tabeView, name= 'mess'),

#]
#_________________________________________________

from .views import MessView

urlpatterns = [
    path('',MessView.as_view(), name= 'mess'),

]


