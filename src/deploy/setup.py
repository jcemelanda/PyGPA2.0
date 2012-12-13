from distutils.core import setup
from sys import version
from os import popen

YUM_STRING = 'yum install python-imaging python-matplotlib PyQt4 -y'
APT_PIP = 'apt-get install python-pip libpng* libfreetype* PyQt4* && pip install matplotlib'
PIP = 'pip install '
if 'Red Hat' in version:
    string = YUM_STRING
elif 'Debian' in version:
    string = APT_PIP

popen(string)
setup(name='PyGPA',
      version='2.0',
      url='http://programeempython.blog.br',
      description='Python Software to process Gradient Pattern Analysis',
      author='Julio Cesar Eiras',
      author_email='jcemelanda@gmail.com',
      packages=['PyGPA', 'PyGPA.control', 'PyGPA.utils','PyGPA.models','PyGPA.view', 'PyGPA.widgets'],
      requires=['pil', 'pyqt4', 'matplotlib', 'numpy'],) 

