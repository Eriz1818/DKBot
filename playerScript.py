import DraganKnight
import random
import time
import re
import mechanize

browser = mechanize.Browser()
browser.addheaders = [
            ("User-agent", "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:30.0) Gecko/20100101 Firefox/30.0")]
browser.open("http://dragon.se7enet.com/login.php?do=login")
browser.select_form(nr=0)
browser.form["username"] = "eriz18"
browser.form["password"] = "testtest"
response = browser.submit()
print ("Creds Submitted")

f = open('out.html', 'a')
f.write('<tr> <td> Sr No. </td> <td> NAME </td> <td> LEVEL </td> <td> EXP </td> <td> GOLD </td> </tr> \n')
for i in range(1,32754):
    html = browser.open("http://dragon.se7enet.com/index.php?do=onlinechar:%d"%i).get_data()
    # print(html)
    name_match = re.search("Here is the character profile for <b>(.*?)</b>", html)
    level_match = re.search("Level: (.*?)<br />", html)
    exp_match = re.search("Experience: (.*?)<br />", html)
    gold_match = re.search("Gold: (.*?)<br />", html)
    if(name_match):
        if(int(level_match.group(1)) > 10):
            f.write('<tr> <td> %s </td> <td> %s </td> <td> %s </td> <td> %s </td> <td> %s </td> </tr> \n' % (i,
            name_match.group(1), level_match.group(1), exp_match.group(1), gold_match.group(1)))

f.close()