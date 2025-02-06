from setuptools import setup, find_packages

setup(
    name="apiMoneyFusion",  # Remplace par le nom de ton package
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    author="Assemien Dev",
    author_email="sidjaneassemien1@gmail.com",
    description="API pour gérer la transactions dans fusion Money pour python",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/AssemienDev/docs.moneyfusion.net.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
