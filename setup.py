#!/usr/bin/env python


import os
from distutils.core import setup

packages, data_files = [], []
root_dir = os.path.dirname(__file__)


for dirpath, dirnames, filenames in os.walk('django_russian'):
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.'):
            del dirnames[i]
    if '__init__.py' in filenames:
        pkg = dirpath.replace(os.path.sep, '.')
        if os.path.altsep:
            pkg = pkg.replace(os.path.altsep, '.')
        packages.append(pkg)
    elif filenames:
        prefix = dirpath[10:]
        for f in filenames:
            data_files.append(os.path.join(prefix, f))

setup(
    name='django_russian',
    description='Some russian localization',
    author='Ivan Sagalaev',
    author_email=' maniac@softwaremaniacs.org',
    license = 'BSD Licence',
    version = '0.1',
    url='https://github.com/glader/django_russian',
    package_dir={'django_russian': 'django_russian'},
    packages=packages,
    package_data={'django_russian': data_files},
    install_requires=[]
)
