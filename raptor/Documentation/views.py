from django.shortcuts import render


def single_linux_view(request):
    context = {}
    return render(request, "Single_linux.html", context)
