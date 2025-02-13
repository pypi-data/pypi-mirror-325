from setuptools import setup, find_packages

setup(
    name="promptbook",
    version="0.2.0",
    description="A CLI-based prompt library with Ollama support.",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "PyYAML",
        "requests",
    ],
    entry_points={
        "console_scripts": [
            "promptbook=promptbook.cli:main",
        ],
    },
    python_requires=">=3.8",
)
