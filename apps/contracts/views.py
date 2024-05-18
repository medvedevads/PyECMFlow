from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Contracts
from .forms import ContractsForm
from django.core.paginator import Paginator


@login_required
def contracts_list(request):
    show_all = str(request.session.get('show_all', False)).lower()
    if 'show_all' in request.GET:
        show_all = str(request.GET.get('show_all', 'false')).lower() == 'true'
        request.session['show_all'] = show_all
    if show_all:
        contracts = Contracts.objects.all().order_by('name')
    else:
        contracts = Contracts.objects.filter(user=request.user).order_by('name')
    paginator = Paginator(contracts, 10)  # Показать 10 договоров на странице
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'apps/contracts/contracts_list.html',
                  {'page_obj': page_obj, 'show_all': show_all})

@login_required
def contracts_detail(request, pk):
    contracts = get_object_or_404(Contracts, pk=pk)
    return render(request, 'apps/contracts/contracts_detail.html',
                  {'contracts': contracts})

@login_required
def contracts_create(request):
    if request.method == 'POST':
        form = ContractsForm(request.POST, request.FILES)
        if form.is_valid():
            contracts = form
            contracts.contract_file = request.FILES['contract_file']
            contracts.save()
            return redirect('contracts:contracts_list')
    else:
        form = ContractsForm()
    return render(request, 'apps/contracts/contracts_form.html', {'form': form})

def contracts_update(request, pk):
    contracts = get_object_or_404(Contracts, pk=pk)
    if request.method == 'POST':
        form = ContractsForm(request.POST, request.FILES, instance=contracts)
        if form.is_valid():
            contracts = form.save(commit=False)  # Сохраняем форму, но не отправляем изменения в базу данных
            if 'contract_file' in request.FILES:  # Проверяем, существует ли файл contract_file
                contracts.contract_file = request.FILES['contract_file']
            contracts.save()  # Сохраняем изменения в базе данных
            return redirect('contracts:contracts_list')
    else:
        form = ContractsForm(instance=contracts)
    return render(request, 'apps/contracts/contracts_form.html',
                  {'form': form, 'contracts': contracts})
@login_required
def contracts_delete(request, pk):
    contracts = get_object_or_404(Contracts, pk=pk)
    if request.method == 'POST':
        contracts.delete()
        return redirect('contracts:contracts_list')
    return render(request, 'apps/contracts/contracts_confirm_delete.html',
                  {'contracts': contracts})


