from setuptools import setup, find_packages

setup(
    name='my-flask-app-pratik-12345',
    version='0.3.0',
    packages=find_packages(),  # Automatically detects 'app' as the package
    install_requires=[
        'Flask',
    ],
    include_package_data=True,
)
