from setuptools import setup, find_packages

# ✅ Find all sub-packages, including `assistant`
core_packages = find_packages(include=["codehammer", "codehammer.core"])

setup(
    name="codehammer",
    version="0.0.1",  # Increment the version

    # ✅ Only install core by default
    packages=core_packages,  

    include_package_data=True,

    install_requires=[
        "pytest",
        "pydantic",
        "langchain",
        "pathspec",
        "langchain_community",
    ],

    entry_points={
        "console_scripts": [
            "code-hammer=codehammer.core.cli:main",
            "codehammer=codehammer.core.cli:main",
        ],
    },

    description="A tool to combine code files into a single prompt",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="RG",
    url="https://github.com/RobinsonGarcia/CodeHammer",
    author_email="rlsgarcia@icloud.com",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)