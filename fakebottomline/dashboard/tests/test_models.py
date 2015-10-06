from unittest import TestCase

from mock import Mock, patch

from dashboard.models import Dashboard


class TestDashboardSites(TestCase):
    """Dashboard.sites"""

    def setUp(self):
        self.dashboard = Dashboard()

    @patch('dashboard.models.Site')
    def test_return_last_edited_site(self, Site):
        expected_sites = [Mock(), Mock()]
        Site.get_all.return_value = expected_sites
        self.assertEqual(self.dashboard.sites, expected_sites)
