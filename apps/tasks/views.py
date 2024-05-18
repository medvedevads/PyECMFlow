from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Task, Comment
from .forms import TaskForm, CommentForm
from django.urls import reverse
from django.http import HttpResponseRedirect

@login_required
def task_list(request):
    show_all = str(request.session.get('show_all', False)).lower()
    order_by = request.GET.get('order_by', 'due_date')

    if 'show_all' in request.GET:
        show_all = str(request.GET.get('show_all', 'false')).lower() == 'true'
        request.session['show_all'] = show_all

    if show_all:
        tasks = Task.objects.all().order_by(order_by)
    else:
        tasks = Task.objects.filter(assigned_to=request.user).order_by(order_by)

    paginator = Paginator(tasks, 5)  # Показать 5 заданий
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'apps/tasks/task_list.html',
                  {'page_obj': page_obj, 'show_all': show_all})

@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.assigned_to = request.user
            task.save()
            return redirect('tasks:task_list')
    else:
        form = TaskForm()
    return render(request, 'apps/tasks/task_form.html', {'form': form})

@login_required
def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    top_level_comments = task.comments.filter(parent__isnull=True).order_by('-created_at')
    form = CommentForm()
    return render(request, 'apps/tasks/task_detail.html',
                  {'task': task, 'comments': top_level_comments, 'form': form})

@login_required
def task_update(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.due_date = form.cleaned_data['due_date']
            task.save()
            show_all = str(request.session.get('show_all', False)).lower()
            return HttpResponseRedirect(reverse('tasks:task_list') + f'?show_all={show_all}')
    else:
        form = TaskForm(instance=task)
    return render(request, 'apps/tasks/task_form.html', {'form': form, 'task': task})

@login_required
def task_delete(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks:task_list')
    return render(request, 'apps/tasks/task_confirm_delete.html', {'task': task})

@login_required
def comment_create(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.task = task
            parent_id = request.POST.get('parent_id')
            if parent_id:
                comment.parent = Comment.objects.get(id=parent_id)
            comment.save()
            return redirect('tasks:task_detail', task_id=task.id)
    else:
        form = CommentForm()
    return render(request, 'apps/tasks/comment_form.html', {'form': form})

@login_required
def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user != comment.user:
        return redirect('tasks:task_detail', task_id=comment.task.id)

    if request.method == 'POST':
        comment.delete()
        return redirect('tasks:task_detail', task_id=comment.task.id)
    else:
        return render(request, 'apps/tasks/comment_confirm_delete.html',
                      {'comment': comment})

@login_required
def comment_edit(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user != comment.user:
        return redirect('tasks:task_detail', task_id=comment.task.id)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('tasks:task_detail', task_id=comment.task.id)
    else:
        form = CommentForm(instance=comment)

    return render(request, 'apps/tasks/comment_form.html',
                  {'form': form, 'comment': comment})
