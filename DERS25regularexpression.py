import re
str="python öğrenmeliyiz saat 24 35 ee "
result=re.findall("[abe]",str)
print(result)
#+köşeli parantez içine yazdığımız bütün karakterleri arar
result=re.findall("[a-z]",str)
print(result)
#köşeli parantez içine a-z yazarsak abcde karakterlerini arar
result=re.findall("[1-5]",str)
#1-6>>>1235
result=re.findall("[^abe]",str)
print(result)
#köşeli parantez içine [^] arayacağıkmız karakterin başına ^koyarsak o karakter dışındakileri bize veirri
#. karakteri herhangi bir basamaklı karakteri temsil eder
#.. nokta iki karakteri gibi
result=re.findall("...",str)
print(result)
result=re.findall("py..on",str)
print(result)
#arayacağımız karakterin başına ^ karakterini koyarsak o karakterle başlayan objeleri bize verir
result=re.findall("^p",str)
print(result)
#arayacağımız karakterin sonuna $ koyarsajk arayacağımız karakterle biten bir elenmanı varmı demiş oluruz
result=re.findall("n$",str)
print(result)
#*karakteri bir karakterin sıfır yada daha fazla sayıda olmasını kontrol eder
"""ma* => mn:1 eşlendi
          man:1 eşlendi
          maan:1 eşlendi
          main:no match (a nı9n arkasından n gelmşyor)"""
result=re.findall("sa*t",str)
print(result)
#sadece bir kere takrar edeni bulmak istediğimizde ? kullanırız
result=re.findall("sa?t",str)
print(result)
"""{} karaktewrin sayısını kontrol eder
    al{2} => a karakterinin arkasına l karakteri 2 kez tekrarlamalı
    al{2,3}=> a karakterinin arkasına l karakteri en az 2 en fazla 3 kez tekrarlamalı
    [0-9]{2,3} => en az 2 en ç9ok 4 basamaklı"""
result=re.findall("e{2}",str)
result=re.findall("[0-9]{2,4}",str)
print(result)
"""| alternatif seçeneklerden birinin gerçekleşmesi gerekir 
            a|b => a yada b
                cde => no match
                ade=> 1 match
                acdbea=> 3 match"""
result=re.findall("a|b",str)
print(result)
"""() gruplamak için kullanılır
          (a|b|c)xz => a,b,c karakterlerinin arkasına xz gelmelidir"""
#---------------------------------------------------
"""\ özel karakterleri aramamızı sağlar
    \$a => $ karakterin arkasına a karakteri arar. yani $ reular exp.ç engine tarafından yorumlamaz
    \A belirtilen karakter stringi in başındamı 
          \Athe => the stringi in başındamı
    \Z belitirilen karakter stringi in sonundamı
          the\Z => the karakteri stringin sonundamı
    \b belirtilen karakter kelimenin in başınb-damı ya da sonundamı (her kelimenin)
           \bthe => the kelimeinin in başındamı
           the\b => the kelimenin sonundamı
    \B belirtilen karakter kelimein in başındamı yada sonunda değilmi 
           \Bthe=> the kelimenin başında değilmi
           the\B=> the kelimenin sonunda değil mi
    \d [0-9] ile aynı anlama gelir yani rakamları arar
           \d=>123dgt56
    \D [^0-9] ile aynı anlma gelir yani rakam olmayanları verir
    
    \s boşluk karakteri ara
    \S boşluk karakteri dışındakileri arar
    \w alfabetik karakterileri,rakamlar ve alt çzigi karakteri
    \W \w tam tersi"""