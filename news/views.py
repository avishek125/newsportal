from django.shortcuts import render
from news.models import News

# Create your views here.
def home_page(request):
    news = News.objects.all()
    context ={
        "news":news,
    }
    return render(request,'index.html', context)