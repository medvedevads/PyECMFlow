from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from apps.contact.models import Contact
from .forms import ContactForm
from django.core.paginator import Paginator

@login_required
def contact_list(request):
    contacts = Contact.objects.all().order_by('-created_at')
    paginator = Paginator(contacts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'apps/contact/contact_list.html', {'page_obj': page_obj})
def contact_create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            if form.cleaned_data['assign_to_me']:
                contact.user = request.user
            else:
                contact.user = None
            contact.save()
            return redirect('contact:contact_list')
    else:
        form = ContactForm()
    return render(request, 'apps/contact/contact_form.html', {'form': form})

def contact_detail(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, 'apps/contact/contact_detail.html', {'contact': contact})

def contact_update(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            contact = form.save(commit=False)
            if form.cleaned_data['assign_to_me']:
                contact.user = request.user
            else:
                contact.user = None
            contact.save()
            return redirect('contact:contact_list')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'apps/contact/contact_form.html', {'form': form})

def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('contact:contact_list')
    return render(request, 'apps/contact/contact_confirm_delete.html', {'contact': contact})