from django.shortcuts import render, get_object_or_404, redirect


class ObjectDetailMixin:
    model = None
    template = None

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        return render(request, self.template, context=({self.model.__name__.lower(): obj}))


class ObjectCreateMixin:
    form = None
    template = None

    def get(self, request):
        obj = self.form()
        return render(request, self.template, context=({'form': obj}))

    def post(self, request):
        bound_form = self.form(request.POST)
        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        return render(request, self.template, context={'form': bound_form})