import sys
from wsgiref.util import application_uri


application = application_uri(sys.argv)