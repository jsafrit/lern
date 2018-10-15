import re

logfilename = 'mini-access-log.txt'


def re_line_to_dict(line):
    regexp = r'''
((?:\d{1,3}\.){3}\d{1,3})       # IP addresses contain four numbers (each with 1-3 digits)
.*                              # Junk between IP address and timestamp
\[([^\]]+)\]                    # Timestamp, defined to be anything between [ and ]
.*                              # Junk between timestamp and request
"(GET[^"]+)"                    # Request, starting with GET
'''
    m = re.search(regexp, line, re.X)

    if m:
        ip_address = m.group(1)
        timestamp = m.group(2)
        request = m.group(3)

    else:
        ip_address = 'No IP address found'
        timestamp = 'No timestamp found'
        request = 'No request found'

    output = {'ip_address': ip_address,
              'timestamp': timestamp,
              'request': request}
    return output


def line_to_dict(line):
    ip_address = line.split()[0]

    timestamp_start = line.index('[') + 1
    timestamp_end = line.index(']')
    timestamp = line[timestamp_start:timestamp_end]

    request_start = line.index('"') + 1
    request_end = line[request_start:].index('"')
    request = line[request_start:request_start+request_end]

    return {'ip_address': ip_address,
            'timestamp': timestamp,
            'request': request}


def logtolist(filename):
    return [line_to_dict(line)
            for line in open(filename)]


for one_item in logtolist(logfilename):
    print(one_item)
