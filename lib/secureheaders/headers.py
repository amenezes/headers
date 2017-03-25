class Headers(object):
    def __init__(self):
        self.option = {}
        self.name = {}

class CSP(Header):


    def __init__(self):
        self.option = {
            'report-uri': '',
            'default-src': '',
            'script-nonce': '',
            'upgrade-insecure-requests': '',
            'media-src': '',
            'report-to': '',
            'reflected-xss': '',
            'style-src': '',
            'frame-src': '',
            'block-all-mixed-content': '',
            'child-src': '',
            'form-action': '',
            'base-uri': '',
            'img-src': '',
            'frame-ancestors': '',
            'manifest-src': '',
            'referrer': '',
            'sandbox': '',
            'plugin-types': '',
            'object-src': '',
            'connect-src': '',
            'font-src': '',
            'script-src': ''
        }
        self.name = 'content-security-policy'
