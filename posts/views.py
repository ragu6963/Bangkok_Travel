from django.shortcuts import redirect, render, get_object_or_404
from django.conf import settings
from .models import Post
from .forms import PostForm, CommentForm
from django.views.decorators.http import require_http_methods, require_safe
from django.contrib.auth.decorators import login_required
import requests
from django.http import HttpResponse, JsonResponse
import json


@require_safe
def home(request):
    posts = Post.objects.all().order_by("-created_at")
    context = {
        "posts": posts,
    }
    return render(request, "posts/home.html", context)


@require_safe
def index(request):

    return render(request, "posts/index.html")


@login_required(login_url="accounts:login", redirect_field_name="")
@require_http_methods(["GET", "POST"])
def create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            # Post 인스턴스 변수 생성
            post = Post()

            # 인스턴스 변수 값 할당
            post = set_post_data(post, form, request)

            # Post 인스턴스 저장
            post.save()

            # Post static_image 파일 저장 및 경로 할당
            post = get_street_view_static(post)
            post.save()

            return redirect("posts:home")
    else:
        form = PostForm

    context = {
        "form": form,
    }
    return render(request, "posts/create.html", context)


@require_safe
def detail(request, post_pk):
    MAPS_API_KEY = settings.MAPS_API_KEY

    post = get_object_or_404(Post, pk=post_pk)

    comments = post.comment_set.all()
    commentform = CommentForm

    context = {
        "MAPS_API_KEY": MAPS_API_KEY,
        "post": post,
        "comments": comments,
        "commentform": commentform,
    }
    return render(request, "posts/detail.html", context)


@login_required(login_url="accounts:login", redirect_field_name="")
@require_http_methods(["GET", "POST"])
def update(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if post.user != request.user:
        return redirect("posts:detail", post.id)
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            # 인스턴스 변수 값 할당
            post = set_post_data(post, form, request)

            # Post static_image 파일 저장 및 경로 할당
            post = get_street_view_static(post)

            # 수정사항 저장
            post.save()
            return redirect("posts:detail", post.id)

    else:
        form = PostForm(
            initial={
                "title": post.title,
                "content": post.content,
                "category": post.category,
                "url": post.url,
            }
        )

    context = {
        "form": form,
        "post": post,
    }
    return render(request, "posts/update.html", context)


@login_required(login_url="accounts:login", redirect_field_name="")
@require_http_methods(["POST"])
def delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if post.user != request.user:
        return redirect("posts:detail", post.id)

    if request.method == "POST":
        post.delete()
        return redirect("posts:home")

    return redirect("posts:detail", post.id)


@login_required(login_url="accounts:login", redirect_field_name="")
@require_http_methods(["POST"])
def comment_create(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    commentform = CommentForm(request.POST)
    if commentform.is_valid():
        comment = commentform.save(commit=False)
        comment.post = post
        comment.user = request.user
        comment.save()
        return redirect("posts:detail", post.pk)

    context = {
        "commentform": commentform,
    }
    return render(request, "posts/detail.html", context)


@require_safe
def like(request):
    if request.is_ajax():  # ajax 방식일 때 아래 코드 실행
        # 좋아요 버튼 누른 post 데이터 불러오기
        post_id = request.GET["post_id"]
        post = Post.objects.get(id=post_id)

        if request.user.is_authenticated:  # 버튼을 누른 유저가 비로그인 유저일 때
            user = request.user  # request.user : 현재 로그인한 유저

            if post.like.filter(id=user.id).exists():  # 이미 좋아요를 누른 유저일 때
                post.like.remove(user)  # like field에 현재 유저 추가
                post.like_count -= 1  # 좋아요 수 -1
                state = "좋아요 취소"

            else:  # 좋아요를 누르지 않은 유저일 때
                post.like.add(user)  # like field에 현재 유저 삭제
                post.like_count += 1  # 좋아요 수 + 1
                state = "좋아요"

            post.save()
            context = {
                "like_count": post.like_count,
                "state": state,
            }
            return HttpResponse(
                json.dumps(context), content_type="application/json"
            )


@require_safe
def like_list(request):
    if request.user.is_authenticated:
        posts = request.user.likes.all()
        context = {
            "posts": posts,
        }
        return render(request, "posts/home.html", context)

    else:
        return redirect("posts:home")


def set_post_data(post, form, request):
    url = form.cleaned_data["url"]
    lat, lng, heading, pitch = get_street_view_option(url)

    post.title = form.cleaned_data["title"]
    post.content = form.cleaned_data["content"]
    post.lat = lat
    post.lng = lng
    post.heading = heading
    post.pitch = pitch
    post.url = url
    post.user = request.user

    return post


def get_street_view_option(url):
    split_url = url.split(",")
    lat = float(split_url[0].split("@")[1])
    lng = float(split_url[1])
    heading = float(split_url[4].replace("h", ""))
    pitch = float(split_url[5].split("t")[0]) - float(90)

    return lat, lng, heading, pitch


def get_street_view_static(post):
    base_url = "https://maps.googleapis.com/maps/api/streetview?size=400x400"
    static_image_url = f"{base_url}&location={post.lat},{post.lng}&fov=80&pitch={post.pitch}&heading={post.heading}&key={settings.MAPS_API_KEY}"
    static_image = requests.get(static_image_url)
    with open(
        f"{settings.MEDIA_ROOT}/posts/thumnail/{post.id}.jpg", "wb"
    ) as file:
        file.write(static_image.content)
        post.static_image = f"{settings.MEDIA_URL}posts/thumnail/{post.id}.jpg"

    return post
