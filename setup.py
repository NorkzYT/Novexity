"""
Setup script for the Novexity package.

This script facilitates the installation and distribution of the Novexity package,
which is designed to scrape Google Search Results efficiently.
"""
from setuptools import setup, find_packages

setup(
    name='Novexity',
    version='0.3',
    packages=find_packages(),
    install_requires=[
        'beautifulsoup4',
        'requests',
        'python-dotenv',
        'requests_ip_rotator'
    ],
    author='Richard Lora',
    description='Scrape Google Search Results Fast and Easy.',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourgithubusername/google_search_pkg'
)
