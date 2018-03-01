from distutils.core import setup

setup(
    name='easyref',
    version='0.0.1',
    description = 'BibTex citation key generating tool',
    author='CyberNeurons',
    url='https://github.com/Cyber-Neuron/easyref',
    packages=['easyref'],
    install_requires=['fire','bibtexparser'],
    scripts=['bin/easyref'],
)