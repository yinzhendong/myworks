import re

# * 0次或任意次
# + 1次或任意次
# ? 0次或1次

m = re.match("([abc])+", "abc")
print(m.groups())

m = re.match("(?:[abc])+", "abc")
print(m.groups())

p = re.compile(r'(?P<word>\b\w+\b)')
m = p.search( '(((( Lots of punctuation ')
print(m .group('word'))
print(m .group(1))

m = re.match(r'(?P<first>\w+) (?P<last>\w+)', 'Jane Doe')
print(m.groupdict())
