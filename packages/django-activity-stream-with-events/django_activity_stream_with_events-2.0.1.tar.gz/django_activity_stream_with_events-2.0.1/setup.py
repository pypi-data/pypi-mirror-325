try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
from actstream import __version__, __author__

setup(name='django-activity-stream-with-events',
      version=__version__,
      description='Generate generic activity streams from the actions on your '
      'site. Users can follow any actors\' activities for personalized streams.',
      long_description=open('README.rst').read(),
      author=__author__,
      license='BSD 3-Clause',
      author_email='ja.alvarezgom@gmail.com',
      url='https://github.com/jalvarezgom/django-activity-stream-with-events',
      install_requires=['Django>=3.2'],
      packages=['actstream',
                'actstream.migrations',
                'actstream.templatetags',
                'actstream.tests',
                ],
      package_data={'actstream': ['locale/*/LC_MESSAGES/*.po',
                                  'templates/actstream/*.html']},
      classifiers=['Development Status :: 5 - Production/Stable',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 3',
                   'Topic :: Utilities'],
      extras_require={
          'drf': ['django-rest-framework', 'rest-framework-generic-relations'],
      },
      )
