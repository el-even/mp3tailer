import re

description = """
This is the "title" of a 'book' by O'Henry
Sometimes it is "book2", "book3" and 'book4'.
"""

def typographer(pattern, substitute, string):
    string = string.decode("utf-8")
    result = re.sub(pattern, substitute, string).encode("utf-8")
    return result


def strip(text):
    result = text
    result = typographer(" (\"|\')", u" \xab", result)
    result = typographer("(\"|\') ", u"\xbb ", result) # don't like these similar lines
    result = typographer("(\"|\')\.", u"\xbb.", result)
    result = typographer("\((\"|\')", u"(\xab", result)
    result = typographer("(\"|\')\)", u"\xbb)", result)
    return result

print strip(description)