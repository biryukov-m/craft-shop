from django.shortcuts import render


def main(request):
    template = 'custom_admin/main.html'
    return render(request, template)
