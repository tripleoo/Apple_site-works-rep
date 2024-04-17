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



class Glav(ListView):
    paginate_by = 4
    model = Iphone
    template_name = 'glav.html'
    promo = Promo.objects.all()
    vids = VidTovara.objects.all()
    context_object_name = 'iphones'
    extra_context = {
        'promo': promo,
        'vids': vids,
    }


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

class Filter_By_Category(ListView):
    template_name = 'glav.html'
    context_object_name = 'iphones'
    paginate_by = 4

    def get_queryset(self):
        category_slug = self.kwargs['category_slug']
        return Iphone.objects.filter(vid__slug=category_slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['promo'] = Promo.objects.all()
        context['vids'] = VidTovara.objects.all()
        return context