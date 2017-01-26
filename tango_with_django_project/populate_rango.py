import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')
import django
django.setup()
from rango.models import Category, Page

def populate():

    python_pages = [
        {"title": "Official Python Tutorial",
         "url": "http://docs.python.org/2/tutorial/",
         "views": 43},
        {"title": "How to Think like a Computer Scientist",
         "url": "http://www.greenteapress.com/thinkpython/",
         "views": 31},
        {"title": "Learn Python in 10 Minutes",
         "url": "http://www.korokithakis.net/tutorials/python/",
         "views": 123}]

    django_pages = [
        {"title": "Official Django Tutorial",
         "url": "https://docs.djangoproject.com/en/1.9/intro/tutorial01/",
         "views": 312},
        {"title": "Django Rocks",
         "url": "http://www.djangorocks.com/",
         "views": 8},
        {"title": "How to Tango with Django",
         "url": "http://www.tangowithdjango.com/",
         "views": 98}]

    other_pages = [
        {"title": "Bottle",
         "url": "http://bottlepy.org/docs/dev/",
         "views": 3},
        {"title": "Flask",
         "url": "http://flask.pocoo.org",
         "views": 0}]

    cats = {"Python": {"pages": python_pages},
            "Django": {"pages": django_pages},
            "Other Frameworks": {"pages": other_pages}}

    cat_data = cats.get("Python")
    c = add_cat("Python",128,64)
    for p in cat_data["pages"]:
        add_page(c, p["title"], p["url"], p["views"])

    cat_data = cats.get("Django")
    c = add_cat("Django", 64, 32)
    for p in cat_data["pages"]:
        add_page(c, p["title"], p["url"], p["views"])

    cat_data = cats.get("Other Frameworks")
    c = add_cat("Other Frameworks", 32, 16)
    for p in cat_data["pages"]:
        add_page(c, p["title"], p["url"], p["views"])


    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(p)))

def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views
    p.save()
    return p

def add_cat(name, views, likes):
    c = Category.objects.get_or_create(name=name)[0]
    c.views=views
    c.likes=likes
    c.save()
    return c

if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()