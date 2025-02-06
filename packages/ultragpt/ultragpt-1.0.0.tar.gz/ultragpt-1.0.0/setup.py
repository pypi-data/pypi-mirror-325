from setuptools import setup, find_packages
from pathlib import Path

# Get the long description from the README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding='utf-8')

setup(
    name='ultragpt',
    version='1.0.0',
    license="MIT",
    author='Ranit Bhowmick',
    author_email='bhowmickranitking@duck.com',
    description='UltraGPT: A modular library for advanced GPT-based reasoning and step pipelines',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages('src', include=["ultragpt", "ultragpt.*"]),
    package_dir={'': 'src'},
    url='https://github.com/Kawai-Senpai',
    install_requires=[
        'pydantic',
        'openai',
        'ultraprint>=3.1.0',
        'duckduckgo_search>=7.3.0' 
    ],
    python_requires='>=3.6',
)
