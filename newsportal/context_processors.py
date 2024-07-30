from news.models import Category, Subscribe


"""
News category to show in navbar
"""
def category(request):
    category = Category.objects.all()
    return {
        "category": category
    }