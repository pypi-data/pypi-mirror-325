from setuptools import setup, find_packages

setup(
    name="django-vite-app",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "django>=4.0",
        "djangorestframework",
        "django-cors-headers",
    ],
    author="Sidjane Assemien",
    author_email="sidjaneassemien1@gmail.com",
    description="Script pour créer un projet Django avec Vite et Tailwind CSS",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    #url="https://github.com/sidjaneassemien/django-vite-app",
    entry_points={
        "console_scripts": [
            "create-django-vite-app=scripts.create_project:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Framework :: Django",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
)
