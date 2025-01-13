# dorking

Automates some Google browser-based recon tasks.

Install:

pip install -r requirements.txt
Please add default logging folder, browser information, and Fireprox URL (if any) to settings in code. 

Usage: browser_recon_platform.py [options] 

python3 .\browser_recon_platform.py -d <target domain> -s <search string> -t (optional throttle) -m (optional maximum tabs fired) -a (optional autofire all tests) -o (optional output directory)

Options:
  -h, --help            show this help message and exit
  -d DOMAIN, --domain=DOMAIN
                        Target domain e.g. "behind-bars.com" or "gentex.com"
  -s NAME, --name=NAME  Target search phrase/name e.g. "Behind Bars Bicycle
                        Shop" or "Gentex"
  -t THROTTLE, --throttle=THROTTLE
                        Request throttling in seconds.  Defaults to 0.
  -a, --autofire        Automatically runs all tests in sequence.  Only stops
                        to promt when maximum tabs is met.
  -o OUTDIR, --outdir=OUTDIR
                        Path to directory where output files will be written.
                        Defaults to settings value.
  -m MAXTABS, --maxtabs=MAXTABS
                        Maximum number of tabs fired at your browser before
                        prompting, with the expectation that you will close
                        the browser.  Default is 10.  Best if it is an even
                        number!

Enclose complex strings in single quotes e.g. '/a/file/path' or 'Company Name'

Example:

python3 .\browser_recon_platform.py -d behind-bars.com -s 'Behind Bars' -t 2 -a -o '/tmp/engagement'
