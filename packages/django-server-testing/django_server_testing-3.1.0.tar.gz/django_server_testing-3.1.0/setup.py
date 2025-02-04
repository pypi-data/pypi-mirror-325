from setuptools import setup, find_packages


def readme():
  with open('README.md', 'r') as f:
    return f.read()


setup(
  name='django_server_testing',
  version='3.1.0',
  author='SODT',
  author_email='svsharygin@icloud.com',
  description='',
  long_description=readme(),
  long_description_content_type='',
  url='https://github.com/lum0vi/django_server_testing',
  packages=find_packages(),
  install_requires=['requests>=2.25.1'],
  classifiers=[
    'Programming Language :: Python :: 3.11',
  ],
  keywords='files speedfiles',
  project_urls={
    'GitHub': 'https://github.com/lum0vi/django_server_testing'
  },
  python_requires='>=3.6'
)
