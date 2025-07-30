from setuptools import setup, find_packages
import io

try:
    with io.open("README.md", "r", encoding="utf-8") as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = "A library for African jokes."

setup(
    name='africanjokes',
    version='0.0.5',
    description='A library for African jokes',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Morris D. Toclo',
    author_email='morristoclo@gmail.com',
    url='https://daddysboy21.link',
    license='MIT',
    packages=find_packages(),
    install_requires=[],
    python_requires='>=3.8',
    keywords=['jokes', 'africa', 'fun', 'humor', 'python'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Topic :: Entertainment',
    ],
    project_urls={
        "GitHub": "https://github.com/daddysboy21",
        "Author Website": "https://daddysboy21.link",
        "Support": "https://buymeacoffee.com/PBEzMY14YC",
    },
    include_package_data=True,
    zip_safe=False,
)