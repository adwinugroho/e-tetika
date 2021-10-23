from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        "title": "e-Tetika | Wadah Etam Berekspresi",
        "email": "hello@etetika.com",
        "no_hp": "+62 821 2200 2993",
        "address": "Jln. Semeru gg. 2 No. 4 Samarinda, Indonesia"
    }

    return render(request, "frontpage/index.html", context)