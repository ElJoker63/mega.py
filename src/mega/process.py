from humanize import naturaldate, naturalday, naturaldelta, naturalsize, naturaltime
import os
from platform import system

global cmd
if system() == "Linux":
    cmd = "clear"
elif system() == "Windows":
    cmd = "cls"

start_time = 0


def create_progress_bar(current, total, filename, eta, speed, length=20):
    filled_length = int(length * current // total)
    bar = "●" * filled_length + "○" * (length - filled_length)
    percentage = round((current / total) * 100, 2)
    os.system(cmd)
    return f"{filename}\nDownload: {percentage}%\n[{bar}]\n{naturalsize(current)} of {naturalsize(total)}\nSpeed: {naturalsize(speed)}/s\nETA: {format_time(int(eta))}"


def format_time(seconds):
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return f"{hours:02d}h:{minutes:02d}m:{seconds:02d}s"
