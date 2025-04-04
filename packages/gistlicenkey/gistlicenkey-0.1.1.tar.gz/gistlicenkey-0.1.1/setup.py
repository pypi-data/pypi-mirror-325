from setuptools import setup

setup(
    name="gistlicenkey",
    version="0.1.1",
    packages=["gistlicenkey"],
    install_requires=["requests"],
    author="Moh Iqbal Hidayat",
    author_email="iqbalmh18.dev@gmail.com",
    description="A Python wrapper for software License Key management",
    long_description="GistLicenKey is a Python wrapper for managing license key using GitHub Gists as storage, with machine ID-based verification and customizable expiration dates.",
    long_description_content_type="text/plain",
    url="https://pypi.org/project/gistlicenkey",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
)