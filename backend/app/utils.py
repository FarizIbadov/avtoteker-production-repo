from PIL import Image
from django.urls import resolve, reverse_lazy
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Column, Div, HTML, Field


def compress(path, dimentions=None, quality=None):
    kwargs = {
        'fp': path
    }
    img = Image.open(path)
    if dimentions and (img.height > dimentions[1] or img.width > dimentions[0]):
        img.thumbnail(dimentions)
    elif quality:
        kwargs['optimize'] = True
        kwargs['quality'] = quality

    img.save(**kwargs)


def get_url_name(request):
    return str(resolve(request.path_info).url_name.split("-")[0])


def get_submit_label(kwargs):
    if kwargs["instance"]:
        return "Update"
    return "Add"


def get_prev_url(**kwargs):
    instance, list_url = kwargs["instance"], kwargs["list_url"]
    if instance:
        return instance.get_absolute_url()
    return reverse_lazy(list_url)


def get_button_container(
    submit_label, prev_url, btn_container_class="specific-form__btn-group"
):
    return Div(
        HTML(f'<a href="{prev_url}" class="btn btn-danger d-inline-block ">Cancel</a>'),
        Submit("submit", submit_label, css_class="btn btn-secondary-1 d-inline-block"),
        css_class=btn_container_class,
    )
