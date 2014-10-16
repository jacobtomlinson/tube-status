# _TFL tube line status for Python_
[![PyPi version](https://pypip.in/v/tubestatus/badge.svg?style=flat)](https://pypi.python.org/pypi/datapoint/)
[![PyPi downloads](https://pypip.in/d/tubestatus/badge.svg?style=flat)](https://pypi.python.org/pypi/datapoint/)
[![Supported Python versions](https://pypip.in/py_versions/tubestatus/badge.svg?style=flat)](https://pypi.python.org/pypi/datapoint/)
[![Development Status](https://pypip.in/status/tubestatus/badge.svg?style=flat)](https://pypi.python.org/pypi/datapoint/)
[![Build Status](https://travis-ci.org/jacobtomlinson/tube-status.svg?branch=master)](https://travis-ci.org/jacobtomlinson/tube-status)


_A Python module for accessing tube line status data via [Transport for London](https://www.tfl.gov.uk/info-for/open-data-users/our-feeds?intcmp=3671#on-this-page-1)'s open data API._

## Installation

```Bash
$ pip install tubestatus
```

## Example Usage

```Python
import tubestatus

current_status = tubestatus.Status()

for line in current_status.list_lines():
    print line, "-", current_status.get_status(line)

```

Example output
```
Jubilee - GS
Bakerloo - GS
Central - GS
Metropolitan - GS
District - GS
Piccadilly - GS
Overground - GS
Victoria - GS
DLR - GS
Hammersmith and City - GS
Waterloo and City - GS
Circle - GS
Northern - GS

```

## Features
 * List all tube lines
 * Get the current status for a line

## Contributing changes

Please feel free to submit issues and pull requests.

## License

Currently under decision.
