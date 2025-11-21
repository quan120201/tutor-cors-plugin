from setuptools import setup, find_packages

setup(
    name="tutor-cors-plugin",
    version="0.1.0",
    packages=find_packages(),
    url="https://github.com/quan120201/tutor-cors-plugin",
    project_urls={
        "Code": "https://github.com/quan120201/tutor-cors-plugin",
    },
    include_package_data=True,
    entry_points={
        "tutor.plugin.v1": [
            "cors = cors-plugin.plugin"
        ]
    },
)