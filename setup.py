from setuptools import setup, find_packages

setup(
    entry_points={
        'console_scripts': [
            'lambda-toolkit=lambda_toolkit.cli:main'
        ]
    },

    name="lambda_toolkit",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    description="Symbolic lambda calculus interpreter with Church encoding support.",
    author="Laura + Ada",
    python_requires='>=3.8',
)
