from django.apps import apps as django_apps
from django.core.exceptions import ObjectDoesNotExist
from edc_model_wrapper import ModelWrapper
from edc_consent.exceptions import ConsentError


class SubjectConsentModelWrapper(ModelWrapper):

    model = 'bcpp_clinic_subject.subjectconsent'
    next_url_name = django_apps.get_app_config(
        'bcpp_clinic_dashboard').dashboard_url_name
    next_url_attrs = ['subject_identifier', ]
    querystring_attrs = [
        'gender', 'screening_identifier', 'first_name', 'initials', 'modified']
    subject_eligibility_model = 'bcpp_clinic_subject.subjecteligibility'

    @property
    def map_area(self):
        model_cls = django_apps.get_model(self.subject_eligibility_model)
        try:
            subject_eligibility = model_cls.objects.get(
                screening_identifier=self.object.screening_identifier)
        except ObjectDoesNotExist:
            raise ConsentError(
                'Missing subject eligibility with identifier '
                f'{subject_eligibility.screening_identifier}.')
        return subject_eligibility.map_area
