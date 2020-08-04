from django.shortcuts import render
from django.http import HttpResponse
import markdown2 
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect 

from . import util

class SearchForm(forms.Form):
    result = forms.CharField(label="Search Encyclopedia")


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "form":SearchForm()
})

def data(request, name): 
    for list in util.list_entries():
        if list == name:
            return render(request, "encyclopedia/data.html",{    
            "data":markdown2.markdown(util.get_entry(name)),
            "name":name,
            "form":SearchForm()
            } )
            break
    else:
        return render (request,"encyclopedia/data.html",{
            "data":markdown2.markdown(util.get_entry("error"))
        })   

def search(request):
    if method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            result = form.cleaned_data["result"]
            for list in util.list_entries():
                if result == list:
                    return HttpResponseRedirect("wiki/html")