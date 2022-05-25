
def setup_settings(settings, is_prod, **kwargs):

    settings['MIDDLEWARE'] += ['cart.middleware.CartMiddleware']

    settings['JAVASCRIPT'] += ['cart.js']
