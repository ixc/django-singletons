from functools import update_wrapper

from django.contrib import admin
from django.utils.translation import ugettext as _
from django.utils.encoding import force_unicode
from django.http import HttpResponseRedirect

class SingletonModelAdmin(admin.ModelAdmin):

    change_form_template = "admin/singleton_models/change_form.html"
    
    def has_add_permission(self, request):
        """ Singleton pattern: prevent addition of new objects (but allow first one) """
        return self.model.objects.count() < 1
        
    def get_urls(self):
        try:
            from django.conf.urls import url  # >= 1.4
        except ImportError:
            from django.conf.urls.defaults import url

        def wrap(view):
            def wrapper(*args, **kwargs):
                return self.admin_site.admin_view(view)(*args, **kwargs)
            return update_wrapper(wrapper, view)

        try:
            info = self.model._meta.app_label, self.model._meta.model_name  # >= 1.6
        except AttributeError:
            info = self.model._meta.app_label, self.model._meta.module_name

        urlpatterns = super(SingletonModelAdmin, self).get_urls()
        urlpatterns = [
            url(r'^$',
                wrap(self.change_view),
                {'object_id': '1'},
                name='%s_%s_changelist' % info),
        ] + urlpatterns

        return urlpatterns
        
    def response_change(self, request, obj):
        """
        Determines the HttpResponse for the change_view stage.
        """
        opts = obj._meta

        msg = _('%(obj)s was changed successfully.') % {'obj': force_unicode(obj)}
        if request.POST.has_key("_continue"):
            self.message_user(request, msg + ' ' + _("You may edit it again below."))
            return HttpResponseRedirect(request.path)
        else:
            self.message_user(request, msg)
            return HttpResponseRedirect("../../")
            
    def change_view(self, request, object_id, extra_context=None):
        if object_id=='1':
            self.model.objects.get_or_create(pk=1)
        return super(SingletonModelAdmin, self).change_view(
            request,
            object_id,
            extra_context=extra_context,
        )

