from unittest import TestCase


from dashboard.views import render_dashboard
from sites.models import Site


class TestUserViewsDashboard(TestCase):
    def test_renders_sites_on_dashboard(self):
        site1 = Site.create(name="Site 1")
        site2 = Site.create(name="Site 2")

        context = render_dashboard()
        sites = context['dashboard'].sites

        self.assertIn(site1, sites)
        self.assertIn(site2, sites)
