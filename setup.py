# Use this command for deploy.
#   python3 setup.py sdist bdist_wheel
#   python3 -m twine upload --skip-existing dist/*

import io
from setuptools import find_packages, setup

setup(name='simple_utils',
      version='1.0.6',
      description='Python utils.',
      long_description="Please refer to the https://github.com/da-huin/simple_utils",
      long_description_content_type="text/markdown",
      url='https://github.com/da-huin/simple_utils',
      download_url= 'https://github.com/da-huin/simple_utils/archive/master.zip',
      author='JunYeong Park',
      author_email='dahuin000@gmail.com',
      license='MIT',
      packages=find_packages(),
      install_requires=[],
      classifiers=[
          'Programming Language :: Python :: 3',
    ]
)
