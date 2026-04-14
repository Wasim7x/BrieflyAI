from setuptools import setup, find_packages

setup(
    name="BrieflyAI",
    version="0.1.0",
    author="Wasim Hassan",
    description="AI-powered assistant project",
    packages=find_packages(include=["src*", "ui*"]),
    install_requires=[
    ],
    python_requires=">=3.10",
)