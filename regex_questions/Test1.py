import re

text = '''
<div> 
    <span class="actionBar__text"> Showing 18 of 101 products. </span> 
</div>'
'''

pattern = r'Showing \d+ of (\d+) products'
match = re.search(pattern, text)
print(match.group(1))