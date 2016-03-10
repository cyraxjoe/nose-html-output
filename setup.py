import os
import setuptools

import htmloutput


REPODIR = os.path.dirname(os.path.realpath(__file__))

def _get_version(repodir):
    version = 'UNKNOWN'
    init = open(os.path.join(repodir, 'htmloutput', '__init__.py'))
    for line in init.readlines():
        if '__version__' in line and '=' in line:
            version = line.split('=')[-1].strip()
            version = version.replace('"', '').replace("'", '')
            break
    init.close()
    return version

def _get_longdesc(repodir):
    return open(os.path.join(repodir, 'README.rst')).read()


version = _get_version(REPODIR)
longdesc = _get_longdesc(REPODIR)
setuptools.setup(
    name="alt-nose-html-output",
    author='Joel Rivera',
    description="Nose plugin to produce test results in html.",
    version=version,
    long_description=longdesc,
    license="Apache License, Version 2.0",
    url="https://github.com/cyraxjoe/nose-html-output",
    packages=["htmloutput"],
    install_requires=['nose'],
    classifiers=[
        "Environment :: Console",
        "Topic :: Software Development :: Testing",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3"
    ],
    entry_points={
        'nose.plugins.0.10': [
            'html-output = htmloutput.htmloutput:HtmlOutput'
        ]
    }
)
