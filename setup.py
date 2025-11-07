"""
Setup script for Student Management System
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="student-management-system",
    version="1.0.0",
    author="Satyam Kumar",
    author_email="your.email@example.com",
    description="A professional student management system built with Python and Tkinter",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/student-management-system",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Topic :: Education :: Computer Aided Instruction (CAI)",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "Environment :: X11 Applications :: Qt",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "student-management=student_management_system:main",
        ],
    },
    keywords="student management system education database gui tkinter mysql",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/student-management-system/issues",
        "Source": "https://github.com/yourusername/student-management-system",
        "Documentation": "https://github.com/yourusername/student-management-system#readme",
    },
)