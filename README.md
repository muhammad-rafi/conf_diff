[![license](https://img.shields.io/github/license/abatilo/actions-poetry.svg)](https://github.com/muhammad-rafi/conf_diff/blob/main/LICENSE)
[![Pypi](https://img.shields.io/pypi/v/conf_diff.svg)](https://pypi.org/project/conf-diff/) 
[![Build Status](https://github.com/muhammad-rafi/conf_diff/actions/workflows/main.yml/badge.svg)](https://github.com/muhammad-rafi/conf_diff/actions)

# Introduction

This module is built to provide you the configuration comparison between two configuration files and generates configuration differences either on the terminal or create a HTML output file based on the parameter provided to the module.

Note: This module is built on the top of the Python built-in difflib module but modified to show you the colourful output and customised HTML template.

## Features

* Shows the configuration differences on the terminal window with colourful output.
* Generate a HTML output file as a comparison report.

## Installation

Install this module from PyPI:

```sh
pip install conf_diff
```

## Usage:

### Prerequisite
As this module compares the configuration difference between two config file, so we need to have two configuration files should be present in the same directory where you are running the script from or specify the absolute path for the configuration files. e.g. `"/Users/rafi/sandbox-nxos-1.cisco.com_before_config.cfg"` and `"/Users/rafi/sandbox-nxos-1.cisco.com_after_config.cfg"
`

You may use either .cfg or .txt file extensions.

In the below example, I am using two running configuration files from the Cisco always-on NXOS Sandbox, assuming that, `sandbox-nxos-1.cisco.com_before_config.cfg` was taken before the change and ` sandbox-nxos-1.cisco.com_after_config.cfg` after the change, and we want to see the configuration diffrence between them. You may name the filenames as you like or add the timestamps.

Import the module on your python script and instantiate a class object 'delta'

```python
import conf_diff

# Instantiate a class object 'delta'
delta = conf_diff.ConfDiff("sandbox-nxos-1.cisco.com_before_config.cfg", "sandbox-nxos-1.cisco.com_after_config.cfg")

# Display the output of the diff on the terminal 
print(delta.diff())
```
Above will generate a configuration difference on the terminal. 

![App Screenshot](https://github.com/muhammad-rafi/conf_diff/blob/main/images/cli_output.png)

To generate a html output file, add third parameter as the expected output file name. e.g. `"html_diff_output.html"`

```python
 # Instantiate a class object 'delta'
delta = conf_diff.ConfDiff("sandbox-nxos-1.cisco.com_before_config.cfg", "sandbox-nxos-1.cisco.com_after_config.cfg", "html_diff_output.html")

# Generates a `html_diff_output.html` in your current directory unless expected full path is specified.
delta.diff()
```
See the screenshot below for the `html_diff_output.html`
![App Screenshot](https://github.com/muhammad-rafi/conf_diff/blob/main/images/html_output_file.png)

## Issues
Please raise any issue or pull request if you find something wrong with this module.

## Authors
[Muhammad Rafi](https://github.com/muhammad-rafi)

## License
The source code is released under the MIT License.
