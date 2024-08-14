Python 3.12.4 (v3.12.4:8e8a4baf65, Jun  6 2024, 17:33:18) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=10
>>> asd
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    asd
NameError: name 'asd' is not defined
>>> vek = 20
>>> vek
20
>>> MAX_RYCHLOST = 130
>>> MAX_RYCHLOST
130
>>> moje_mesto = 'Praha'
>>> vaha = 50.6
>>> je_streda = True
>>> type(moje_mesto)
<class 'str'>
>>> type(je_streda)
<class 'bool'>
>>> type(vaha)
<class 'float'>
>>> a = '10'
>>> int(a)
10
>>> a
'10'
>>> float(a)
10.0
>>> jmeno = 'Dima'
>>> prijmeni = 'Yablunovskiy
SyntaxError: unterminated string literal (detected at line 1)
>>> prijmeni = 'Yablunovskiy'
>>> mesto = 'Praha'
>>> cely_text = jmeno + prijmeni + mesto
>>> cely_text
'DimaYablunovskiyPraha'
>>> cely_text = '%s %s %s' % (jmeno, prijmeni, mesto)
>>> print(cely_text)
Dima Yablunovskiy Praha
>>> cely_text = f'shsiuhg;ahg; {jmeno} {prijmeni}'
>>> cely_text
'shsiuhg;ahg; Dima Yablunovskiy'
>>> #auhl;sh;v;vix
>>> # askjfg;sg;sgjshglslg
>>> # comment
