from setuptools import setup, find_packages
import os


setup(
    name='plonetheme.unilluminated',
    version='0.1.6',
    description='Unilluminated, is an installable Diazo theme for Plone 4',
    long_description=open("README.rst", "rb").read() +
        open(os.path.join("docs", "HISTORY.txt"), "rb").read(),
    author='Alex Clark',
    author_email='aclark@aclark.net',
    maintainer='Leonardo Caballero',
    maintainer_email='leonardocaballero@gmail.com',
    url='https://github.com/aclark4life/plonetheme.unilluminated',
    # Get more strings from
    # https://pypi.org/pypi?:action=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Plone',
        'Framework :: Plone :: 4.1',
        'Framework :: Plone :: 4.2',
        'Framework :: Plone :: 4.3',
        'Framework :: Plone :: Theme',
        'Framework :: Zope2',
        'Framework :: Zope3',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='web zope plone theme diazo unilluminated',
    packages=find_packages(),
    include_package_data=True,
    namespace_packages=[
        'plonetheme',
    ],
    install_requires=[
        'setuptools',
        'plone.app.theming',
    ],
    entry_points={
        'z3c.autoinclude.plugin': 'target = plone',
    },
)
