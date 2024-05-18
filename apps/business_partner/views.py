from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from apps.business_partner.models import BusinessPartner
from apps.contracts.models import Contracts
from .forms import BusinessPartnerForm
from django.core.paginator import Paginator


@login_required

def businesspartner_list(request):
    show_all = str(request.session.get('show_all', False)).lower()
    if 'show_all' in request.GET:
        show_all = str(request.GET.get('show_all', 'false')).lower() == 'true'
        request.session['show_all'] = show_all

    if show_all:
        businesspartners = BusinessPartner.objects.all().order_by('name')  # Order by name
    else:
        businesspartners = BusinessPartner.objects.filter(user=request.user).order_by('name')  # Order by name

    paginator = Paginator(businesspartners, 10)  # 10 контрагентов на странице
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'apps/business_partner/businesspartner_list.html',
                  {'page_obj': page_obj, 'show_all': show_all})

@login_required
def businesspartner_detail(request, pk):
    businesspartner = get_object_or_404(BusinessPartner, pk=pk)
    contracts = Contracts.objects.filter(business_partner=businesspartner)
    return render(request, 'apps/business_partner/businesspartner_detail.html',
                  {'businesspartner': businesspartner, 'contracts': contracts})


@login_required
def businesspartner_create(request):
    if request.method == 'POST':
        form = BusinessPartnerForm(request.POST)
        if form.is_valid():
            businesspartner = form.save(commit=False)
            businesspartner.user = request.user
            businesspartner.save()
            return redirect('business_partner:businesspartner_list')
    else:
        form = BusinessPartnerForm()
    return render(request, 'apps/business_partner/businesspartner_form.html',
                  {'form': form})

@login_required
def businesspartner_update(request, pk):
    businesspartner = get_object_or_404(BusinessPartner, pk=pk)
    if request.method == 'POST':
        form = BusinessPartnerForm(request.POST, instance=businesspartner)
        if form.is_valid():
            businesspartner = form.save()
            # Save the association with the contact
            contact = form.cleaned_data.get('contact')
            if contact:
                contact.business_partner = businesspartner
                contact.save()
            return redirect('business_partner:businesspartner_list')
    else:
        form = BusinessPartnerForm(instance=businesspartner)
    return render(request, 'apps/business_partner/businesspartner_form.html', 
                  {'form': form, 'businesspartner': businesspartner})
@login_required
def businesspartner_delete(request, pk):
    businesspartner = get_object_or_404(BusinessPartner, pk=pk)
    if request.method == 'POST':
        businesspartner.delete()
        return redirect('business_partner:businesspartner_list')
    return render(request, 'apps/business_partner/businesspartner_confirm_delete.html',
                  {'businesspartner': businesspartner})


