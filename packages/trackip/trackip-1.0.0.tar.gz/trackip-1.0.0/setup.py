from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="trackip",
    version="1.0.0",
    author="Nayan Das",
    author_email="nayanchandradas@hotmail.com",
    description="A CLI tool to track any IP address and get detailed info. 🌍",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nayandas69/trackip",
    project_urls={
        "Bug Tracker": "https://github.com/nayandas69/trackip/issues",
        "Documentation": "https://github.com/nayandas69/trackip#readme",
        "Source Code": "https://github.com/nayandas69/trackip",
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Utilities",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    keywords=[
        "IP tracker",
        "CLI tool",
        "IP geolocation",
        "networking",
        "geolocation",
        "IP lookup",
        "IP address info",
        "public IP checker",
        "CLI geolocation",
        "track IP",
    ],
    packages=find_packages(
        include=["trackip*"], exclude=["tests*", "docs*"]
    ),
    py_modules=["trackip"],
    python_requires=">=3.6",
    install_requires=[
        "requests>=2.25.1",
        "colorama>=0.4.4",
    ],
    entry_points={
        "console_scripts": [
            "trackip=trackip:main_menu",
        ],
    },
    include_package_data=True,
    zip_safe=False,
    license="Apache-2.0",
)
