from setuptools import setup, find_packages


def _make_requirents(req_file: str):
    with open(req_file) as f:
        return f.read().splitlines()

setup(
    name="kosmoy-gateway-sdk",
    version="0.0.1-dev",
    packages=find_packages(),
    install_requires=_make_requirents("requirements.txt"),
    author="Olsi Hoxha",
    author_email="olsi.hoxha@kosmoy.com",
    description="A Gateway SDK for making API requests",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    # url="https://github.com/yourusername/gateway-sdk",
    extras_require={
        "langchain": _make_requirents("requirements-langchain.txt")
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
