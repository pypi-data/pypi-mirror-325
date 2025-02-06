from setuptools import setup, find_packages

setup(
    name="VortexWEB",
    version="0.1.0",
    description="A simple HTTP API framework for building RESTful APIs",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="Murat",
    url="https://github.com/yourusername/simple-http-api-framework",
    packages=find_packages(include=["core", "core.*"]),
    install_requires=[
        "jinja2",  # Для рендеринга шаблонов
        "requests"  # Если нужно для тестирования или работы с API
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
