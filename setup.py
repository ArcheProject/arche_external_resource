import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.rst')).read()

requires = [
    'Arche',
    'pyramid',
    'pyramid_deform',
    'betahaus.viewcomponent',
    'colander',
    'deform',
    'fanstatic',
    'lingua',
    'Babel',
    'requests',
    'beautifulsoup4',
    'lxml',
    ]

setup(name='arche_external_resource',
      version='0.1dev',
      description='Experimental package to include external resources',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Development Status :: 3 - Alpha",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='Arche development team and contributors',
      author_email='robin@betahaus.net',
      url='https://github.com/ArcheProject/arche_external_resource',
      keywords='web pylons pyramid education e-learning',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="arche_external_resource",
      entry_points="""\
      """,
      message_extractors = { '.': [
              ('**.py',   'lingua_python', None ),
              ('**.pt',   'lingua_xml', None ),
              ]},
      )
