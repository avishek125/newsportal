from django.shortcuts import render
from news.models import News

"""
home page
"""
def home_page(request):
    context = {
        "news":"",
    }
    return render(request,'index.html', context)



"""
contact us page
"""
def contact_us(request):
    context = {
        "from": "", # 
    }
    return render(request, "contactus.html", context)