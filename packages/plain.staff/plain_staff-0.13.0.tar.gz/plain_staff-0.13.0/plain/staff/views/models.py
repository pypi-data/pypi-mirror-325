from typing import TYPE_CHECKING

from plain import models
from plain.models import Q
from plain.urls import reverse_lazy

from .base import (
    URL_NAMESPACE,
    StaffCreateView,
    StaffDeleteView,
    StaffDetailView,
    StaffListView,
    StaffUpdateView,
)

if TYPE_CHECKING:
    from plain import models
    from plain.views import View


def get_model_field(instance, field):
    if "__" in field:
        # Allow __ syntax like querysets use,
        # also automatically calling callables (like __date)
        result = instance
        for part in field.split("__"):
            result = getattr(result, part)

            # If we hit a None, just return it
            if not result:
                return result

            if callable(result):
                result = result()

        return result

    return getattr(instance, field)


class StaffModelListView(StaffListView):
    show_search = True
    allow_global_search = True

    model: "models.Model"

    fields: list = ["pk"]
    queryset_order = []
    search_fields: list = ["pk"]

    def get_title(self) -> str:
        if title := super().get_title():
            return title

        return self.model._meta.model_name.capitalize() + "s"

    @classmethod
    def get_nav_title(cls) -> str:
        if cls.nav_title:
            return cls.nav_title

        if cls.title:
            return cls.title

        return cls.model._meta.model_name.capitalize() + "s"

    @classmethod
    def get_slug(cls) -> str:
        return cls.model._meta.model_name

    def get_template_context(self):
        context = super().get_template_context()

        order_by = self.request.GET.get("order_by", "")
        if order_by.startswith("-"):
            order_by_field = order_by[1:]
            order_by_direction = "-"
        else:
            order_by_field = order_by
            order_by_direction = ""

        context["order_by_field"] = order_by_field
        context["order_by_direction"] = order_by_direction

        return context

    def get_objects(self):
        queryset = self.get_initial_queryset()
        queryset = self.order_queryset(queryset)
        queryset = self.search_queryset(queryset)
        return queryset

    def get_initial_queryset(self):
        # Separate override for the initial queryset
        # so that annotations can be added BEFORE order_by, etc.
        return self.model.objects.all()

    def order_queryset(self, queryset):
        if order_by := self.request.GET.get("order_by"):
            queryset = queryset.order_by(order_by)
        elif self.queryset_order:
            queryset = queryset.order_by(*self.queryset_order)

        return queryset

    def search_queryset(self, queryset):
        if search := self.request.GET.get("search"):
            filters = Q()
            for field in self.search_fields:
                filters |= Q(**{f"{field}__icontains": search})

            queryset = queryset.filter(filters)

        return queryset

    def get_field_value(self, obj, field: str):
        try:
            return super().get_field_value(obj, field)
        except AttributeError:
            return get_model_field(obj, field)

    def get_field_value_template(self, obj, field: str, value):
        templates = super().get_field_value_template(obj, field, value)
        if hasattr(obj, f"get_{field}_display"):
            # Insert before the last default template,
            # so it can still be overriden by the user
            templates.insert(-1, "staff/values/get_display.html")
        return templates


class StaffModelDetailView(StaffDetailView):
    model: "models.Model"
    fields: list = []

    def get_title(self) -> str:
        return str(self.object)

    @classmethod
    def get_slug(cls) -> str:
        return f"{cls.model._meta.model_name}_detail"

    @classmethod
    def get_path(cls) -> str:
        return f"{cls.model._meta.model_name}/<int:pk>/"

    def get_template_context(self):
        context = super().get_template_context()
        context["fields"] = self.fields or ["pk"] + [
            f.name for f in self.object._meta.get_fields() if not f.remote_field
        ]
        return context

    def get_field_value(self, obj, field: str):
        try:
            return super().get_field_value(obj, field)
        except AttributeError:
            return get_model_field(obj, field)

    def get_object(self):
        return self.model.objects.get(pk=self.url_kwargs["pk"])

    def get_template_names(self) -> list[str]:
        template_names = super().get_template_names()

        if not self.template_name and isinstance(self.object, models.Model):
            object_meta = self.object._meta
            template_names = [
                f"staff/{object_meta.package_label}/{object_meta.model_name}{self.template_name_suffix}.html"
            ] + template_names

        return template_names


class StaffModelCreateView(StaffCreateView):
    model: "models.Model"
    form_class = None  # TODO type annotation

    def get_title(self) -> str:
        if title := super().get_title():
            return title

        return f"New {self.model._meta.model_name}"

    @classmethod
    def get_slug(cls) -> str:
        return f"{cls.model._meta.model_name}_create"

    @classmethod
    def get_path(cls) -> str:
        return f"{cls.model._meta.model_name}/create/"

    def get_template_names(self):
        template_names = super().get_template_names()

        if not self.template_name and issubclass(self.model, models.Model):
            model_meta = self.model._meta
            template_names = [
                f"staff/{model_meta.package_label}/{model_meta.model_name}{self.template_name_suffix}.html"
            ] + template_names

        return template_names


class StaffModelUpdateView(StaffUpdateView):
    model: "models.Model"
    form_class = None  # TODO type annotation
    success_url = "."  # Redirect back to the same update page by default

    def get_title(self) -> str:
        if title := super().get_title():
            return title

        return f"Update {self.object}"

    @classmethod
    def get_slug(cls) -> str:
        return f"{cls.model._meta.model_name}_update"

    @classmethod
    def get_path(cls) -> str:
        return f"{cls.model._meta.model_name}/<int:pk>/update/"

    def get_object(self):
        return self.model.objects.get(pk=self.url_kwargs["pk"])

    def get_template_names(self):
        template_names = super().get_template_names()

        if not self.template_name and isinstance(self.object, models.Model):
            object_meta = self.object._meta
            template_names = [
                f"staff/{object_meta.package_label}/{object_meta.model_name}{self.template_name_suffix}.html"
            ] + template_names

        return template_names


class StaffModelDeleteView(StaffDeleteView):
    model: "models.Model"

    def get_title(self) -> str:
        return f"Delete {self.object}"

    @classmethod
    def get_slug(cls) -> str:
        return f"{cls.model._meta.model_name}_delete"

    @classmethod
    def get_path(cls) -> str:
        return f"{cls.model._meta.model_name}/<int:pk>/delete/"

    def get_object(self):
        return self.model.objects.get(pk=self.url_kwargs["pk"])


class StaffModelViewset:
    @classmethod
    def get_views(cls) -> list["View"]:
        views = []

        if hasattr(cls, "ListView"):

            def get_list_url(self):
                return reverse_lazy(f"{URL_NAMESPACE}:{cls.ListView.view_name()}")

            for v in ["CreateView", "DetailView", "UpdateView", "DeleteView"]:
                if other_class := getattr(cls, v, None):
                    other_class.get_list_url = get_list_url
                    other_class.parent_view_class = cls.ListView

        if hasattr(cls, "CreateView"):

            def get_create_url(self):
                return reverse_lazy(f"{URL_NAMESPACE}:{cls.CreateView.view_name()}")

            if hasattr(cls, "ListView"):
                cls.ListView.get_create_url = get_create_url

        if hasattr(cls, "DetailView"):

            def get_detail_url(self, obj):
                return reverse_lazy(
                    f"{URL_NAMESPACE}:{cls.DetailView.view_name()}",
                    kwargs={"pk": obj.pk},
                )

            for v in ["ListView", "UpdateView", "DeleteView"]:
                if other_class := getattr(cls, v, None):
                    other_class.get_detail_url = get_detail_url

        if hasattr(cls, "UpdateView"):

            def get_update_url(self, obj):
                return reverse_lazy(
                    f"{URL_NAMESPACE}:{cls.UpdateView.view_name()}",
                    kwargs={"pk": obj.pk},
                )

            for v in ["ListView", "DetailView", "DeleteView"]:
                if other_class := getattr(cls, v, None):
                    other_class.get_update_url = get_update_url

        if hasattr(cls, "DeleteView"):

            def get_delete_url(self, obj):
                return reverse_lazy(
                    f"{URL_NAMESPACE}:{cls.DeleteView.view_name()}",
                    kwargs={"pk": obj.pk},
                )

            for v in ["ListView", "DetailView", "UpdateView"]:
                if other_class := getattr(cls, v, None):
                    other_class.get_delete_url = get_delete_url

        if hasattr(cls, "ListView"):
            views.append(cls.ListView)

        if hasattr(cls, "CreateView"):
            views.append(cls.CreateView)

        if hasattr(cls, "DetailView"):
            views.append(cls.DetailView)

        if hasattr(cls, "UpdateView"):
            views.append(cls.UpdateView)

        if hasattr(cls, "DeleteView"):
            views.append(cls.DeleteView)

        return views
