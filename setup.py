from setuptools import setup, find_packages

setup(
    name="api813bet",
    version="0.0.1",
    author="813bet API Team",
    description="Interface não oficial para a plataforma 813bet",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.1",
        "urllib3>=1.26.5"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
) 