# Finding the email address inside the string

import re
search ="intensive.learnings@cigna.com"
fullstring = "xyz intensive.learnings@cigna.com purple monkey"
s = re.search(search,fullstring)
print(s.group())