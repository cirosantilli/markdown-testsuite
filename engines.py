"""
All nested classes of this class represent markdown engines and implement the static methods:

- present
- get_output
"""

class gfm(object):
    """
    You **must** be authenticated to use this because this test suite has more than 50 tests.
    <http://developer.github.com/v3/#rate-limiting>
    - authenticated: 60 requests per hour
    - unauthenticated requests: 5000 requests per hour
    """

    url = 'https://api.github.com/markdown?access_token=' + config['gfm_oauth_token']

    @classmethod
    def available(cls):
        if not config['gfm_oauth_token']:
            return False
        data = '{"text":"a","mode":"gfm","context":"github/gollum"}'
        req = urllib2.Request(cls.url, data)
        try:
            response = urllib2.urlopen(req, timeout = config['timeout'])
        except urllib2.URLError, e:
            return False
        return True

    @classmethod
    def get_output(cls, input):
        data = '{{"text":{},"mode":"gfm","context":"github/gollum"}}'.format(json.dumps(input))
        req = urllib2.Request(cls.url, data)
        try:
            response = urllib2.urlopen(req, timeout = config['timeout'])
        except urllib2.URLError, e:
            return 'CONNEXION ERROR: ' + str(e)
        return response.read().decode(md_testsuite.encoding)

class CommandEngine(object):
    """
    Base class for engines which use a command in PATH.
    """
    @classmethod
    def available(cls):
        return command_present(cls.__name__)
    @classmethod
    def get_output(cls, input):
        return stdin_stdout_get_output([cls.__name__], input)

class kramdown(CommandEngine): pass
class multimarkdown(CommandEngine): pass
class pandoc(CommandEngine): pass
class redcarpet(CommandEngine): pass
