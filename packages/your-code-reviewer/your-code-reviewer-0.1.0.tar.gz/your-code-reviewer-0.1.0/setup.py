from setuptools import setup, find_packages

setup(
    name="your-code-reviewer",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "requests",
        "python-dotenv",
        "groq",
    ],
    entry_points={
        "console_scripts": [
            "cr-review=cr.cli:review_pr",
        ],
    },
)
