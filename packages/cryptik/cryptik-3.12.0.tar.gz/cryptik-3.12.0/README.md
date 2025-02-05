## About

a [cli](https://en.wikipedia.org/wiki/Command-line_interface) application for displaying the current price of a cryptocurrency, designed (but not limited) to be ran in conky. cryptik supports multiple exchanges and multiple currencies.

Please see the project wiki for supported currencies and supported exchanges or to request new currencies/exchanges.


## Latest Changes

- update copyright date
- package updates: click


## NOTICES

- version 3.11.0 requires python 3.11+ (for internal toml processing capabilities and...its faster)


## Install

We recommend using [pipx](https://github.com/pypa/pipx) to install cryptik: `pipx install cryptik`. You can also install via pip: `pip install --user cryptik`.

cryptik uses a config file to store your setup. This file contains information such as the exchange(s) to use. You can grab the sample config file from  [cryptik/example/config.toml](https://gitlab.com/drad/cryptik/-/blob/master/example/config.toml) and place it in `~/.config/cryptik` as this is where cryptik looks for the file by default or you can place it anywhere you like and use the `--config-file` parameter to specify the location.


## Usage

- call cryptik from command line: `cryptik -e BITSTAMP -t BTC`
  + show full response: `cryptik.py -d full`
- list all available exchanges: `cryptik.py -l`
- get help on cryptik: `cryptik.py -h`
- example conky usage (note: this will show prices from two exchanges):

```
CRYPTIK
  ${texeci 600 cryptik -e KRAKEN -t BTC}
  ${texeci 600 cryptik -e BITSTAMP -t BTC}
```

## Example Response

- direct call:
```
$ cryptik -e BITSTAMP -t BTC
BTMP:BTC $9711.24 @12:33
```
