from subprocess import check_call, CalledProcessError
import pytest


def test_help():
    check_call('nrf-sniffer-cli --help', shell=True)


def test_sniff_help():
    check_call('nrf-sniffer-cli sniff --help', shell=True)


def test_scan_help():
    check_call('nrf-sniffer-cli scan --help', shell=True)


def test_invalid_args():
    with pytest.raises(CalledProcessError) as error:
        check_call('nrf-sniffer-cli invalid', shell=True)
    assert error.value.returncode == 2
