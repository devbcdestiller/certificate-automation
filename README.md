# Certificate Automation
 Python script that generates personalized certificates from a template.
 
 ## Dependencies
 - Python 3.8 or greater. [Installation](https://www.python.org/downloads/)
 - PIL library. [Installation](https://pillow.readthedocs.io/en/stable/installation.html)

## Installation
- Download the [zip](https://github.com/devbcdestiller/certificate-automation/archive/refs/heads/main.zip) or;
- type `git clone https://github.com/devbcdestiller/certificate-automation.git` in your terminal

Once downloaded go to the directory or `cd certificate-automation` when you want to run the `main.py`.

## Quick Start
- Copy your custom certificate template, text file containing names of the recipients and your font file in TTF format to the `source` folder.  
- Then run `python main.py -n your_names.txt -c your_cert.png -y yPos -f your_font.ttf`.
- Certificates are then saved into the `certs` folder.  
You can adjust the vertical position of the text by using `-y yPos` where yPos is the y position in pixels.

## Commands
|                  Argument                 | Required? | Description                                                                                                                                                             |
|:-----------------------------------------:|:---------:|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                 -h, --help                |     no    | show this help message and exit                                                                                                                                         |
|          -n NAMES, --names NAMES          |    yes    | Text file containing the names for the certificates separated by a newline                         (Enter key). Must be in the source folder.                           |
| -c CERTIFICATE, --certificate CERTIFICATE |    yes    | Image template for the certificate. Must be in the source folder.                                                                                                       |
|                    -x X                   |     no    | Default: The text will be center aligned from the horizontal axis.   X/Horizontal position of the text in pixels where it will be pasted into the template certificate. |
|                    -y Y                   |    yes    | Y/Vertical position of the text in pixels where it will be pasted into the template certificate.                                                                        |
|            -f FONT, --font FONT           |    yes    | Specify font in TTF format. Must be in the source folder.                                                                                                               |
|     -fs FONTSIZE, --fontsize FONTSIZE     |     no    | Default: 50. Specify font size.                                                                                                                                         |
|                                           |           |                                                                                                                                                                         |

## Example Usage
- See `source` folder to view the certificate template, text file and the font file in TTF format.
- Run `python main.py -n names.txt -c sample_cert.png -y 650 -f Arial.ttf`
- See `certs` folder to view the generated certificates.
