import re
import random
import markdown2
from django.shortcuts import render, redirect

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def information(request, title):
    lists = util.get_entry(title)

    if lists is None:
        return render(request, "encyclopedia/information.html",{
            "entry": "Page not found",
            "title": title
        })
    else:
        return render(request, "encyclopedia/information.html",{
            "entry": markdown2.markdown(lists) ,
            "title": title
        })

def searchbar(request):
    if request.method == 'POST':
        query = request.POST
        query = query['q']
        lists = []
        datalist = util.list_entries()

        for data in datalist:
            if re.search(query.lower(), data.lower()):
                lists.append(data)
        
        if len(lists) == 0:
            return render(request, "encyclopedia/error.html",{
                "error": "No result"
            })
        else:

            return render(request, "encyclopedia/search.html",{
                "inform": lists
                })


def newpost(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        datalist = util.list_entries()
        if title in datalist:
            return render(request, "encyclopedia/newpost.html",{
                'taken': "yes"
            })
        else:
            util.save_entry(title, content)
            return redirect('info', title=title)
    
    return render(request, "encyclopedia/newpost.html",{
        "taken" : "no"
    })

def edit(request, title):
    if request.method == 'GET':
        datalist = util.get_entry(title)
        return render(request, "encyclopedia/editpage.html",{
            'title': title,
            'content': datalist
        })
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        datalist = util.list_entries()        
        util.save_entry(title, content)
        return redirect('info', title=title)

def getrandom(request):
    datalist = util.list_entries()        
    show = random.randint(0, len(datalist) - 1)
    title = datalist[show]

    return redirect("info", title= title)

