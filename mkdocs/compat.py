# coding: utf-8
"""Python 2/3 compatibility module."""
import sys

PY2 = int(sys.version[0]) == 2

if PY2:
    from urlparse import urljoin, urlparse, urlunparse
    import urllib
    urlunquote = urllib.unquote
    from urllib2 import urlopen, URLError

    import SimpleHTTPServer as httpserver
    httpserver = httpserver
    import SocketServer
    socketserver = SocketServer
    from HTMLParser import HTMLParser

    import itertools
    zip = itertools.izip

    from StringIO import StringIO

    text_type = unicode
    binary_type = str
    string_types = (str, unicode)
    unicode = unicode
    basestring = basestring
else:  # PY3
    from urllib.parse import urljoin, urlparse, urlunparse, unquote
    from urllib.request import urlopen, URLError
    urlunquote = unquote

    import http.server as httpserver
    httpserver = httpserver
    import socketserver
    socketserver = socketserver
    from html.parser import HTMLParser

    zip = zip

    from io import StringIO

    text_type = str
    binary_type = bytes
    string_types = (str,)
    unicode = str
    basestring = (str, bytes)
