from setuptools import setup, find_packages

setup(
    name="initbysql",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Jinja2',
    ],
    package_data={
        'initbysql': ['templates/*', 'templates/auth/*'],
    },
    entry_points={
        'console_scripts': [
            'initbysql=initbysql.__main__:main',  # Исправлено на __main__
        ],
    },
)