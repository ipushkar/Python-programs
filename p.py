import urllib2
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

page="http://www.imdb.com/search/title?genres=horror&explore=title_type,genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=75c37eae-37a7-4027-a7ca-3fd76067dd90&pf_rd_r=1CK36JW4RY26BB5QKG6F&pf_rd_s=center-1&pf_rd_t=15051&pf_rd_i=genre&page={0}&ref_=adv_nxt"
#counter=1
#page="http://www.imdb.com/search/title?genres=horror&explore=title_type,genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=75c37eae-37a7-4027-a7ca-3fd76067dd90&pf_rd_r=1CK36JW4RY26BB5QKG6F&pf_rd_s=center-1&pf_rd_t=15$
counter=1
together={}
#parse_page=urllib2.urlopen(page)
#soup=BeautifulSoup(parse_page,'html.parser')
#found_box=soup.find_all("div",class_="lister-item-content")

for i in range (5):
    url=page.format(counter)
    parse_page=urllib2.urlopen(url)
    soup=BeautifulSoup(parse_page,'html.parser')
    found_box=soup.find_all("div",class_="lister-item-content")
    

    for line in found_box:
        try:
            ratio=line.div.strong.text
        except:
            ratio=None  
        name=line.a.text
        together[name]=ratio
        if ratio>7.0:
           print str(name) + "  " + str(ratio)
    counter=counter+1  
  #except:
#          print "this field not found"
#with open("file_1.txt","w") as _file:
#    _file.write(str(together))
#print(together)
  
#    print ratio
#name_box=soup.find_all('h3',attrs={'class':'lister-item-header'})

#for name in name_box:
    #import pdb; pdb.set_trace() 
 #   name_new=name.a.text
#    print name_new
#   index=index_box.text

#name_box=soup.find_all('h3',attrs={'class':'lister-item-header'})
#name=name_box.text

#for name in name_box:
#    print name
#print index
#print name
