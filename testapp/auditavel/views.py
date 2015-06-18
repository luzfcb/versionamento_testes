from django.shortcuts import render

# Create your views here.
class AuditavelViewMixin(object,):
    def form_valid(self, form, ):
        if not form.instance.criado_por:
            form.instance.criado_por = self.request.user
        form.instance.modificado_por = self.request.user
        return super(AuditavelViewMixin, self).form_valid(form)
