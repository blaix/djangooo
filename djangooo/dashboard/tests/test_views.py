from unittest import TestCase

from mock import patch

from dashboard.views import render_dashboard


class TestDashboardContext(TestCase):
    @patch('dashboard.views.Dashboard')
    def test_includes_dashboard_instance(self, Dashboard):
        context = render_dashboard()
        self.assertEqual(context['dashboard'], Dashboard.return_value)
