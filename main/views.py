from django.shortcuts import render # berguna untuk mengimpor fungsi render dari modul django.shortcuts.

#  render akan digunakan untuk render tampilan HTML dengan menggunakan data yang diberikan.

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306152374',
        'name': 'Ahmad Dzulfikar As Shavyyyyyyyy',
        'class': 'PBP D',
        'comment' : 'amba'
    }

    return render(request, "main.html", context)
