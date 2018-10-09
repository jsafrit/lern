"""
The exercise is to write a function that, when given a filename, returns a list of dictionaries.
Each dict should have the following keys:
  - ip_address, containing the IP address
  - timestamp, containing the timestamp (not including the square brackets, but everything inside of them)
  - request, containing the HTTP request (not including the double quotes, but everything inside of them)

Thus, the above line from mini-access-log.txt would look like this:
    {'ip_address': '67.218.116.165',
     'timestamp': '30/Jan/2010:00:03:18 +0200',
     'request': 'GET /robots.txt HTTP/1.0'}
We'll transform the file into a list of dicts, each of which looks that.  There are 206 lines in the file, which means
that this list will contain 206 dictionaries, each with these three key-value pairs.

Using a regular expression will definitely help here -- but if you don't know regexps, then don't worry; you can still
get it to work. That said, it'll be a bit clunky.
"""

filename = 'mini-access-log.txt'


def logtolist(logfilename):
    result = []

    with open(logfilename, 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            line_dict = dict()
            line_dict['ip_address'] = line[:line.find(' ')]
            line_dict['timestamp'] = line[line.find('[') + 1:line.find(']')]
            first_quote = line.find('"') + 1
            line_dict['request'] = line[first_quote:line.find('"', first_quote)]
            result.append(line_dict)
    return result


if __name__ == '__main__':
    log_dict = logtolist(filename)
    for d in log_dict[:4]:
        print(d)