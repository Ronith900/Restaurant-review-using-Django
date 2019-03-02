from django.shortcuts import render,redirect
from .models import restaurant
from users.models import user
from django.views.generic import ListView
from django.views.generic import CreateView
from users.forms import commentform
from django.contrib.auth.decorators import login_required



def home(request):

    context = {
        'posts': restaurant.objects.all()
    }
    return render(request, 'restaurant/home.html', context)


class PostListView(ListView):
    model = restaurant
    template_name = 'restaurant/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'

   
class userCreateView(CreateView):
    model = user
    fields = ['comment']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def filterRest(request,category):

	if category == "" or category == "All":
		context = {'posts': restaurant.objects.all()}
		return render(request, 'restaurant/home.html', context)
	else:
		context = {'posts': restaurant.objects.filter(category = category)}
		return render(request, 'restaurant/home.html', context)


def about(request):
    return render(request, 'restaurant/about.html', {'title': 'About'})

@login_required
def restReviews(request,ID):
    if request.method == 'POST':
        form = commentform(request.POST)
        if form.is_valid():
         post = form.save(commit = False)
         post.rest = restaurant.objects.get(id = ID)
         post.author = request.user
         post.save()
           
         return redirect('rest_reviews',ID)
    else:
        form = commentform() 
        context = {
        'posts': restaurant.objects.get(id = ID),
        'cust': user.objects.filter(rest=ID),
        'form': form}
        return render(request,'restaurant/review.html',context)



