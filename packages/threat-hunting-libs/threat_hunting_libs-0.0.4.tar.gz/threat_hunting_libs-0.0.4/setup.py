import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="threat_hunting_libs",
    version="0.0.4",
    author="h4cklife",
    author_email="h4cklife_src@protonmail.com",
    description="Libraries and modules to assist in threat hunting and research.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/h4cklife/threat_hunting",
    packages=setuptools.find_packages(),
    install_requires=['certifi', 'pytz'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)