from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseBadRequest, HttpResponse
from django.forms import ModelForm

from user_bizz.models import Book

from random import randint

import csv

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'birthday', 'randNum', 'bizz']

def book_list(request, template_name='user_bizz/book_list.html'):
    book = Book.objects.all()    
    data = {}
    data['object_list'] = book
    return render(request, template_name, data)

def book_create(request, template_name='user_bizz/book_form.html'):
    form = BookForm(request.POST or None)
    bizz_num = randint(1,100)
    form.fields['randNum'].initial = bizz_num
    
    if bizz_num % 3 == 0 and bizz_num % 5 == 0:
        form.fields['bizz'].initial = 0
    elif bizz_num % 3 == 0:
        form.fields['bizz'].initial = 1
    elif bizz_num % 5 == 0:
        form.fields['bizz'].initial = 2
    else:
        form.fields['bizz'].initial = 3
    
    if form.is_valid():             
        form.save()
        return redirect('user_bizz:book_list')
    return render(request, template_name, {'form':form})

def book_update(request, pk, template_name='user_bizz/book_form.html'):
    book= get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('user_bizz:book_list')
    return render(request, template_name, {'form':form})

def book_delete(request, pk, template_name='user_bizz/book_confirm_delete.html'):
    book= get_object_or_404(Book, pk=pk)    
    if request.method=='POST':
        book.delete()
        return redirect('user_bizz:book_list')
    return render(request, template_name, {'object':book})
    
def export_users_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="users.csv"'

    writer = csv.writer(response)
    writer.writerow(['name', 'birthday', 'randNum'])

    users = Book.objects.all().values_list('name', 'birthday', 'randNum')
    for user in users:
        writer.writerow(user)

    return response