from unittest import TestCase


from sites.models import Site


class TestSiteGetAll(TestCase):
    """Site.get_all"""

    def setUp(self):
        Site.delete_all()
        site1 = Site.create(name='My Site 1')
        site2 = Site.create(name='My Site 2')
        self.expected_sites = [site1, site2]

    def test_returns_all_created_records(self):
        self.assertEqual(Site.get_all(), self.expected_sites)


class TestSiteDeleteAll(TestCase):
    """Site.delete_all"""

    def test_removes_all_created_records(self):
        Site.create(name='foo')
        Site.delete_all()
        self.assertFalse(Site.get_all())


class TestSiteCreate(TestCase):
    """Site.create"""

    def test_instantiates_site_with_given_name(self):
        site = Site.create(name='Cool Name')
        self.assertEqual(site.name, 'Cool Name')
