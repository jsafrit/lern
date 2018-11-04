"""
At the heart of this class will be the same list of dicts.  That is, when we create an instance of our LogDicts
class, we'll load the entire file into memory.  (You can assume that the logfile isn't too big; perhaps in the future,
we'll talk about "chunking" files that are too load to read all at once.)  Then, with that in place, we'll be able to
invoke a number of different methods:
    ld = LogDicts('mini-access-log.txt')

Again, creating an instance of LogDicts will load the list of dicts into the object, making them available for our use.
    ld.dicts(key=None)      # return the list of dicts, same as last week's exercise
    ld.iterdicts(key=None)  # returns an iterator of dicts, rather than the list all at once

    ld.earliest()   # returns the dict with the earliest timestamp
    ld.latest()     # returns the dict with the latest timestamp

In order for these two methods to work, you'll need to turn the timestamp into an actual time object. I'd suggest
using time.strptime, although there are alternatives on PyPI that you might prefer, such as "arrow".
    ld.for_ip(ip_address, key=None)   # returns all records for a particular IP address
    ld.for_request(text, key=None)    # returns all records whose request contains text

The above will return a subset of the list, filtering for certain IP addresses and text. The text can be a plain
ol' string; you don't have to use a regexp. Unless you want to do so, of course...

If you're wondering why ld.dicts, ld.iterdicts, and for_ip all take a "key" parameter, it's because we want our users
to be able to sort the resulting list of dictionaries. For example, I should be able to say:
    def by_ip_address(one_log_dict):
        return one_log_dict['ip_address']

    ld.dicts(key=by_ip_address)

The function can be a lot more complex than this, if we want. But it's nice to be able to sort the results according
to something we want, such as (for example) the path of the request.
"""
import operator

filename = 'mini-access-log.txt'


class LogDicts:
    def __init__(self, filename):
        self.filename = filename

    def dicts(self, key=None):
        if key:
            return sorted(logtolist(self.filename), key=key)
        else:
            return logtolist(self.filename)

    def iterdicts(self, key=None):
        for dic in logtolist(self.filename):
            yield dic

    def earliest(self):
        return self.dicts(key=operator.itemgetter('timestamp'))[0]

    def latest(self):
        return self.dicts(key=operator.itemgetter('timestamp'))[-1]

    def for_ip(self, ip_addr):
        return [i for i in self.dicts() if i['ip_address'] == ip_addr]

    def for_request(self, requests):
        return [i for i in self.dicts() if requests in i['request']]


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
