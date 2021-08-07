from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


DEPENDENCIES = ['numpy', 'pandas', 'matplotlib==3.4.2', 'scipy', 'seaaborn']

setup(name='braingraphgeo',
      version='0.1',
      description='Python package for performing analysis on structural brain networks using random geometric surrogate graphs',
      long_description=readme(),
      author='Scott Trinkle',
      author_email='tscott.trinkle@gmail.com',
      license='MIT',
      install_requires=DEPENDENCIES,
      url='https://github.com/scott-trinkle/braingraphgeo',
      packages=['braingraphgeo'],
      package_dir={'mrpy': 'mrpy'},
      zip_safe=False)
