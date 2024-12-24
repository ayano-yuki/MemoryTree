from django.shortcuts import render

# Create your views here.
# 以下を追記
def index(req):
    return render(req, 'index.html')