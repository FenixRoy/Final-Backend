from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from gestion.models import equipo, colaborador, asignacion, tecnico

class EquipoSerializer(ModelSerializer):
    class Meta:
        model = equipo
        fields = ('id', 'tipo', 'marca', 'modelo', 'numero_serie')

    def update(self, instance, validated_data):
        instance.tipo = validated_data.get('tipo', instance.tipo)
        instance.marca = validated_data.get('marca', instance.marca)
        instance.modelo = validated_data.get('modelo', instance.modelo)
        instance.numero_serie = validated_data.get('numero_serie', instance.numero_serie)
        instance.save()
        return instance

class ColaboradorSerializer(ModelSerializer):
    class Meta:
        model = colaborador
        fields = ('id', 'nombre', 'apellido', 'dni', 'email', 'departamento', 'puesto')
    def update(self, instance, validated_data):
        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.apellido = validated_data.get('apellido', instance.apellido)
        instance.dni = validated_data.get('dni', instance.dni)
        instance.email = validated_data.get('email', instance.email)
        instance.departamento = validated_data.get('departamento', instance.departamento)
        instance.puesto = validated_data.get('puesto', instance.puesto)
        instance.save()
        return instance

class TecnicoSerializer(ModelSerializer):
    class Meta:
        model = tecnico
        fields = '__all__'
    def update(self, instance, validated_data):
        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.apellido = validated_data.get('apellido', instance.apellido)
        instance.usuario = validated_data.get('usuario', instance.usuario)
        instance.password = validated_data.get('password', instance.password)
        instance.save()
        return instance

class AsignacionSerializer(ModelSerializer):
    equipo = PrimaryKeyRelatedField(queryset=equipo.objects.all())
    colaborador = PrimaryKeyRelatedField(queryset=colaborador.objects.all())
    tecnico = PrimaryKeyRelatedField(queryset=tecnico.objects.all())
    class Meta:
        model = asignacion
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.equipo = validated_data.get('equipo', instance.equipo)
        instance.colaborador = validated_data.get('colaborador', instance.colaborador)
        instance.tecnico = validated_data.get('tecnico', instance.tecnico)
        instance.fecha_asignacion = validated_data.get('fecha_asignacion', instance.fecha_asignacion)
        instance.estado = validated_data.get('estado', instance.estado)
        instance.save()
        return instance

class AsignacionGetSerializer(ModelSerializer):
    equipo = EquipoSerializer()
    colaborador = ColaboradorSerializer()
    tecnico = TecnicoSerializer()
    class Meta:
        model = asignacion
        fields = '__all__'
        