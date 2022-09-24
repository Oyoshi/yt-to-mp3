import sys


def log(*args):
    print(*args)


def debug_log(*args):
    print("DEBUG: ", *args)


green = "\033[38;2;00;255;65m"
default = "\033[39m"


def on_progress(chunk, file_handle, bytes_remaining):
    filesize = chunk.filesize
    current = (filesize - bytes_remaining) / filesize
    percent = ("{0:.1f}").format(current * 100)
    progress = int(50 * current)
    status = "█" * progress + "-" * (50 - progress)
    sys.stdout.write(green + f'|{status}| {percent}%\r' + default)
    sys.stdout.flush()
