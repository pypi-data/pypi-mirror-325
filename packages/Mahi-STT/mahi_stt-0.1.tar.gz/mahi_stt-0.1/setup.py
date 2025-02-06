from setuptools import setup,find_packages

setup(
    name='Mahi-STT',
    version='0.1',
    author='Mohit',
    author_email='mksinghmksinghmk@gmail.com',
    description='this is speech to text package '
)
packages = find_packages(),
install_requirements = [
    'selenium',
    'webdriver_manager'

]