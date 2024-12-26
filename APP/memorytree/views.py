from django.shortcuts import render, redirect
from .models import DiaryEntry
from .forms import DiaryEntryForm

def index(req):
    return render(req, 'index.html')

def write_diary(req):
    if req.method == 'POST':
        form = DiaryEntryForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('memorytree:diary_success')  # 日記が保存された後のリダイレクト先
    else:
        form = DiaryEntryForm()

    return render(req, 'write_diary.html', {'form': form})

def see_word_cloud(req):
    return render(req, 'see_word_cloud.html')



def diary_success(request):
    return render(request, 'diary_success.html')