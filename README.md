# **Company Information Analysis Software** 
A software to search and download company information, and generate Excel report.

[![standard-readme compliant](https://img.shields.io/badge/Lauguage-Python-brightgreen.svg?style=flat-square)](https://github.com/MatthewTsan/qichachaCrawler)

[![standard-readme compliant](https://img.shields.io/badge/Urllib-blue.svg?style=flat-square)](https://github.com/MatthewTsan/qichachaCrawler)
[![standard-readme compliant](https://img.shields.io/badge/BeautifulSoup-blue.svg?style=flat-square)](https://github.com/MatthewTsan/qichachaCrawler)
[![standard-readme compliant](https://img.shields.io/badge/pandas-blue.svg?style=flat-square)](https://github.com/MatthewTsan/qichachaCrawler)
[![standard-readme compliant](https://img.shields.io/badge/OpenPyxl-blue.svg?style=flat-square)](https://github.com/MatthewTsan/qichachaCrawler)


## Table of Contents

- [Functions](#funcitons)
- [Build and Run](#build-and-run)
  - [Run from Source code](#run-from-source-code)
  - [Generate exe File](#generate-.exe-file)
  - [Report](#report)
- [Maintenance](#maintenance)
- [License](#license)

## Functions

- Automatic log in Qichacah website and keep loging in
- Read keyword in Excel and search in system
- For each search result, download the company information and generate report

## Build and Run

This project uses python. You can directly run from source file or generate .exe file.

### Run from source code

1. Setup Python environment. Install Python3.

2. Install requirement using pip:
```bash
pip install -r requirements.txt
```
3. Log in Qichacha website, and copy the cookie into ./cookie.txt
4. Copy your keyword file into ./ and modify the ./conf.cfg, replace file_test_name and file_sheet_name with your test file name and sheet file name.
5. Run crawnler/main.py
```bash
python main.py
```

### Generate .exe file
To generate .exe file you will need to use Pyinstaller

1. Setup Python environment and install Pyinstaller
```bash
pip install pyinstaller
```
2. Prepare a virtual env with no package installed and install the only package above
3. generate exe file
```
pyinstaller --onefile main.py
```
4. You will still need to have files:
+ cookie.txt
+ config.cfg
+ test file with Excel format

### Report

The software will create a ./result folder and generate a report under it. 

For each company shareholder change, it will generate a new line.


## Maintenance

The Qichacha website will change their website style sometimes. This software is not guarentieed that the website anylize part is up-to-date. If you would like to use the software, please check that part.

## License

[MIT](LICENSE) © Richard Littauer
