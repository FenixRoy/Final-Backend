from django.urls import path, include
from rest_framework.routers import DefaultRouter
from gestion.views import EquipoAPIView, ColaboradorAPIView, ColaboradoresAPIView, AsignacionesAPIView, TecnicosAPIView, AsignacionAPIView  

router = DefaultRouter()

urlpatterns = [
    path('equipos/', EquipoAPIView.as_view(), name='equipos'),
    path('colaboradores/', ColaboradoresAPIView.as_view(), name='colaboradores'),
    path('colaborador/<int:dni>/', ColaboradorAPIView.as_view(), name='colaborador'),
    path('tecnicos/', TecnicosAPIView.as_view(), name='tecnicos'),
    path('asignaciones/', AsignacionesAPIView.as_view(), name='asignaciones'),
    path('asignacion/<int:id>/', AsignacionAPIView.as_view(), name='asignacion'),
]



#urlpatterns = [
    #path('api/equipos/', EquipoViewSet.as_view(), name='equipos'),
    #path('api/colaboradores/', ColaboradorViewSet.as_view(), name='colaboradores'),
#]


