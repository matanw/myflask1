# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

test_deps = [
    'pylint',
    'pytest==3.2.3'
]
extras = {'test': test_deps}

setup(
    name='migration_agent',
    version='0.1.0',
    description='Package for OCI Migration-Agent',
    long_description=readme,
    author='OCI Israel',
    license=license,
    install_requires=[
        'Flask >=1.0.2, <1.1',
        'Flask-User',  # todo://version
        'flask-sqlalchemy-session',  # todo://version
        'oci >=1.4.1, <1.4.4',
        'retrying >=1.3.3, <1.4',
        'pyVmomi >= 6.0',
        'flask-restplus >=0.11.0, <0.12.0',
        'flask-security == 3.0.0'
    ],
    tests_require=test_deps,
    extras_require=extras,
    packages=find_packages(exclude=('tests', 'docs')),
    entry_points={'console_scripts': ['migration_agent=migration_agent.migration_agent:main']}
)
