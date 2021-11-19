from subprocess import check_call


def test_help():
    check_call('nrf-sniffer-cli --help', shell=True)
