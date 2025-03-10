from setuptools import setup, find_packages

setup(
    name="codepromptforge",
    version="0.0.6",  # Increment the version

    # ✅ Find all sub-packages, including assistant
    packages=find_packages(include=["codepromptforge", "codepromptforge.core", "codepromptforge.assistant", "codepromptforge.assistant.*"]),

    include_package_data=True,

    install_requires=[
        "pytest",
        "pydantic",
        "langchain",
        "pathspec",
        "langchain_community",
    ],

    extras_require={
        "assistant": [  # ✅ Installing `[assistant]` installs both dependencies & assistant package
            "langchain_ollama",
            "langgraph",
            "ollama",
            "duckduckgo-search",
            "flask"
        ],
    },

    entry_points={
        "console_scripts": [
            "codepromptforge=codepromptforge.core.cli:main",
            "cli_assistant=codepromptforge.assistant.cli_assistant:main",  # ✅ CLI Assistant
            "web_assistant=codepromptforge.assistant.web_assistant:main",  # ✅ Web Assistant
        ],
    },

    description="A tool to combine code files into a single prompt",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="RG",
    url="https://github.com/RobinsonGarcia/CodePromptForge",
    author_email="rlsgarcia@icloud.com",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)