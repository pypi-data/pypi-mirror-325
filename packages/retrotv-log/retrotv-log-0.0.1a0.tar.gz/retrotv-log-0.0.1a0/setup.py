from setuptools import setup, find_packages

setup(
    name="retrotv-log",
    version="v0.0.1-alpha",
    description="로깅을 위한 패키지",
    author="RetroTV",
    author_email="yjj8353@gmail.com",
    url="https://github.com/retrotv-pypi-repo/log",
    install_requires=[],
    packages=find_packages(exclude=[]),
    keywords=["retrotv", "RetroTV", "yjj8353", "log", "Log", "logging", "Logging", "pypi"],
    python_requires=">=3",
    package_data={},
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3"
    ],
)