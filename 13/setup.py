from setuptools import Extension, setup

setup(
    name="Matrix_power",
    version="1.0.0",
    description="Python interface for matrix powering in C",
    author="ELz0N1",
    author_email="d.zhukov1@g.nsu.ru",
    ext_modules=[
        Extension(
            name="foreign",
            sources=["foreignmodule.c"],
        ),
    ]
)
