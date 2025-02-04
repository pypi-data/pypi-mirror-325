from setuptools import setup, find_packages

setup(
    name="chai_model_config",  # Your package name
    version="0.1.0",  # Versioning
    author="Your Name",
    author_email="your_email@example.com",
    description="A package for evaluating model configurations based on accuracy, latency, and size",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/chai_model_config",  # Replace with your GitHub repo
    packages=find_packages(),
    install_requires=[
        "torch",
        "transformers",
        "datasets",
        "scikit-learn",
        "kneed",
        "numpy"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
