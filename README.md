# Do you speak London?

Command line tool for naturla language identification, also known as langID. Currently supporting 4 languages only, English, Spanish, Portuguese and Arabic:

`$ python dysl.py WRITE SOME TEXT HERE TO BE CLASSIFIED`

And for more options, and help message

`$ python dysl.py --help`

## Use in Code

You can also use dysl's LangID within your code

```python
from dysl.langid import LangID

l = LangID()
l.train()

text = u'hello, world'

lang = l.classify(text)
print text, 'Language:', lang
```

# Contacts
 
+ Name: [Tarek Amr](http://tarekamr.appspot.com/)
+ Twitter: [@gr33ndata](https://twitter.com/gr33ndata)
