from django.shortcuts import render

# Create your views here.
def projects_list(request):
    return render(request, 'content/projects-list.html')
