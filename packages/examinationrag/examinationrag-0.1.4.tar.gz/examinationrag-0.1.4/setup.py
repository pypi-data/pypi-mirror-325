import os
import re

from setuptools import find_packages, setup

def get_requires():
    with open("requirements.txt", "r", encoding="utf-8") as f:
        file_content = f.read()
        lines = [line.strip() for line in file_content.strip().split("\n") if not line.startswith("#")]
        return lines


extra_require = {
    'jury': ['jury']
}


def main():
    setup(
        name="examinationrag",
        version='0.1.4',
        author="DocAILab",
        author_email="luoyangyifei@buaa.edu.cn",
        description="XRAG: eXamining the Core - Benchmarking Foundational Component Modules in Advanced Retrieval-Augmented Generation",
        long_description=open("README.md", "r", encoding="utf-8").read(),
        long_description_content_type="text/markdown",
        keywords=["RAG", "LLM", "ChatGPT", "LLamaIndex", "Benchmarking"],
        license="Apache 2.0 License",
        url="https://github.com/DocAILab/XRAG",
        package_dir={"": "src"},
        packages=find_packages("src"),
        package_data={
            "xrag": ["default_config.toml"],
        },
        python_requires=">=3.9.0",
        install_requires=get_requires(),
        extras_require=extra_require,
        entry_points={"console_scripts": ["xrag-cli = xrag.cli:main"]},
        classifiers=[
            "Development Status :: 4 - Beta",
            "Intended Audience :: Developers",
            "Intended Audience :: Education",
            "Intended Audience :: Science/Research",
            "License :: OSI Approved :: Apache Software License",
            "Operating System :: OS Independent",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
            "Programming Language :: Python :: 3.11",
            "Topic :: Scientific/Engineering :: Artificial Intelligence",
        ],
    )


if __name__ == "__main__":
    main()
