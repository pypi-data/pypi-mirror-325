from setuptools import setup, find_packages


setup(
    name="yt-shorts-grab",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["yt-dlp>=2023.0.0"],
    description="Download all YouTube Shorts from channels with quality selection",
    author="7afidi",
    url="https://github.com/7afidi/yt-shorts-grab"
)

