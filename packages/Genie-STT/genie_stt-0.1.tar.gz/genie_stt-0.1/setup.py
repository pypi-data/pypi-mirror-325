from setuptools import setup,find_packages

setup(
    name='Genie-STT',
    version='0.1',
    author='Samir Prasad',
    author_email='samirprasad075@gmail.com',
    description='this is speech to text package created by samir prasad'
)
packages = find_packages(),
install_requirements = [
    'selenium',
    'webdriver_manager'
]
