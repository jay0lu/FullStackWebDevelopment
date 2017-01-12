import cgi

# use python build in function cgi.escape
def escape_string(s):
    # for(i,o) in (("&", "&amp;"),
    #               (">", "&gt;"),
    #               ("<", "&lt;"),
    #               ('"', "&quot;")):
    #     s = s.replace(i,o)
    # return s

    return cgi.escape(s, quote = True)

print(escape_string("<b>html!</b>"))
