from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="tile-image-grid",
    version="0.1.0",
    author="Jason Schwarz",
    author_email="jason.c.schwarz@gmail.com",
    description="A tool that takes an image and creates a grid of tiles",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/passandscore/tile-image-grid",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.7",
    install_requires=[
        "click>=7.0",
        "Pillow>=8.0.0",
        "torch>=1.7.0",
        "diffusers>=0.11.1",
        "transformers>=4.25.1",
    ],
    entry_points={
        "console_scripts": [
            "tile-image-grid=tile_image_grid.cli:main",
        ],
    },
) 