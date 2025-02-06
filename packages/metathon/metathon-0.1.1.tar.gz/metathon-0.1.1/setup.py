from setuptools import setup

setup(
    name="metathon",
    version="0.1.1",
    packages=["metathon"],
    install_requires=["requests","pycryptodomex"],
    author="Moh Iqbal Hidayat",
    author_email="iqbalmh18.dev@gmail.com",
    description="A Python wrapper for Meta social media API's",
    long_description="Metathon is a lightweight and user-friendly Python wrapper designed to interact seamlessly with Meta's social media platforms, including Threads, Facebook, and Instagram. It simplifies API integrations, making it easier for developers to build and manage social media automation, analytics, and content publishing solutions.",
    long_description_content_type="text/plain",
    url="https://pypi.org/project/metathon",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
)