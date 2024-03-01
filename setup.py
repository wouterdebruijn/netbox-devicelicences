from setuptools import find_packages, setup

setup(
    name='device-licenses',
    author='Wouter de Bruijn',
    author_email='wouter@netco.nl',
    version='0.1.4',
    description='Manage devices licenses and (support) contracts in Netbox',
    install_requires=[],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
