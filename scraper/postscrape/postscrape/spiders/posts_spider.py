import scrapy
from scrapy.crawler import CrawlerProcess
import urllib.request as urllib2
import json
import urllib 

import re
import urllib.parse



class PostsSpider(scrapy.Spider) :
    name = "sagas"
    '''
    Geri þetta síðar
    word = input()
    urltest = 'https://bin.arnastofnun.is/api/beygingarmynd/' + urllib.parse.quote_plus(word)
    print(urltest)
    binJson = json.load(urllib2.urlopen(urltest))
    #print(binJson[0]['bmyndir'])
    declList = set({})
    declList.add(word)
    if len(binJson) > 0:
        for match in binJson:
            guid = str(match.get('guid'))
            singleMatch = json.load(urllib2.urlopen('https://bin.arnastofnun.is/api/ord/%s' %guid))
            bmyndir = singleMatch[0].get('bmyndir')
            if len(bmyndir) > 0:
                for decl in bmyndir:
                    declList.add(decl['b'])
    print(declList)
    '''

    returnList = []

    start_urls = [
        "https://www.snerpa.is/net/isl/band.htm", 
        "https://www.snerpa.is/net/isl/b-snae.htm", 
        "https://www.snerpa.is/net/isl/bjarnar.htm", 
        "https://www.snerpa.is/net/isl/njala.htm", 
        "https://www.snerpa.is/net/isl/droplaug.htm", 
        "https://www.snerpa.is/net/isl/egils.htm", 
        "https://www.snerpa.is/net/isl/eirik.htm", 
        "https://www.snerpa.is/net/isl/eyrbygg.htm", 
        "https://www.snerpa.is/net/isl/finnboga.htm", 
        "https://www.snerpa.is/net/isl/fljotsd.htm", 
        "https://www.snerpa.is/net/isl/floam.htm", 
        "https://www.snerpa.is/net/isl/fostb.htm", 
        "https://www.snerpa.is/net/isl/fsaga.htm", 
        "https://www.snerpa.is/net/isl/grettir.htm", 
        "https://www.snerpa.is/net/isl/gisl.htm", 
        "https://www.snerpa.is/net/isl/graens.htm", 
        "https://www.snerpa.is/net/isl/graent.htm", 
        "https://www.snerpa.is/net/isl/gull.htm", 
        "https://www.snerpa.is/net/isl/gunnars.htm", 
        "https://www.snerpa.is/net/isl/gunnl.htm", 
        "https://www.snerpa.is/net/isl/hallf.htm", 
        "https://www.snerpa.is/net/isl/hallfr2.htm", 
        "https://www.snerpa.is/net/isl/hardar.htm", 
        "https://www.snerpa.is/net/isl/havardar.htm", 
        "https://www.snerpa.is/net/isl/heidarv.htm", 
        "https://www.snerpa.is/net/isl/hrafn.htm", 
        "https://www.snerpa.is/net/isl/hrana.htm", 
        "https://www.snerpa.is/net/isl/haensna.htm", 
        "https://www.snerpa.is/net/isl/kjalnes.htm", 
        "https://www.snerpa.is/net/isl/kormaks.htm", 
        "https://www.snerpa.is/net/isl/krokaref.htm", 
        "https://www.snerpa.is/net/isl/laxdal.htm", 
        "https://www.snerpa.is/net/isl/ljosvetn.htm", 
        "https://www.snerpa.is/net/isl/vigaskut.htm", 
        "https://www.snerpa.is/net/isl/svarfd.htm", 
        "https://www.snerpa.is/net/isl/valla.htm", 
        "https://www.snerpa.is/net/isl/vatnsdae.htm", 
        "https://www.snerpa.is/net/isl/vigaglum.htm", 
        "https://www.snerpa.is/net/isl/viglund.htm", 
        "https://www.snerpa.is/net/isl/vopn.htm", 
        "https://www.snerpa.is/net/isl/thors-hv.htm", 
        "https://www.snerpa.is/net/isl/thorst-s.htm", 
        "https://www.snerpa.is/net/isl/hredu.htm",
        "https://www.snerpa.is/net/snorri/gylf.htm",
        "https://www.snerpa.is/net/snorri/landnama.htm",
        "https://www.snerpa.is/net/forn/jomsvik.htm",
        "https://www.snerpa.is/net/forn/uppl.htm", "https://www.snerpa.is/net/forn/ans.htm", "https://www.snerpa.is/net/forn/asmund.htm", "https://www.snerpa.is/net/forn/bosa.htm", "https://www.snerpa.is/net/forn/asberser.htm", "https://www.snerpa.is/net/forn/fornjot.htm", "https://www.snerpa.is/net/forn/fridpjof.htm", "https://www.snerpa.is/net/forn/gautrek.htm", "https://www.snerpa.is/net/forn/grim.htm", "https://www.snerpa.is/net/forn/gonguhr.htm", "https://www.snerpa.is/net/forn/halfd-br.htm", "https://www.snerpa.is/net/forn/half-e.htm", "https://www.snerpa.is/net/forn/halfs.htm", "https://www.snerpa.is/net/forn/helga-th.htm", "https://www.snerpa.is/net/forn/hervar.htm", "https://www.snerpa.is/net/forn/hjalm-ol.htm", "https://www.snerpa.is/net/forn/hr-gaut.htm", "https://www.snerpa.is/net/forn/hrolf.htm", "https://www.snerpa.is/net/forn/hrom.htm", "https://www.snerpa.is/net/forn/illuga.htm", "https://www.snerpa.is/net/forn/ketill-h.htm", "https://www.snerpa.is/net/forn/nornages.htm", "https://www.snerpa.is/net/forn/ragnar.htm", "https://www.snerpa.is/net/forn/sturlaug.htm", "https://www.snerpa.is/net/forn/sogubrot.htm", "https://www.snerpa.is/net/forn/sor-st.htm", "https://www.snerpa.is/net/forn/sorla.htm", "https://www.snerpa.is/net/forn/toka.htm", "https://www.snerpa.is/net/forn/volsung.htm", "https://www.snerpa.is/net/forn/yngvar.htm", "https://www.snerpa.is/net/forn/rag-son.htm", "https://www.snerpa.is/net/forn/thorstei.htm", "https://www.snerpa.is/net/forn/th-bmagn.htm", "https://www.snerpa.is/net/forn/orvar.htm",
        "https://www.snerpa.is/net/snorri/prolog.htm", "https://www.snerpa.is/net/snorri/yngl-sag.htm", "https://www.snerpa.is/net/snorri/halfd-sv.htm", "https://www.snerpa.is/net/snorri/har-har.htm", "https://www.snerpa.is/net/snorri/hakon-g.htm", "https://www.snerpa.is/net/snorri/h-grafel.htm", "https://www.snerpa.is/net/snorri/ol-tr.htm", "https://www.snerpa.is/net/snorri/ol-helg.htm", "https://www.snerpa.is/net/snorri/magnus-g.htm", "https://www.snerpa.is/net/snorri/har-sig.htm", "https://www.snerpa.is/net/snorri/okyrra.htm", "https://www.snerpa.is/net/snorri/mag-berf.htm", "https://www.snerpa.is/net/snorri/msonsaga.htm", "https://www.snerpa.is/net/snorri/m-blind.htm", "https://www.snerpa.is/net/snorri/ingi-k.htm", "https://www.snerpa.is/net/snorri/herdibr.htm", "https://www.snerpa.is/net/snorri/m-erl.htm",
        "https://www.snerpa.is/net/isl/arnor.htm", "https://www.snerpa.is/net/isl/audun.htm", "https://www.snerpa.is/net/isl/bergb.htm", "https://www.snerpa.is/net/isl/laxdal.htm#bolli", "https://www.snerpa.is/net/isl/brandk.htm", "https://www.snerpa.is/net/isl/brands.htm", "https://www.snerpa.is/net/isl/draum.htm", "https://www.snerpa.is/net/isl/egils-th.htm", "https://www.snerpa.is/net/isl/einar-th.htm", "https://www.snerpa.is/net/isl/gisl-th.htm", "https://www.snerpa.is/net/isl/gisl-th2.htm", "https://www.snerpa.is/net/isl/gisl-th3.htm", "https://www.snerpa.is/net/isl/gull-as.htm", "https://www.snerpa.is/net/isl/g-asa2.htm", "https://www.snerpa.is/net/isl/gun-tidr.htm", "https://www.snerpa.is/net/isl/halld-s1.htm", "https://www.snerpa.is/net/isl/halld-s2.htm", "https://www.snerpa.is/net/isl/hrafn-g.htm", "https://www.snerpa.is/net/isl/hreidar.htm", "https://www.snerpa.is/net/isl/hromund.htm", "https://www.snerpa.is/net/isl/th-islen.htm", "https://www.snerpa.is/net/isl/th-ivar.htm", "https://www.snerpa.is/net/isl/th-kumlb.htm", "https://www.snerpa.is/net/isl/th-mana.htm", "https://www.snerpa.is/net/isl/th-odds.htm", "https://www.snerpa.is/net/isl/th-orms.htm", "https://www.snerpa.is/net/isl/ljosvetn.htm#ofeigs", "https://www.snerpa.is/net/isl/ottsv-be.htm", "https://www.snerpa.is/net/isl/ottsv-ba.htm", "https://www.snerpa.is/net/isl/ottsv-fl.htm", "https://www.snerpa.is/net/isl/ottsv-to.htm", "https://www.snerpa.is/net/isl/snegl-fl.htm", "https://www.snerpa.is/net/isl/snegl-mo.htm", "https://www.snerpa.is/net/isl/st-oddi.htm", "https://www.snerpa.is/net/isl/stufs-me.htm", "https://www.snerpa.is/net/isl/stufs-sk.htm", "https://www.snerpa.is/net/isl/svada.htm", "https://www.snerpa.is/net/isl/ljosvetn.htm#sorli", "https://www.snerpa.is/net/isl/ljosvetn.htm#vodu", "https://www.snerpa.is/net/isl/thidrand.htm", "https://www.snerpa.is/net/isl/th-halla.htm", "https://www.snerpa.is/net/isl/th-jarl.htm", "https://www.snerpa.is/net/isl/thorm-fl.htm", "https://www.snerpa.is/net/isl/thorm-fo.htm", "https://www.snerpa.is/net/isl/th-aust.htm", "https://www.snerpa.is/net/isl/th-forvi.htm", "https://www.snerpa.is/net/isl/siduh-fl.htm", "https://www.snerpa.is/net/isl/siduh-mo.htm", "https://www.snerpa.is/net/isl/skelks.htm", "https://www.snerpa.is/net/isl/stangar.htm", "https://www.snerpa.is/net/isl/sogufr.htm", "https://www.snerpa.is/net/isl/tjaldst.htm", "https://www.snerpa.is/net/isl/uxafots.htm", "https://www.snerpa.is/net/isl/tasaldi.htm", "https://www.snerpa.is/net/isl/th-vidfo.htm", "https://www.snerpa.is/net/isl/krakunef.htm", "https://www.snerpa.is/net/isl/nefjolf.htm", "https://www.snerpa.is/net/isl/th-ofsa.htm", "https://www.snerpa.is/net/isl/th-stutt.htm", "https://www.snerpa.is/net/isl/th-knapp.htm", "https://www.snerpa.is/net/isl/dytts.htm"
    ]
    
    
    
    def parse(self, response) :        
        curChapt = ""
        dic = {}
        title = response.css('h2 b::text').get()
        blockquote = response.css('blockquote')
        for par in blockquote.css('p'):
            b = par.xpath("normalize-space(.//b/text())").get()
            if b is not None and len(b) > 0:
                curChapt = b.rstrip().lstrip()
                dic[curChapt] = []
            else:
                p = par.xpath("normalize-space(.//text())").get()
                if p is not None:
                    dic[curChapt].append(p)
        yield {
            "title": title,
            "chapters": dic
        }

            
        '''
        for post in response.css('div.post-item'):
            yield {
                'title': post.css('.post-header h2 a::text')[0].get(),
                'date': post.css('.post-header a::text')[1].get(),
                'author': post.css('.post-header a::text')[2].get()
            }
        
        
        next_page = response.css('a.next-posts-link::attr(href)').get()
        if next_page is not None:
            print('next_page before ', next_page)
            next_page = response.urljoin(next_page)
            print('next_page after ', next_page)
            yield scrapy.Request(next_page, callback = self.parse)
        '''
     
'''
Kann ekki að láta process gera output
process = CrawlerProcess()
#process.crawl(AnotherSpider)
process.crawl(PostsSpider)
process.start()
'''

