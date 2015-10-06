from dashboard.models import Dashboard


def render_dashboard():
    return {'dashboard': Dashboard()}
