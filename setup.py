from setuptools import setup, find_packages
import io

try:
    with io.open("README.md", "r", encoding="utf-8") as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = "A library for African jokes."

setup(
    name='africanjokes',
    version='1.0.0',
    description='A library for African jokes',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Morris D. Toclo',
    author_email='morristoclo@gmail.com',
    license='MIT',
    packages=find_packages(),
    install_requires=[],
    python_requires='>=3.8',
    keywords=['jokes', 'africa', 'fun', 'humor', 'python'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Games/Entertainment",
        "Topic :: Games/Entertainment"
    ],
    entry_points={
        "console_scripts": [
            "africanjokes=africanjokes.cli:main",
        ],
    },
    package_data={
        'africanjokes': ['jokes.txt'],
    },
    url='https://github.com/daddysboy21/africanjokes',
    project_urls={
        "Homepage": "https://github.com/daddysboy21/africanjokes",
        "Author": "https://github.com/daddysboy21",
        "Website": "https://daddysboy21.link",
        "Funding": "https://buymeacoffee.com/PBEzMY14YC",
        "Source": "https://github.com/daddysboy21/africanjokes",
        "Tracker": "https://github.com/daddysboy21/africanjokes/issues",
        "Documentation": "https://github.com/daddysboy21/africanjokes/wiki",
        "License": "https://github.com/daddysboy21/africanjokes/blob/main/LICENSE",
    },
    include_package_data=True,
    zip_safe=False,
)