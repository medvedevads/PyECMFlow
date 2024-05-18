from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.tasks.models import Task

@login_required
def dashboard(request):
    user_tasks = Task.objects.filter(assigned_to=request.user).order_by('due_date')[:5]
    return render(request, 'dashboard.html', {
        'user_tasks': user_tasks,
    })
