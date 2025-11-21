from setuptools import setup, find_packages

setup(
    name="cors-plugin",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        "tutor.plugin.v1": [
            "cors = cors_plugin.plugin"
        ]
    },
)