from django.views.generic.base import TemplateView


class RobotsView(TemplateView):
    """
    Serves /robots.txt without Apache configuration modification.
    """
    template_name = 'robots.txt'

    def render_to_response(self, context, **kwargs):
        return super(TemplateView, self).render_to_response(context,
            content_type='text/plain', **kwargs)
