from sites.models import Site


class Dashboard(object):

    @property
    def sites(self):
        return Site.get_all()
