from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Todo
from usermanage.models import CustomUser
from .serializer import TodoSerializer

@api_view(['GET', 'POST'])
@permission_classes([permissions.IsAuthenticated])
def todo_list_create_view(request):
    if request.method == 'GET':
        user = CustomUser.objects.get(username = request.user)
        todos = Todo.objects.filter(user_id=user)
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # Create a new todo item
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)  # Associate the todo with the authenticated user
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([permissions.IsAuthenticated])
def todo_retrieve_update_destroy_view(request, pk):
    try:
        # Get the todo item that belongs to the authenticated user
        user = CustomUser.objects.get(username = request.user)
        todo = Todo.objects.get(pk=pk, user_id=user)
    except Todo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        # Return the todo item details
        serializer = TodoSerializer(todo)
        return Response(serializer.data)

    elif request.method == 'PUT':
        # Update the todo item
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        # Delete the todo item
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
