import setuptools

with open("readme.md", mode="r", encoding="utf-8") as fh:
    long_description = fh.read()

REQUIRED_PACKAGES = []

setuptools.setup(
    name="chinese-library-classification",
    packages=['chinese_library_classification'], 
    version="0.0.1",
    author="Sheo Guo",
    author_email="sheoguo@gmail.com",
    author_personalpage="https://sheoguo.github.io/",
    description="Easy to get classification data from Chinese library classification",
    install_requires=REQUIRED_PACKAGES,
    license='MIT License',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sheoguo/Chinese-library-classification",
    package_data={'chinese_library_classification': ['chinese_library_classification/data.json']},
    python_requires=">=3.7",
    include_package_data=True,
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development'
    ],
)
