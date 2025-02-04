from setuptools import setup, find_packages

with open("docs/ALTERNATIVE_README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="utilsds",
    version="1.0.13",
    packages=find_packages(),
    install_requires=[
        "pandas>=2.2.2",
        "numpy>=1.26.4",
        "scikit-learn>=1.4.2",
        "seaborn>=0.13.2",
        "matplotlib>=3.9.0",
        "google-cloud-bigquery>=3.22.0",
        "google-cloud-bigquery-storage>=2.0.0",
        "google-cloud-storage>=2.16.0",
        "google-cloud-aiplatform>=1.51.0",
        "scipy>=1.13.0",
        "hyperopt>=0.2.7",
        "tqdm>=4.66.4",
        "xgboost>=1.7.6",
        "lightgbm>=4.0.0",
        "yellowbrick>=1.5",
        "cloudpickle>=2.3.0",
        "db-dtypes>=1.4.0",
        "pygments>=2.19.1",
    ],
    author="DS Team",
    author_email="ds@sts.pl",
    description="Solution for DS Team",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",
)
