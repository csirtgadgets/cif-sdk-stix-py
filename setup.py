from setuptools import setup, find_packages

# this grabs the requirements from requirements.txt
req = [i.strip() for i in open("requirements.txt").readlines()]

import cif.sdk.stix

setup(
      name="cif-sdk-stix",
      version=cif.sdk.stix.__version__,
      description="CIF-STIX SDK",
      long_description="CIF-STIX SDK for Python",
      url="https://github.com/csirtgadgets/py-cif-sdk-stix",
      license='LICENSE',
      classifiers=[
                   "Topic :: System :: Networking",
                   "Environment :: Other Environment",
                   "Intended Audience :: Developers",
                   "License :: OSI Approved :: LGPL License",
                   "Programming Language :: Python",
                   ],
      keywords=['cif','security','stix'],
      author="Wes Young",
      author_email="wes@barely3am.com",
      packages=find_packages(),
      install_requires=req,
      test_suite = "test"
)
