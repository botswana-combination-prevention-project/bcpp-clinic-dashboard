from django.apps import AppConfig as DjangoApponfig


class AppConfig(DjangoApponfig):
    name = 'bcpp_clinic_dashboard'

    listboard_template_name = 'bcpp_clinic_dashboard/subject/listboard.html'
    dashboard_template_name = 'bcpp_clinic_dashboard/subject/dashboard.html'
    base_template_name = 'bcpp_clinic_dashboard/base.html'
    listboard_url_name = 'bcpp_clinic_dashboard:listboard_url'
    dashboard_url_name = 'bcpp_clinic_dashboard:dashboard_url'
    admin_site_name = 'bcpp_clinic_subject_admin'

    screening_listboard_template_name = 'bcpp_clinic_dashboard/screening/listboard.html'
    screening_listboard_url_name = 'bcpp_clinic_dashboard:screening_listboard_url'
