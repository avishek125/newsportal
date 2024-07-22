from django.shortcuts import render
from news.models import News

"""
home page
"""
def home_page(request):
    editorial_news = News.objects.filter(is_editorial=True).order_by("-id")[:3]
    trending_news = News.objects.all().order_by("-views_count")[:4]
    popular_news = News.objects.all().order_by("-views_count")[:4]
    recent_news = News.objects.all().order_by("-created_date")[:3]
    context = {
        "editorial":editorial_news,
         "trending_news": trending_news,
         "popular_news":popular_news,
         "recent_news":recent_news,
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