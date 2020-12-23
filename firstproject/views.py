from django.http import HttpResponse
from datetime import date
from django.shortcuts import render

'''def index(request):
    #return HttpResponse("<h2><center>Welcome to my site.....</center></h2>")
    return HttpResponse("<pre><a href='http://127.0.0.1:8000/home/'>Home</a>   "
                        " <a href='https://www.python.org/about/'>AboutPython</a>  "
                        "<a>AboutJava</a></pre>")
def home(request):
    now=date.today()
    return HttpResponse("<h2><center>This is a Home Page.....%s </center></h2>"%now)'''

def index(request):
    params={'name':'janki','city':'Anand','age':24}
    return render(request,'index.html',params)

