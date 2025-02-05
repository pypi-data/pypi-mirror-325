from setuptools import setup, find_packages

setup(
    name="mcp-mssql",
    version="0.1.3",
    author="amornpan",
    author_email="amornpan@gmail.com",
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
        "fastapi>=0.104.1",
        "pydantic>=2.10.6", 
        "uvicorn>=0.34.0",
        "python-dotenv>=1.0.1",
        "pyodbc>=4.0.35",
        "anyio>=4.5.0",
        "mcp==1.2.0"
    ],
)