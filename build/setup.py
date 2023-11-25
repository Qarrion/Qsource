from setuptools import setup, find_packages


"""
location file :
    project
        - my_module (import name)
        - my_util

    <setup.py>


    
    """

setup(
    name='my_package (pip name)',
    version='0.0.1',
    packages=find_packages(include=['project']),
    package_data={
        'my_package':['data.ini']
    } # non-py files
)