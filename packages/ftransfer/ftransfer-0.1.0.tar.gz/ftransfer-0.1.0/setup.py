from setuptools import setup

setup(
    name="ftransfer",  # Pick a unique name
    version="0.1.0",
    packages=["quicktransfer"],
    package_dir={"": "src"},
    install_requires=["tqdm"],
    entry_points={
        "console_scripts": ["ftransfer=quicktransfer.transfer:main"]
    },
)