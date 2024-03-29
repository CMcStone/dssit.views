from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='dssit.views',
      version=version,
      description="DSSIT Custom Plone Views",
      long_description=open("README.txt").read() + "\n" +
                       open("CHANGES.txt").read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author="Carol McMasters-Stone",
      author_email="cbeck@ucdavis.edu",
      url='http://it.dss.ucdavis.edu',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Plone>=4.0',
      ],
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
