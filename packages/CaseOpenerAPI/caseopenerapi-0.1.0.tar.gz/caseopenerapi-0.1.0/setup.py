from setuptools import setup, find_packages


def readme():
  with open('README.md', 'r') as f:
    return f.read()


setup(
  name='CaseOpenerAPI',
  version='0.1.0',
  author='Markshubat',
  author_email='markshubat@gmail.com',
  description='Case Opener api tools',
  long_description=readme(),
  long_description_content_type='text/markdown',
  packages=find_packages(),
  install_requires=['requests>=2.25.1','tqdm'],
  classifiers=[
    'Programming Language :: Python :: 3.12',
    'Operating System :: OS Independent'
  ],
  keywords='skin generation caseopener',
  python_requires='>=3.6'
)