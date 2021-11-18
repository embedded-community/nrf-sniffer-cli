# nrf-sniffer-cli

This package provides python APIs and simple command line tool for nRF sniffer.

## Hardware and firmware requirements

See nRF sniffer documentation for supported hardware and how to flash the firmware: https://infocenter.nordicsemi.com/index.jsp?topic=%2Fug_sniffer_ble%2FUG%2Fsniffer_ble%2Fintro.html

## Basic usage

Installing nrf-sniffer-cli and its dependencies:

```
$ pip install git+https://github.com/embedded-community/nrf-sniffer-cli.git
```

To start sniffing plug in the sniffer dongle and first scan for advertising devices.
```
$ nrf-sniffer-cli --scan
```

Then select the device you are interested in sniffing and start the sniffer:

```
$ nrf-sniffer-cli --address 001122334455
```

Or by name:

```
$ nrf-sniffer-cli --name example-name
```

By default, the sniffer will write the captured packets to `capture.pcap` file. This is configurable with:

```
$ nrf-sniffer-cli --name example-name --capture-file example-capture.pcap
```

Sniffer can be stopped using ctrl+c.


## Structure of the project

 * cli
   * command line interface for capturing Bluetooth LE traffic using nRF sniffer hardware
 * SnifferAPI
   * API copied directly from Nordic's nRF sniffer software package: https://www.nordicsemi.com/Products/Development-tools/nRF-Sniffer-for-Bluetooth-LE/Download?lang=en#infotabs


