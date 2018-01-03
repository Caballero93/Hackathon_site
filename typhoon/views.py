from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import sys
import os
import subprocess
import shutil
import json
import importlib.util
from .models import HallOfFame


def my_homepage_view(request):
    return render(request, "my_homepage_view.html")


def submit_sol(request):
    error = False
    if 'repo_link' in request.GET:
        r = request.GET['repo_link']
        if not r:
            error = True
        else:
            root_dir = os.getcwd()
            os.chdir("./hackathon")
            cwd = str(os.getcwd())
            # return HttpResponse(cwd)
            # if __name__ == '__main__':
            theirs = 'hackathon2017.their'
            # os.mkdir(theirs)
            # return HttpResponse(cwd)
            subprocess.run(['git', 'clone', r, theirs])

            # #Remove ours requirements file
            # os.remove('requirements.txt')
            # Get theirs
            shutil.copyfile(os.path.join(theirs, 'requirements.txt'),
                            'requirements.txt')

            # Remove our hackathon/solution
            shutil.rmtree(os.path.join('hackathon', 'solution'))
            # Get their hackathon/solution
            shutil.copytree(os.path.join(theirs, 'hackathon', 'solution'),
                            os.path.join('hackathon', 'solution'))

            # Remove their repository completely
            if sys.platform.startswith('win'):
                os.system('rmdir /S /Q "{}"'.format(theirs))
            else:
                shutil.rmtree(theirs)

            subprocess.run(['pip', 'install', '-r', 'requirements.txt'])
            subprocess.run(['python', 'run.py'])
            with open('./data/results.json', 'r') as f:
                res = json.load(f)
            Overall = res[7199]['overall']
            os.system('git reset --hard')
            os.system('git clean -f')
            os.chdir(root_dir)
            return HttpResponseRedirect(reverse('typhoon:result'), args=(Overall,))
    return render(request, 'submit_sol.html', {"error": error})


def visualize(request):
    return render(request, "viz.html")


def results(request):
    if request.is_ajax:
        return HttpResponse("YES!")
    else:
        return HttpResponse("NO!")


def hallOfFame(request):
    entries = HallOfFame.objects.all()
    context = {"entries": entries}
    return render(request, "halloffame.html", context)

def result(request, Overall):
    error = False
    if 'name' in request.POST:
        name = request.POST['name']
        if not name:
            error = True
        else:
            entry = HallOfFame(name=name, score=Overall)
            entry.save()
            return HttpResponseRedirect(reverse('typhoon:halloffame'))
    return render(request, 'result.html', {"overall":Overall,"error":error})
