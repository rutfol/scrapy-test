import json
import urllib.request as urllib2
import urllib 


db = r'sagas.json'
data = json.loads(open(db).read())

word = input("Sladu inn leitarord (beygingarmyndir koma sjalfkrafa)")
urltest = 'https://bin.arnastofnun.is/api/beygingarmynd/' + urllib.parse.quote_plus(word)
#print(urltest)
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

for saga in data:
    for key in saga['chapters']:
        for paragraph in saga['chapters'][key]:
            for decl in declList:
                if decl in paragraph:
                    print(saga['title'], ", ", key, " ->\n", paragraph)
