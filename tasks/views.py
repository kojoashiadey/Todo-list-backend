from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Users can only access their own tasks
        return Task.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        # Save new task with the logged-in user as owner
        serializer.save(owner=self.request.user)
