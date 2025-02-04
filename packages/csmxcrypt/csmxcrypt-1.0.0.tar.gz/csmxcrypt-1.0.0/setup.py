from setuptools import setup, find_packages

setup(
    name="csmxcrypt",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "pillow",
        "numpy"
    ],
    author="Sumedh Patil",
    author_email="admin@aipresso.uk",
    description="AI-proof, post-quantum cryptographic encryption library",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Sumedh1599/csmxcrypt",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
