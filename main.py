#! /usr/bin/python

import sys
import argparse
from packages.process_image import ProcessImage

def main():
    parser = argparse.ArgumentParser(description='Automate naming of certificates. '
                                                 'See https://github.com/devbcdestiller/certificate-automation for more information.')
    parser.add_argument('-n', '--names', type=str, required=True,
                        help='Text file containing the names for the certificates separated by a newline (Enter key). Must be in the source folder.')
    parser.add_argument('-c', '--certificate', type=str, required=True,
                        help='Image template for the certificate. Must be in the source folder.')
    parser.add_argument('-x', default='center', required=False,
                        help='Default: The text will be center aligned from the horizontal axis. '
                             'X/Horizontal position of the text in pixels where it will be pasted into the template certificate.')
    parser.add_argument('-y', type=int, required=True,
                        help='Y/Vertical position of the text in pixels where it will be pasted into the template certificate.')
    parser.add_argument('-f', '--font', type=str, required=True,
                        help='Specify font in TTF format. Must be in the source folder.')
    parser.add_argument('-fs', '--fontsize', type=int, default=50, required=False,
                        help='Default: 50. Specify font size.')

    args = parser.parse_args()

    certs = ProcessImage(f'source/{args.names}', f'source/{args.certificate}', location=(args.x, args.y), font=f'source/{args.font}', font_size=args.fontsize)
    certs.generate_certificates()
    print('Certificate done processing! Saved in /certs.')


if __name__ == '__main__':
    main()
