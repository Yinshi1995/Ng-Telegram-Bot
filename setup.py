from setuptools import setup

setup(
    name='telegram_bot',
    version='0.0.1',
    packages=['telegram_bot'],
    package_dir={'telegram_bot': 'src'},
    install_requires=[
        'aiogram',
        'python-dotenv'
    ],
    entry_points={
        'console_scripts': [
            'start_bot = telegram_bot:go',
        ],
    },
)
