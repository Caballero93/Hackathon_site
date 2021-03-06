from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import sys
import os
import subprocess
import shutil
import importlib.util


def my_homepage_view(request):
    return render(request, "my_homepage_view.html")

def submit_sol(request):
    error = False
    if 'repo_link' in request.GET:
        r = request.GET['repo_link']
        if not r:
            error = True
        else:
            os.chdir("./hackathon")
            cwd = str(os.getcwd())
            #if __name__ == '__main__':
            theirs = 'hackathon2017.their'
            # os.mkdir(theirs)
            # return HttpResponse(cwd)
            os.system('git reset --hard')
            subprocess.run(['git', 'clone', r, theirs])

            # #Remove ours requirements file
            #os.remove('requirements.txt')
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
            return HttpResponse(cwd)
            # return HttpResponseRedirect('/viz.html')
    return render(request, 'submit_sol.html', {"error": error})

def visualize(request):
    return render(request, "viz.html")

def results(request):
    if request.is_ajax:
        return HttpResponse("YES!")
    else:
        return HttpResponse("NO!")

