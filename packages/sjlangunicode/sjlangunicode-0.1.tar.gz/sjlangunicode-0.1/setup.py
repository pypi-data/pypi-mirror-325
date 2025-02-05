from setuptools import setup, find_packages

setup(
    name="sjlangunicode",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    author="Sumedh Patil",
    author_email="admin@aipresso.uk",
    description="Advanced Unicode Processing for the SJLang Stacked Language Project.",
    long_description="""sjlangunicode is responsible for mapping characters into a custom 
    Private Unicode range for stacked script processing. This ensures seamless integration
    of Sanskrit-Japanese hybrids within the SJLang ecosystem.""",
    long_description_content_type="text/markdown",
    url="https://github.com/aipresso/sjlangunicode",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Text Processing :: Linguistic",
    ],
    python_requires=">=3.6",
)
