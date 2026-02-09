from django.shortcuts import render, redirect
from candidates.forms import CandidateRegister
from django.contrib import messages
from candidates.models import Candidate

# Create your views here.

#form view to add candidates
def register (request):
    if request.method == 'POST':
        form = CandidateRegister(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('name')
            messages.success(request, 'Candidate {0} created'.format(name))
            return redirect('home')
    else:
        form = CandidateRegister()

    return render(request, 'candidates/register.html', {'form': form})


#displays a list of all candidates
def candidate_list(request):
    all_candidates = Candidate.objects.all()
    context={'all_candidates': all_candidates}
    return render(request, 'candidates/list.html', context)

