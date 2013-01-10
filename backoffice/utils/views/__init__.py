from django import http
from django.utils import simplejson as json
from django.shortcuts import get_object_or_404
from django.core.exceptions import ImproperlyConfigured
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django.views.generic.base import TemplateView, TemplateResponseMixin
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import (BaseCreateView, DeletionMixin,
                                       BaseUpdateView)


class JSONResponseMixin(object):
    """
    JSON serialize class.
    """
    def render_json_to_response(self, context):
        "Returns a JSON response containing 'context' as payload"
        return self.get_json_response(self.convert_context_to_json(context))

    def get_json_response(self, content, **httpresponse_kwargs):
        "Construct an `HttpResponse` object."
        return http.HttpResponse(content,
                                 content_type='application/json',
                                 **httpresponse_kwargs)

    def convert_context_to_json(self, context):
        "Convert the context dictionary into a JSON object"
        return json.dumps(context)


class AjaxCreateView(BaseCreateView, TemplateResponseMixin, JSONResponseMixin):
    form_class = None
    template_name = None
    result_template_name = None

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AjaxCreateView, self).dispatch(*args, **kwargs)

    def form_invalid(self, form):
        """
        Collect errors for serializing.
        """
        return self.render_json_to_response({'success': False,
                                             'errors': dict([(k, v[0]) for k, v in form.errors.items()])})

    def form_valid(self, form):
        if self.result_template_name:
            return self.render_result_to_response(self.get_context_data())
        else:
            return self.render_json_to_response({'success': True})

    def render_result_to_response(self, context, **response_kwargs):
        return self.response_class(
            request = self.request,
            template = self.get_result_template_name(),
            context = context,
            **response_kwargs
        )

    def get_result_template_name(self):
        if self.result_template_name:
            url = self.result_template_name
        else:
            raise ImproperlyConfigured(
                "No result template name given. Provide a result_template_name.")
        return url


class AjaxUpdateView(BaseUpdateView, TemplateResponseMixin, JSONResponseMixin):
    form_class = None
    template_name = None
    result_template_name = None

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AjaxUpdateView, self).dispatch(*args, **kwargs)

    def form_invalid(self, form):
        """
        Collect errors for serializing.
        """
        return self.render_json_to_response({'success': False,
                                             'errors': dict([(k, v[0]) for k, v in form.errors.items()])})

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return self.render_result_to_response(self.get_context_data())

    def render_result_to_response(self, context, **response_kwargs):
        return self.response_class(
            request = self.request,
            template = self.get_result_template_name(),
            context = context,
            **response_kwargs
        )

    def get_result_template_name(self):
        if self.result_template_name:
            template = self.result_template_name
        else:
            raise ImproperlyConfigured(
                "No result template name given. Provide a result_template_name.")
        return template


class ProtectedListView(ListView):
    partial_template_name = None

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProtectedListView, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        if self.request.user.pk == int(self.kwargs['pk']):
            return self.model.objects.filter(user=self.request.user)
        else:
            return self.model.objects.filter(user=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ProtectedListView, self).get_context_data(**kwargs)

        if self.request.user.pk == int(self.kwargs['pk']):
            context['owner'] = True
        else:
            context['owner'] = False
        context.update(self.kwargs)
        return context

    def render_to_response(self, context, **response_kwargs):
        if self.request.is_ajax():
            return self.response_class(
                request=self.request,
                template=self.get_partial_template_name(),
                context=context,
                **response_kwargs
            )
        else:
            return super(ProtectedListView, self).render_to_response(
                context, **response_kwargs)

    def get_partial_template_name(self):
        if self.partial_template_name:
            template = self.partial_template_name
        else:
            raise ImproperlyConfigured("No result template name given.",
                                       "Provide a partial_template_name.")
        return template


class ProtectedDelete(DeletionMixin, SingleObjectMixin, TemplateView):
    success_url = None
    template_name = 'access_denied.html'
    http_method_names = ['post', 'delete']

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProtectedDelete, self).dispatch(*args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.request.user == self.object.user:
            return super(ProtectedDelete, self).delete(request, *args, **kwargs)
        else:
            return self.render_to_response()
