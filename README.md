# dorking

Automates some browser-based recon tasks.

General Recon Framework Version: Resolve/Platform Supplementary Browser Recon

Usage:

python3 .\browser_recon_platform.py -d <target domain> -s <search string> -t (optional throttle) -m (optional maximum tabs fired) -a (optional autofire all tests) -o (optional output directory)

Enclose complex strings in single quotes e.g. '/a/file/path' or 'Company Name'
Example:

python3 .\browser_recon_platform.py -d behind-bars.com -s 'Behind Bars' -t 2 -a -o '/tmp/engagement'
