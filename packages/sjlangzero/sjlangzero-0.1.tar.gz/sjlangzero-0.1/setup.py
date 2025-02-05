from setuptools import setup, find_packages

setup(
    name="sjlangzero",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    author="Sumedh Patil",
    description="Custom Zero-Width Joiner & Stacked Language Processor",
    long_description="sjlangzero is a foundational library for stacking Sanskrit and Japanese characters using a private zero-width joiner.",
    long_description_content_type="text/markdown",
    url="https://github.com/yourgithub/sjlangzero",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
