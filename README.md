# Calendar Date Difference
![example workflow](https://github.com/ruodingt/cald/actions/workflows/ci.yaml/badge.svg)
[![codecov](https://codecov.io/gh/ruodingt/cald/branch/develop/graph/badge.svg?token=3L1YMRWRXV)](https://codecov.io/gh/ruodingt/cald)

This library provide functionality to get differences between two days. 
It can be used as a library or cli tools.

For example:

`"2012-01-10"` <-> `"2012-01-11"` = `0` days

`"2012-01-01"` <-> `"2012-01-10"` = `8` days

`"1801-06-13"` <-> `"1801-11-11"` = `150` days

`"2021-12-01"` <-> `"2017-12-14"` = `1447` days


## Quick starts
Install

```bash
# clone this repo and then install
pip3 install .
# alternatively install the latest dev branch
pip3 install git+https://github.com/ruodingt/cald.git@develop
```

Import as Python lib

```python
from caldiff.date import calendar_date_diff_str
diff = calendar_date_diff_str("2000-12-01", "2000-12-04", signed=False)
print(f"the difference is {diff} days")
```

Using CLI
```bash
cald --help
cald --date1 2000-12-01 --date2 2000-12-04
# or simply do following to run the cli in interaction mode
cald
```

Running with Docker
```bash
docker build -t cald .
# do following to run the cli in interaction mode in container
docker run -it cald cald
```

## Testing

```bash
docker build -t cald .
docker run cald bash run_test.sh
```
