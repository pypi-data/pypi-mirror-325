from setuptools import setup, find_packages

setup(
    name="mcp-hive",
    version="0.2.0",
    packages=find_packages(),
    install_requires=[
        "rich==13.9.4",
        "python-dotenv==1.0.1",
        "langchain==0.3.15",
        "langchain-anthropic==0.3.4",
        "mcp==1.2.0",
    ],
    author="Ashish Mandal",
    author_email="mandal.ashish@codenation.co.in",
    description="Python SDK for MCP Hive - The hub for all your LLM tools",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/trilogy-group/mcp-hive",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
