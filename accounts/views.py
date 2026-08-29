from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import LoginForm, RegistrationForm


def register(request):
    if request.user.is_authenticated:
        return redirect("espace_personnel:dashboard")

    if request.method == "POST":
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(
                request,
                user,
            )

            return redirect(
                "espace_personnel:dashboard"
            )
    else:
        form = RegistrationForm()

    return render(
        request,
        "accounts/register.html",
        {
            "form": form,
        },
    )


def login_view(request):
    if request.user.is_authenticated:
        return redirect("espace_personnel:dashboard")

    if request.method == "POST":
        form = LoginForm(
            request,
            data=request.POST,
        )

        if form.is_valid():
            user = form.get_user()

            login(
                request,
                user,
            )

            return redirect(
                "espace_personnel:dashboard"
            )
    else:
        form = LoginForm()

    return render(
        request,
        "accounts/login.html",
        {
            "form": form,
        },
    )


@login_required
def logout_view(request):
    logout(request)

    return redirect("public:home")