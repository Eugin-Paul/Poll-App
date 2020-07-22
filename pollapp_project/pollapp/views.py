from django.shortcuts import render,redirect
from .models import Poll
from .forms import PollForm
from django.http import HttpResponse

def home(request) :
    polls_available = Poll.objects.all()
    context = {
    'polls_available' : polls_available
    }
    return render(request,'pollapp/home.html',context)

def create(request) :
    if request.method == 'POST':
        form = PollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    form = PollForm()

    context = {
    'form' : form
    }

    return render(request,'pollapp/create.html',context)

def vote(request,poll_id) :
    vote = Poll.objects.get(pk = poll_id)
    if request.method == 'POST':
        option = request.POST['poll']
        if option == 'option1':
            vote.option_one_count += 1
        elif option == 'option2':
            vote.option_two_count += 1
        elif option == 'option3':
            vote.option_three_count += 1
        elif option == 'option4':
            vote.option_four_count += 1
        vote.save()
        return redirect('home')
    context = {
    'vote' : vote
    }
    return render(request,'pollapp/vote.html',context)

def results(request,poll_id) :
    result = Poll.objects.get(pk = poll_id)
    context = {
    'result' : result
    }
    return render(request,'pollapp/results.html',context)

def delete(request,poll_id) :
    delete = Poll.objects.filter(pk = poll_id).delete()
    context = {
    'delete' : delete
    }
    return redirect('home')
