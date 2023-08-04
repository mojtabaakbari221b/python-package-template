import setuptools

with open("README.md", "r") as f:
    description = f.read()

setuptools.setup(
    name="{{ cookiecutter.project_name }}",
    version="{{ cookiecutter.package_version }}",
    author="{{ cookiecutter.author_name }}",
    author_email="{{ cookiecutter.author_email }}",
    packages=["{{ cookiecutter.project_slug }}"],
    description="{{ cookiecutter.project_description }}",
    long_description=description,
    long_description_content_type="text/markdown",
    url="{{ cookiecutter.project_github_url }}",
    license='MIT',
    python_requires='>=3.7',
    install_requires=[],
)