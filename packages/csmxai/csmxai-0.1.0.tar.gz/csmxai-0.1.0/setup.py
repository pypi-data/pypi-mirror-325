from setuptools import setup, find_packages

setup(
    name="csmxai",
    version="0.1.0",
    author="Sumedh Patil",
    author_email="admin@aipresso.uk",
    description="AI-Powered Cyber Defense & Fraud Detection",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Sumedh1599/csmxai",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "cryptography",
        "numpy",
        "scipy"
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.8",
)
