from django.shortcuts import render, redirect

from .forms import ResAiForm
# from .utils import get_classes


def index(request):

    if request.method == "POST":
        form = ResAiForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('ocres:ocres')  

    else:
        form = ResAiForm()

    # classes = get_classes()

    context = {
        'title': 'OCR PAGE',
        # 'classes': classes,
        'form': form,
    }

    return render(request, 'ocres/ocres.html', context)