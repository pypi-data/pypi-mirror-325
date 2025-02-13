from setuptools import setup, find_packages

setup(
    name="wiki-api-client",
    version="1.0.2",
    packages=find_packages(),
    install_requires=[
        "requests",
        "aiohttp",
    ],
    author="b-3dev",
    author_email="b3dev.mmd@gmail.com",
    description="Request to wiki-api.ir APIs",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/b-3dev/python-wiki-client",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Development Status :: 5 - Production/Stable",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
    ],
    python_requires=">=3.6",
)
