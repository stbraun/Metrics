import sys
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


version = '0.1.0'


class PyTest(TestCommand):
    """This is a plug-in for setuptools.

     It will invoke py.test when you run python setup.py test
    """
    def finalize_options(self):
        """Configure."""
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        """Execute tests."""
        import pytest  # import here, because outside the required eggs aren't loaded yet
        sys.exit(pytest.main(self.test_args))


setup(
    name='metrics',
    version=version,
    description='Simple code metrics',
    long_description=open("README.rst").read(),
    package_dir={'': '.'},
    url='https://github.com/stbraun/Metrics',
    license='MIT',
    keywords='development tools',  # Separate with spaces
    author='Stefan Braun',
    author_email='sb@action.ms',
    packages=find_packages(exclude=['examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    cmdclass={'test': PyTest},
    scripts=['runHotspotAnalysis.py', ],

    # List of packages that this one depends upon:
    install_requires=['argh', 'setuptools'],
    requires=['argh', 'setuptools'],
    provides=['metrics']
)
