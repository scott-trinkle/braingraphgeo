from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(name='braingraphgeo',
      version='0.1',
      description='Python package for performing analysis on structural brain networks using random geometric surrogate graphs',
      long_description=readme(),
      author='Scott Trinkle',
      author_email='tscott.trinkle@gmail.com',
      license='MIT',
      packages=['braingraphgeo'],
      package_dir={'mrpy': 'mrpy'},
      zip_safe=False)