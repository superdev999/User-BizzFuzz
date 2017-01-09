from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

def home(request):
    html = """
    <h1>User BizzFuzz Test App</h1>
    <a href="/user_bizz/">Start</a><br>    
    """
    return HttpResponse(html)