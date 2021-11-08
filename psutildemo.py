import os
import psutil


def main():
    # Output current CPU usage as a percentage
    print('CPU usage is {} %'.format(get_cpu_usage_pct()))
    # Output current CPU frequency in MHz.
    print('CPU frequency is {} MHz'.format(get_cpu_frequency()))
    # Output current RAM usage in MB
    print('RAM usage is {} MB'.format(int(get_ram_usage() / 1024 / 1024)))
    # Output total RAM in MB
    print('RAM total is {} MB'.format(int(get_ram_total() / 1024 / 1024)))
    # Output current RAM usage as a percentage.
    print('RAM usage is {} %'.format(get_ram_usage_pct()))
    # Output current Swap usage in MB
    print('Swap usage is {} MB'.format(int(get_swap_usage() / 1024 / 1024)))
    # Output total Swap in MB
    print('Swap total is {} MB'.format(int(get_swap_total() / 1024 / 1024)))
    # Output current Swap usage as a percentage.
    print('Swap usage is {} %'.format(get_swap_usage_pct()))


def get_cpu_usage_pct():
    """
    Obtains the system's average CPU load as measured over a period of 500 milliseconds.
    """
    return psutil.cpu_percent(interval=0.5)


def get_cpu_frequency():
    """
    Obtains the real-time value of the current CPU frequency in MHz.
    """
    return int(psutil.cpu_freq().current)


def get_ram_usage():
    """
    Obtains the absolute number of RAM bytes currently in use by the system.
    """
    return int(psutil.virtual_memory().total - psutil.virtual_memory().available)


def get_ram_total():
    """
    Obtains the total amount of RAM in bytes available to the system.
    """
    return int(psutil.virtual_memory().total)


def get_ram_usage_pct():
    """
    Obtains the system's current RAM usage.
    """
    return psutil.virtual_memory().percent


def get_swap_usage():
    """
    Obtains the absolute number of Swap bytes currently in use by the system.
    """
    return int(psutil.swap_memory().used)


def get_swap_total():
    """
    Obtains the total amount of Swap in bytes available to the system.
    """
    return int(psutil.swap_memory().total)


def get_swap_usage_pct():
    """
    Obtains the system's current Swap usage.
    """
    return psutil.swap_memory().percent


if __name__ == "__main__":
    main()
