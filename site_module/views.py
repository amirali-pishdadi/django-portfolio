from django.shortcuts import render

from account_module.models import User
from .models import FooterLinkBox, SiteSetting, FooterLink, HeaderPage


# Create your views here.

def site_footer(request):
    is_main_setting: SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
    footer_link_boxes = FooterLinkBox.objects.all()
    user: User = User.objects.filter(is_superuser=True).first()
    for item in footer_link_boxes:
        footer_link = item.footerlink_set
    context = {
        'is_main_setting': is_main_setting,
        'footer_link_box': footer_link_boxes,
        'user':user
    }
    return render(request, 'AmirWeb/site_footer.html', context)


def site_header(request):
    is_main_setting: SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
    header_page = HeaderPage.objects.all()
    context = {
        'is_main_setting': is_main_setting,
        'header_links': header_page
    }
    return render(request, 'AmirWeb/site_header.html', context)
