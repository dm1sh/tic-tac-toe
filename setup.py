import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
  long_description = fh.read()

setuptools.setup(
    name="tic-tac-toe-dm1sh",
    version="0.0.1",
    author="dm1sh",
    author_email="me@dmitriy.icu",
    description="A simple tic tac toe game implementation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dm1sh/tic-tac-toe",
    project_urls={
        "Bug Tracker": "https://github.com/dm1sh/tic-tac-toe/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
