from django.apps import apps as django_apps
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView

from edc_base.view_mixins import EdcBaseViewMixin
from edc_dashboard.view_mixins import (
    DashboardViewMixin as EdcDashboardViewMixin, AppConfigViewMixin)

from ....model_wrappers import CrfModelWrapper, SubjectVisitModelWrapper
from ....model_wrappers import RequisitionModelWrapper, SubjectConsentModelWrapper
from .base_dashboard_view import BaseDashboardView


class DashboardView(
        BaseDashboardView, EdcDashboardViewMixin,
        AppConfigViewMixin, EdcBaseViewMixin, TemplateView):

    app_config_name = 'bcpp_clinic_dashboard'
    consent_model = 'bcpp_clininc_subject.subjectconsent'
    off_study_model = 'bcpp_clinic_subject.subjectoffstudy'
    consent_model_wrapper_cls = SubjectConsentModelWrapper
    crf_model_wrapper_cls = CrfModelWrapper
    requisition_model_wrapper_cls = RequisitionModelWrapper
    visit_model_wrapper_cls = SubjectVisitModelWrapper
    navbar_item_selected = 'consented_subject'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    @property
    def subject_off_study_model_cls(self):
        return django_apps.get_model(self.off_study_model)

    @property
    def subject_consent_model_cls(self):
        return django_apps.get_model(self.consent_model)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dashboard_url_name = django_apps.get_app_config(
            'bcpp_clinic_dashboard').dashboard_url_name
        try:
            subject_offstudy = self.subject_off_study_model_cls.objects.get(
                subject_identifier=self.subject_identifier)
        except ObjectDoesNotExist:
            subject_offstudy = None
        context.update(
            subject_offstudy=subject_offstudy,
            bcpp_clinic_subject_dashboard_url_name=dashboard_url_name)
        return context
