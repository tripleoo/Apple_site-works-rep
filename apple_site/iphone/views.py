from django.shortcuts import render, get_object_or_404, redirect
from django.core.files import File
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView

from .forms import ReviewForm
from .models import Iphone, VidTovara, Promo, Review  # Review


def base(request):
    return render(request, 'base.html')

def page_iphone(request):
    return render(request, 'page_iphone.html')

#/
def get_iphone_data(request, devise_slug):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            try:
                Review.objects.create(**form.cleaned_data)
                return redirect('glav')
            except:
                form.add_error(None, 'Ошибка добавления отзыва')
    else:
        form = ReviewForm()

    iphone = get_object_or_404(Iphone, slug=devise_slug)
    reviews = Review.objects.all()
    data = {
        "iphone": iphone,
        "form": form,
        "reviews": reviews,
        "descrip": iphone.descrip
    }
    return render(request, 'page_iphone.html', data)

class PageIphone(DetailView):
    model = Iphone
    template_name = 'page_iphone.html'
    slug_url_kwarg = 'devise_slug'
    context_object_name = 'iphone'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ReviewForm()
        return context
    def post(self, request, *args, **kwargs):
        form = ReviewForm(request.POST)
        if form.is_valid():
            try:
                form.instance.iphone = self.get_object()
                form.save()
                return redirect('glav')
            except:
                form.add_error(None, 'Ошибка добавления отзыва')

        context = self.get_context_data()
        context['form'] = form
        return self.render_to_response(context)

def buy(request, id):
    iphone = get_object_or_404(Iphone, pk=id)
    data = {
        "iphone": iphone,
    }
    return render(request, 'buy.html', data)

class Buy(TemplateView):
    template_name = 'buy.html'
    def get_context_data(self, **kwargs):
        id = self.kwargs['id']
        iphone = get_object_or_404(Iphone, pk=id)
        context = super().get_context_data(**kwargs)
        context['iphone'] = iphone
        return context
def test(request):
    vids = VidTovara.objects.all()
    data = {
        "vdis": vids,
    }
    return render(request, 'test.html', context=data)


def glav(request):
    iphones = Iphone.objects.all()
    promo = Promo.objects.all()
    vids = VidTovara.objects.all()
    data = {
        'iphones': iphones,
        'promo': promo,
        'vids': vids,

    }
    return render(request, 'glav.html', data)

class Glav(ListView):
    model = Iphone
    template_name = 'glav.html'
    promo = Promo.objects.all()
    vids = VidTovara.objects.all()
    context_object_name = 'iphones'
    extra_context = {
        'promo': promo,
        'vids': vids,
    }



# def review(request, iphone_id):
#     iphone = get_object_or_404(Iphone, id=iphone_id)
#     if request.method == 'POST':
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             review = form.save(commit=False)
#             review.iphone = iphone
#             review.save()
#             return redirect('glav')
#         else:
#             form.add_error(None, 'Ошибка добавления отзыва')
#     else:
#         form = ReviewForm()


class AddReview(View):
    def get(self, request):
        form = ReviewForm()
        data = {
            'form': form
        }
        return render(request, 'review.html', context=data)
    def post(self, request, iphone_id):
        iphone = get_object_or_404(Iphone, id=iphone_id)
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.iphone = iphone
            review.save()
            return redirect('glav')

        else:
            form.add_error(None, 'Ошибка добавления отзыва')
        data = {
            'form': form
        }
        return render(request, 'review.html', context=data)


def filter_by_category(request, category_slug):
    iphones = Iphone.objects.filter(vid__slug=category_slug)
    promo = Promo.objects.all()
    vids = VidTovara.objects.all()
    data = {
        'iphones': iphones,
        'promo': promo,
        'vids': vids,
    }
    return render(request, 'glav.html', data)

class Filter_By_Category(ListView):
    template_name = 'glav.html'
    context_object_name = 'iphones'

    def get_queryset(self):
        category_slug = self.kwargs['category_slug']
        return Iphone.objects.filter(vid__slug=category_slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['promo'] = Promo.objects.all()
        context['vids'] = VidTovara.objects.all()
        return context