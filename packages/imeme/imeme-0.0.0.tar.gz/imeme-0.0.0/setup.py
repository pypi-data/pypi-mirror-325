import sys

from setuptools import (find_packages,
                        setup)

project_base_url = 'https://github.com/lycantropos/imeme/'
parameters = dict(packages=find_packages(exclude=('tests', 'tests.*')),
                  url=project_base_url,
                  download_url=project_base_url + 'archive/master.zip')
if sys.implementation.name == 'cpython':
    from setuptools_rust import RustExtension

    parameters.update(
            rust_extensions=[RustExtension('imeme._imeme')],
            zip_safe=False
    )
setup(**parameters)
