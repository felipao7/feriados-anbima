from setuptools import setup, find_packages

setup(
    name='feriados-anbima',
    version='0.1.0',
    description='Módulo para listar feriados da ANBIMA, compatível com bibliotecas de calendário bizdays, business_calendar....',
    long_description=open('README.md').read(),
    author='felipao7',
    author_email='felipe.net.online@gmail.com',
    url='https://github.com/felipao7/feriados-anbima.git',
    packages=find_packages(),
    install_requires=[
        'xlrd',
        'pytest',
        'business_calendar',
    ]
)
