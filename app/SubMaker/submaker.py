from datetime import datetime, timedelta
from lxml import objectify


class SubMaker:

    def __init__(self):
        self.file_content = []

    def generate_time(self, start, duration):
        t = datetime(1, 1, 1, 0, 0, 0)
        b = t + timedelta(seconds=start)
        c = b + timedelta(seconds=duration)
        init_time = str(b.hour).zfill(2) + ':' + str(b.minute).zfill(2) + \
                    ':' + str(b.second).zfill(2) + ',' + \
                    str(b.microsecond).zfill(3)[0:3]
        end_time = str(c.hour).zfill(2) + ':' + str(c.minute).zfill(2) + \
                    ':' + str(c.second).zfill(2) + ',' + \
                str(c.microsecond).zfill(3)[0:3]
        return init_time + ' --> ' + end_time + '\n'

    def fromstring(self, string):
        string = string.replace('<text', '<t')
        string = string.replace('</text', '</t')
        root = objectify.fromstring(string)
        self.file_content = []
        count = 1
        for a in root.t:
            self.file_content.append(str(count) + '\n')
            line_time = self.generate_time(float(a.attrib.get("start")),
                                            float(a.attrib.get("dur")))
            self.file_content.append(line_time)
            self.file_content.append(a + '\n')
            self.file_content.append('\n')
            count += 1
        return self.file_content

    def tofile(self, name=None):
        if name is None:
            name = 'sub.srt'
        outputf = open(name, 'w')
        outputf.writelines(self.file_content)
        outputf.close()