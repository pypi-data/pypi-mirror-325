import setuptools

setuptools.setup(
    name="matchax",
    version="0.0.1",
    description="A JAX library for generative models with diffusion and flow models",
    url="https://github.com/shuds13/pyexample",
    author="James Thornton",
    author_email="jamestomthornton@gmail.com",
    license="Apache",
    install_requires=[
        "jax",
        "jaxlib",
        "numpy",
    ],
    classifiers=[
        "Programming Language :: Python :: 3.10",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
