from setuptools import setup

setup(
    name="php2python",
    version="0.0.1-7fd2331",
    packages=[
        "php",
    ],
    description="Python alternatives for PHP functions",
    url="https://github.com/jxlwqq/php2python",
    author="jxlwqq",
    author_email="jxlwqq@gmail.com",
    license="MIT",
    python_requires=">=3",
    requires=["tzlocal>=1.5", "var_dump>=1.2"],
    zip_safe=False,
)
