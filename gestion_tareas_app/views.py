from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from . import models, serializers
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    
class TaskViewSet(viewsets.ModelViewSet):
    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskSerializer
    
    @action(detail=False, methods=['post'])
    def complete_task(self, request, pk=None):
        serializer = serializers.CompleteTaskSerializer(data = request.data)
        
        if serializer.is_valid():
            
            id = serializer.validate_data['id']
            isDone = serializer.validate_data['is_done']
            
            try:
                task = models.Task.objects.get(id = id)
                
                task.is_done = isDone
                task.save()
                return Response({'message': 'Tarea completada'})
            except models.User.DoesNotExist:
                return Response({'message': 'Datos invalidos'}, status=status.HTTP_404_NOT_FOUND)
    