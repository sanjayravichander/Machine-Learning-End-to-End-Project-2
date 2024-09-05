import setuptools

with open("README.md","r",encoding="utf-8") as fh:
    long_description = fh.read()

__version__="0.0.0"

Repo_name="Machine-Learning-End-to-End-Project-2"
author_user_name="sanjayravichander"
src_repo="mlproject"
author_email="sanjay.1991999@gmail.com"

setuptools.setup(
    name=src_repo,
    version=__version__,
    author=author_user_name,
    author_email=author_email,
    description="A small python project for ML End to End Project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{author_user_name}/{Repo_name}",
    project_urls={
        "Bug Tracker": f"https://github.com/{author_user_name}/{Repo_name}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    #python_requires=">=3.6",
)

