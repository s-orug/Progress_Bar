#!/usr/local/bin/python3
import time

def progress_bar(current, total):
    total_length = 50
    percent = (float(current) / float(total))
    bar = '█' * int((total_length * percent))  # other option to display '█'
    bar += ' ' * (total_length - len(bar))
    print(f'\r   {bar}| {int(percent * 100)}%', end='\r')


def main():
    for i in range(100):
        progress_bar(i, 99)
        time.sleep(0.02)
    print()


if __name__ == '__main__':
    main()
