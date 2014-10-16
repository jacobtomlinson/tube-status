# _TfL Tube Line Status for Python_
[![PyPi version](https://pypip.in/version/tubestatus/badge.svg)](https://pypi.python.org/pypi/tubestatus/)
[![PyPi downloads](https://pypip.in/download/tubestatus/badge.svg)](https://pypi.python.org/pypi/tubestatus/)
[![Supported Python versions](https://pypip.in/py_versions/tubestatus/badge.svg)](https://pypi.python.org/pypi/tubestatus/)
[![Development Status](https://pypip.in/status/tubestatus/badge.svg)](https://pypi.python.org/pypi/tubestatus/)
[![Build Status](https://travis-ci.org/jacobtomlinson/tube-status.svg?branch=master)](https://travis-ci.org/jacobtomlinson/tube-status)


_A Python module for accessing tube line status data for the London Underground via [Transport for London](https://www.tfl.gov.uk/info-for/open-data-users/our-feeds?intcmp=3671#on-this-page-1)'s open data API._

## Installation

```Bash
$ pip install tubestatus
```

## Example Usage

```Python
import tubestatus

# Create a new status object for retrieving data
current_status = tubestatus.Status()

# Get a list of tube lines
lines = current_status.list_lines()

# Loop through the lines and print the status of each one
for line in lines:
    print line, "-", current_status.get_status(line).description

```

Example output
```
Jubilee - Good Service
Bakerloo - Good Service
Central - Good Service
Metropolitan - Good Service
District - Good Service
Piccadilly - Good Service
Overground - Good Service
Victoria - Good Service
DLR - Good Service
Hammersmith and City - Good Service
Waterloo and City - Good Service
Circle - Good Service
Northern - Good Service

```

## Features
 * List all tube lines
 * Get the current status for a line

## Contributing changes

Please feel free to submit issues and pull requests.

## License

Currently under decision.
