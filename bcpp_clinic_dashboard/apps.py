from django.apps import AppConfig as DjangoApponfig


class AppConfig(DjangoApponfig):
    name = 'bcpp_clinic_dashboard'
    listboard_template_name = 'bcpp_clinic_dashboard/listboard.html'
    dashboard_template_name = 'bcpp_clinic_dashboard/dashboard.html'
    base_template_name = 'bcpp_clinic/base.html'
    listboard_url_name = 'bcpp_clinic_dashboard:listboard_url'
    dashboard_url_name = 'bcpp_clinic_dashboard:dashboard_url'
    admin_site_name = 'bcpp_clinic_subject_admin'
