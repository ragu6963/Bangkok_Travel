from django.shortcuts import redirect, render, get_object_or_404
from django.conf import settings
from .models import Post
from .forms import PostForm


def home(request):
    return render(request, "posts/home.html")


def index(request):
    posts = Post.objects.all()

    context = {
        "posts": posts,
    }
    return render(request, "posts/index.html", context)


def create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            # url에서 위도 경도 추출
            url = form.cleaned_data["url"]
            split_url = url.split(",")
            lat = split_url[0].split("@")[1]
            lng = split_url[1]

            # Post 인스턴스 변수 생성
            post = Post()

            # 데이터 대입
            post.title = form.cleaned_data["title"]
            post.content = form.cleaned_data["content"]
            post.lat = lat
            post.lng = lng
            post.user = request.user
            # Post 인스턴스 저장
            post.save()
            return redirect("posts:index")
    else:
        form = PostForm

    context = {
        "form": form,
    }
    return render(request, "posts/create.html", context)


def detail(request, pk):
    MAPS_API_KEY = settings.MAPS_API_KEY

    post = get_object_or_404(Post, pk=pk)
    context = {
        "MAPS_API_KEY": MAPS_API_KEY,
        "post": post,
    }
    return render(request, "posts/detail.html", context)
