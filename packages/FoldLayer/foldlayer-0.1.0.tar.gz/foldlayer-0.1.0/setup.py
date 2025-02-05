from setuptools import setup, find_packages

setup(
    name="FoldLayer",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "torch",
        ],
    author="Dallin Stewart, Sam Layton, Jeddy Bennett, Nathaniel Driggs",
    author_email="dallinpstewart@gmail.com",
    description="A package for fold layers in neural networks",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/binDebug3/FoldLayer",  # Your GitHub repo
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
