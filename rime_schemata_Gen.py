import regex

# process https://github.com/biopolyhedron/rime_schemata

table = """- [rime-arabic](https://github.com/biopolyhedron/rime-arabic)：阿拉伯字母國際鍵盤
- [rime-burmese](https://github.com/biopolyhedron/rime-burmese)：緬甸文
- [rime-devanagari](https://github.com/biopolyhedron/rime-devanagari)：天城體梵文
- [rime-greek](https://github.com/biopolyhedron/rime-greek)：希臘文
- [rime-hebrew](https://github.com/biopolyhedron/rime-hebrew)：希伯來語轉寫輸入
- [rime-jap-poly](https://github.com/biopolyhedron/rime-jap-poly)：poly日文
- [rime-kartuli](https://github.com/biopolyhedron/rime-kartuli)：格魯吉亞字母
- [rime-kyril-international](https://github.com/biopolyhedron/rime-kyril-international)：基利爾字母混合輸入
- [rime-latin-international](https://github.com/biopolyhedron/rime-latin-international)：拉丁字母混合輸入
- [rime-manju](https://github.com/biopolyhedron/rime-manju)：滿語轉寫輸入
- [rime-manju-alikali](https://github.com/biopolyhedron/rime-manju-alikali)：滿語阿禮嘎禮轉寫輸入
- [rime-middle-chinese](https://github.com/biopolyhedron/rime-middle-chinese)：中古漢語（切韻音系）全拼及三拼
- [rime-mongol](https://github.com/biopolyhedron/rime-mongol)：蒙古文
- [rime-qyeyshanglr-hanja](https://github.com/biopolyhedron/rime-qyeyshanglr-hanja)：옛한글・漢字
- [rime-syriac](https://github.com/biopolyhedron/rime-syriac)：敘利亞字母
- [rime-tangut-poly4](https://github.com/biopolyhedron/rime-tangut-poly4)：西夏文【Poly四角】
- [rime-thai-stupid](https://github.com/biopolyhedron/rime-thai-stupid)：泰文（笨）
- [rime-tibetan](https://github.com/biopolyhedron/rime-tibetan)：藏文
- [rime-uyghur](https://github.com/biopolyhedron/rime-uyghur)：維吾爾語
- [rime-zhuyin](https://github.com/biopolyhedron/rime-zhuyin)：漢語注音字母""".split("\n")

formatString='''---
id: {id}
display_name: {name}
url: {url}
url_to_file: /archive/master.zip

provides:
  - {id}:
    type: basic
    display_name: {name}
    files:
      - {id}.schema.yaml
---
'''

for x in table:
    id  = regex.compile('\[(.*?)\]').findall(x)[0][5:]
    url = regex.compile('\((.*?)\)').findall(x)[0]
    name = x.split('：')[1]
    print(id,url,name)
    with open('./'+id+".yaml",'w+') as file:
        file.write(formatString.format(id=id,url=url,name=name))
