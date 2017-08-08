from django.apps import apps as django_apps
from edc_base.utils import get_utcnow
from edc_base.view_mixins import EdcBaseViewMixin
from edc_constants.constants import MALE
from edc_dashboard.view_mixins import AppConfigViewMixin
from edc_dashboard.views import ListboardView
from edc_map.site_mappers import site_mappers

from ..mixins import MapAreaQuerysetViewMixin


class BaseListboardView(AppConfigViewMixin, EdcBaseViewMixin, MapAreaQuerysetViewMixin, ListboardView):

    app_config_name = 'bcpp_clinic_subject'
    navbar_item_selected = 'bcpp_clinic_subject'
    subject_eligibility_model = 'bcpp_clinic_subject.subjecteligibility'

    @property
    def map_area_consent_lookup(self):
        """Returns a list of screening identifiers.
        """
        model_cls = django_apps.get_model(self.subject_eligibility_model)
        subject_eligibility = model_cls.objects.filter(
            map_area=site_mappers.current_map_area).values_list(
                'screening_identifier')
        return subject_eligibility

    def add_map_area_filter_options(self, options=None, **kwargs):
        """Updates the filter options to limit the subject returned
        to those in the current map_area.
        """
        if self.map_area_consent_lookup:
            options.update(
                {'screening_identifier__in': self.map_area_consent_lookup})
        return options

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            MALE=MALE,
            reference_datetime=get_utcnow())
        return context
