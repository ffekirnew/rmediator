import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rmediator",
    author="Fikernew Birhanu",
    author_email="fikernew.birhanu.waju@gmail.com",
    description="Request Mediator PyPI (Python Package Index) Package",
    keywords="rmediator, pypi, package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ffekirnew/rmediator",
    project_urls={
        "Documentation": "https://github.com/ffekirnew/rmediator",
        "Bug Reports": "https://github.com/ffekirnew/rmediator/issues",
        "Source Code": "https://github.com/ffekirnew/rmediator",
        # 'Funding': '',
        # 'Say Thanks!': '',
    },
    package_dir={"": "rmediator"},
    packages=setuptools.find_packages(where="rmediator"),
    classifiers=[
        # see https://pypi.org/classifiers/
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    # install_requires=['Pillow'],
    extras_require={
        "dev": ["check-manifest"],
        # 'test': ['coverage'],
    },
    # entry_points={
    #     'console_scripts': [  # This can provide executable scripts
    #         'run=examplepy:main',
    # You can execute `run` in bash to run `main()` in src/examplepy/__init__.py
    #     ],
    # },
)
