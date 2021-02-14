html_doc="""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>ilkweb</title>
</head>
<body>
     <h1 id="header">
         hello world hi
     </h1>

     <div class="grup1">
         <h2>
             proglama
         </h2>
         <ul>
             <li>menü1</li>
             <li>menü2</li>
             <li>menü3</li>
         </ul>
     </div>
    <div class="grup2">
        <h2>
            mödüller
        </h2>
        <ul>
            <li>menü1</li>
            <li>menü2</li>
            <li>menü3</li>
        </ul>
    </div>
    <img src="LON OFFLINE.jpg" alt="">
    <a class="sister" href="http://example1.com/elsie" id="link1">Elsie</a>,
    <a class="sister" href="http://example2.com/lacie" id="link2">Lacie</a>,
    <a class="sister" href="http://example3.com/tillie" id="link3">Tillie</a>


</body>
</html>"""

from bs4 import BeautifulSoup
#html parser yazdığımızda uygulayacağımız uygulamayı html koduna uygun yapar
soup=BeautifulSoup(html_doc,"html.parser")
#prettify mödülü html dokümanını düzelterek bize döndürür
result=soup.prettify()
#burda html dökümanın içinde hangi bölümünü almak istediğimizi gireriz

result=soup.head
result=soup.body
#burada etiket içindeki isimi alabilşriz
result=soup.title.name
#burada etiket içindeki ifadeyi verir
result=soup.title.string
#burada ilk h1 yada h2 etiketini getirir
result=soup.h2.string
result=soup.h1.string
#find all mödülü ise tüm h1 etiketini bize getirir
result=soup.find_all("h2")[0]

result=soup.div
#liste gibi istediğimiz etiketlere ulaşabiliyoruz
#adım adım istediğimiz etikete ulaşabiliriz
result=soup.find_all("div")[1].ul.find_all("li")
#div altındaki tüm etiketleri bize veirir yani girdiğimiz etiketin alt elemanlarını alır
result=soup.div.findChildren()
#fingNextSinling mödülü ile şuan bulunduğu etiketin kardeşi olan yani aynı hizada bulunan etikete geçiş yapar
result=soup.div.findNextSinling
#findPreviousSibling mödülü ise şuan bulunduğu etiketten bir önceki kardeşi olan etikete geçiş yapar
result=soup.div.findPreviousSibling()



result=soup.find_all("a")
for i in result:
    print(i.get("href"))
print(result)
