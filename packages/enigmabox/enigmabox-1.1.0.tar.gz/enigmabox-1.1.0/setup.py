from setuptools import setup, find_packages

setup(
    name="enigmabox",
    version="1.1.0",
    description="EnigmaBox  is a Python library for secure text encryption and decryption using AES-256  and Argon2id . It combines industry-standard cryptographic algorithms with a simple, intuitive interface, making it easy to protect sensitive data with strong encryption. Perfect for developers who need robust security without complexity.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "cryptography",
        "argon2-cffi",
    ],
)
