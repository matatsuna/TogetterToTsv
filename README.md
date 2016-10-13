# TogetterToTsv
Togetterからタブ区切りのtsvファイルを生成するpython3系のプログラム

# 開発環境
python3.5を使用

#使用方法
```
>>python3.5 togettertotsv.py {ID}
```
{ID}はtogetterのページの番号
togetter_{ID}.tsvというファイルができます。

(例)
urlがhttp://togetter.com/li/826473 の場合、{ID}は826473となります。
```
>>python3.5 togettertotsv.py 826473
```

# お断り
1ページ目のajaxで取得する部分をすっとばしてますので、26番目のツイートから50番目のツイートまで取得できてません。どなたか、プルリクエストをください....
