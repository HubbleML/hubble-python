
import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'hubble'))
from version import VERSION

long_description = '''
Hubble client captures events from your machine learning models.
Allowing you to track model performance in real-time.

Learn more at https://docs.gethubble.io
'''

install_requires = [
    "requests>=2.7,<3.0",
    "six>=1.5",
    "monotonic>=1.5",
    "backoff==1.6.0",
    "python-dateutil>2.1"
]

setup(
    name='hubble-client',
    version=VERSION,
    url='https://docs.gethubble.io',
    author='Hubble',
    author_email='support@gethubble.io',
    maintainer='Hubble',
    maintainer_email='support@gethubble.io',
    packages=['hubble'],
    license='MIT License',
    install_requires=install_requires,
    description='Track ML models in real-time.',
    long_description=long_description,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
