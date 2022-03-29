import setuptools

setuptools.setup(
    name="aiomodrinth",
    version="0.1",
    author="Xemay",
    description="Async API wrapper for modrinth.com",
    long_description_content_type="text/markdown",
    url="https://github.com/Xemay/aiomodrinth",
    project_urls={
        "Bug Tracker": "https://github.com/Xemay/aiomodrinth/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "aiomodrinth"},
    packages=setuptools.find_packages(where="aiomodrinth"),
    python_requires=">=3.6",
)