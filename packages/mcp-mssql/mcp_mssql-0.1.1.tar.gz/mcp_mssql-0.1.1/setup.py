from setuptools import setup, find_packages

setup(
    name="mcp-mssql",
    version="0.1.1",
    author="amornpan",
    author_email="your.email@example.com",
    description="MSSQL server package for MCP",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/amornpan/mcp-mssql",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "python-dotenv",
        "pyodbc",
        "pydantic"
    ],
)