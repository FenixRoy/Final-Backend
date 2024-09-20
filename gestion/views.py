from rest_framework.views import APIView
from rest_framework.response import Response
#from rest_framework.serializers import ModelSerializer 
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from gestion.serializers import EquipoSerializer, ColaboradorSerializer, AsignacionSerializer, TecnicoSerializer
from gestion.models import equipo, colaborador, tecnico, asignacion

class EquipoAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        # Se obtienen los datos de la solicitud
        data = request.data        
        # Se crea un serializador con los datos recibidos
        serializer = EquipoSerializer(data=data)        
        # Se valida el serializador
        validacion = serializer.is_valid()        
        if validacion:
            # Si los datos son válidos, se guarda el nuevo equipo
            nuevo_equipo = serializer.save()            
            # Se serializa el nuevo equipo para la respuesta
            resultado = EquipoSerializer(instance=nuevo_equipo)            
            # Se devuelve una respuesta exitosa
            return Response(data={
                'MENSAJE': 'Equipo creado correctamente',
                'Equipo': resultado.data
                }, status=status.HTTP_201_CREATED)
        else:
            # Si los datos no son válidos, se devuelve una respuesta de error
            return Response(data={
                'MENSAJE': 'Equipo no creado',
                'Errores': serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        equipos = equipo.objects.all()
        serializer = EquipoSerializer(equipos, many=True)
        return Response(serializer.data)


class ColaboradoresAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data
        serializer = ColaboradorSerializer(data=data)
        validacion = serializer.is_valid()
        if validacion:
            nuevo_colaborador = serializer.save()
            resultado = ColaboradorSerializer(instance=nuevo_colaborador)
            return Response(data={
                'MENSAJE': 'Colaborador creado correctamente',
                'Colaborador': resultado.data
                }, status=status.HTTP_201_CREATED)
        else:
            return Response(data={
                'MENSAJE': 'Colaborador no creado',
                'Errores': serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        colaboradores = colaborador.objects.all()
        serializer = ColaboradorSerializer(colaboradores, many=True)
        return Response(serializer.data)

class ColaboradorAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, dni):
        try:
            colaboradorInstance = colaborador.objects.get(dni=dni)
            serializer = ColaboradorSerializer(colaboradorInstance)
            return Response(serializer.data)
        except colaborador.DoesNotExist:
            return Response(data={
                'MENSAJE': 'Colaborador no encontrado',
                }, status=status.HTTP_400_BAD_REQUEST)
        

class TecnicosAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data
        serializer = TecnicoSerializer(data=data)
        validacion = serializer.is_valid()
        if validacion:
            serializer.save()
            return Response(data={
                'MENSAJE': 'Técnico creado correctamente',
                'Técnico': serializer.data
                }, status=status.HTTP_201_CREATED)
        else:
            return Response(data={
                'MENSAJE': 'Técnico no creado',
                'Errores': serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)
        
    def get(self, request):
        tecnicos = tecnico.objects.all()
        serializer = TecnicoSerializer(tecnicos, many=True)
        return Response(serializer.data)

class AsignacionesAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data
        serializer = AsignacionSerializer(data=data)
        validacion = serializer.is_valid()
        if validacion:
            nueva_asignacion = serializer.save()    
            resultado = AsignacionSerializer(instance=nueva_asignacion)
            return Response(data={
                'MENSAJE': 'Asignación creada correctamente',
                'Asignación': resultado.data
                }, status=status.HTTP_201_CREATED)
        else:
            return Response(data={
                'MENSAJE': 'Asignación no creada',
                'Errores': serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)
        
    def get(self, request):
        asignaciones = asignacion.objects.all()
        serializer = AsignacionSerializer(asignaciones, many=True)
        return Response(serializer.data)
    
    def put(self, request, id):
        try:
            asignacionInstance = asignacion.objects.get(id=id)
            serializer = AsignacionSerializer(asignacionInstance, data=request.data)
            validacion = serializer.is_valid()
            if validacion:
                serializer.save()
                return Response(data={
                    'MENSAJE': 'Asignación actualizada correctamente',
                    'Asignación': serializer.data
                    }, status=status.HTTP_200_OK)
            else:
                return Response(data={
                    'MENSAJE': 'Asignación no actualizada',
                    'Errores': serializer.errors
                    }, status=status.HTTP_400_BAD_REQUEST)
        except asignacion.DoesNotExist:
            return Response(data={
                'MENSAJE': 'Asignación no encontrada'
                }, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id):
        try:
            asignacionInstance = asignacion.objects.get(id=id)
            asignacionInstance.delete()
            return Response(data={
                'MENSAJE': 'Asignación eliminada correctamente'
                }, status=status.HTTP_200_OK)
        except asignacion.DoesNotExist:
            return Response(data={
                'MENSAJE': 'Asignación no encontrada'
                }, status=status.HTTP_400_BAD_REQUEST)

class AsignacionAPIView(APIView):
    def get(self, request, id):
        try:
            asignacionInstance = asignacion.objects.get(id=id)
            serializer = AsignacionSerializer(asignacionInstance)
            return Response(serializer.data)
        except asignacion.DoesNotExist:
            return Response(data={
                'MENSAJE': 'Asignación no encontrada'
                }, status=status.HTTP_400_BAD_REQUEST)