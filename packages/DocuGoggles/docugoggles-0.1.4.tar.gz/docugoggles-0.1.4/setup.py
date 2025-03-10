from setuptools import setup, find_packages

setup(
    name="DocuGoggles",
    version="0.1.4",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
    entry_points={
        'console_scripts': [
            'docugoggles=file_search.main:main',
        ],
    },
    author="Naif ALqurashi",
    author_email="Naif.cen@gmail.com",
    description="A tool for scanning and analyzing files in directories",
    long_description="DocuGoggles - A File Search and Analysis Tool",
    long_description_content_type="text/markdown",
    url="https://github.com/Duquesne-Spring-2025-COSC-481/Naif-ALqurashi",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    license="MIT",
)