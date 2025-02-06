from setuptools import setup, find_packages

setup(
    name="tiingo_fetcher",  # Package name
    version="0.1.1",  # Version number
    packages=find_packages(),  # Automatically detect the package
    install_requires=[
        "pandas",
        "requests",
        "python-dateutil",
        "python-dotenv"
    ],
    author="Abdulmalik ALossimi",
    author_email="abdulmalikosaimy@gmail.com",
    description="Fetch large amounts of historical stock data from Tiingo for free.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/chaikrk/tiingo-data-fetcher",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
