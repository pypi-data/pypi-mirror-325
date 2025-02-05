from setuptools import setup
from ast import literal_eval


with open('tgback_x_qt/version.py', encoding='utf-8') as f:
    version = literal_eval(f.read().split('=')[1].strip())

setup(
    name = 'tgback-x-qt',
    version = version,
    packages = [
        'tgback_x_qt',
        'tgback_x_qt.resources',
        'tgback_x_qt.resources._build'
    ],
    license      = 'MIT',
    description  = 'Tgback-XQt is a Qt frontend for tgback-X',
    long_description = open('README.md', encoding='utf-8').read(),
    author_email = 'thenonproton@pm.me',
    url          = 'https://github.com/NotStatilko/tgback-x-qt',
    download_url = f'https://github.com/NotStatilko/tgback-x-qt/archive/refs/tags/v{version}.tar.gz',

    long_description_content_type='text/markdown',

    package_data = {
        'tgback_x_qt': [
            'tgback_x_qt/stylesheet',
            'tgback_x_qt/ui'
        ],
    },
    include_package_data = True,

    install_requires = [
        'tgback-x<2',
        'pyside6-essentials==6.8.1',
        'darkdetect==0.8.0'
    ],
    extras_require = {
        'build': [
            'pyside6==6.8.1',
        ]
    },
    entry_points='''
        [console_scripts]
        tgback-x-qt=tgback_x_qt.app:start_app
    ''',
)
