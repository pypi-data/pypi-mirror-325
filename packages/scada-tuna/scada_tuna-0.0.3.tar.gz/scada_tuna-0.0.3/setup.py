from setuptools import setup, find_packages

setup(
	name='scada-tuna',
	version='0.0.3',
	author='aiyojun',
	author_email='aiyojun@gmail.com',
	description='Generic PLC client',
	long_description=open('README.rst', encoding='utf-8').read(),
	url='https://github.com/aiyojun/scada-tuna',
	packages=find_packages(),
	license='MIT',
	keywords=['plc', 'modbus', 'mcprotocol'],
	classifiers=[
		'Programming Language :: Python :: 3',
	],
	python_requires='>=3.8',
	install_requires=[
		'pymcprotocol==0.3.0',
		'pymodbus==3.6.4'
	],
)