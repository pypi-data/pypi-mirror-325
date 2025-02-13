from setuptools import setup, find_packages

setup(
    name='cnv_vcf2json',
    version='2.0.0',
    author='Khaled Jumah',
    author_email='khalled.jooma@yahoo.com',
    description='Converts the CNVkit structural variants VCF file into JSON format',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license = 'CC-BY-NC-4.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'cnv-vcf2json = vcf_converter.cnv_vcf2json:cnv_vcf2json'
        ]
    },
    install_requires=[
        'jsonschema'  # Added jsonschema dependency
    ],
)
