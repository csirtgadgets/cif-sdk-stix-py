from setuptools import setup

setup(name="cif-sdk-stix",
    version=cif.sdk.stix.__version__,
    description="CIF Python SDK - Stix",
    long_description="Stix Formatter",
    url="https://github.com/csirtgadgets/py-cif-sdk-stix",
    license='LGPL',
    classifiers=[
        "Topic :: System :: Networking",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: LGPL License",
        "Programming Language :: Python",
    ],
    keywords='CIF',
    author="Wes Young",
    author_email="wes@barely3am.com",
    packages = ["cif.sdk.format.stix","test"],
    install_requires = [
        "cif.sdk",
        'stix'
    ],
    test_suite = "test"
)
