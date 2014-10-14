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
## Use your own Training Data

As stated earlier, we currently support English, Spanish, Portuguese and Arabic out of the box, however, this doesn't stop you from using your own data to train dysl. Thus, you can even use it to classify your choice of fictional languages such as George Orwell's Newspeak, Valyrian Languages, and The Klingon language if you have the needed data.

For compatibility with [langid.py](https://github.com/saffsd/langid.py), we require the training data to be in the following format:

> To train a model, we require multiple corpora of monolingual documents. Each document should be a single file, and each file should be in a 2-deep folder hierarchy, with language nested within domain. For example, we may have a number of English files:

`./corpus/domain1/en/File1.txt ./corpus/domainX/en/001-file.xml`

We, however do not rely on domains as they do in langid.py, so you can use a single domain if you want to.

In brief, if you want to classify Valyrian and Klingon for example, your coupus should look somehow as follows:

`./corpus/domain/klingon/file1.txt`
`./corpus/domain/klingon/file2.txt` 
`./corpus/domain/klingon/myfile.xml`
`./corpus/domain/valyrian/file001.txt` 
`./corpus/domain/valyrian/example1.xml`
`./corpus/domain/valyrian/example2.xml`

As you can see, domain and filename can be anything, just the folders containing the example files should be named after the languages you want to classify. 

# Contacts
 
+ Name: [Tarek Amr](http://tarekamr.appspot.com/)
+ Twitter: [@gr33ndata](https://twitter.com/gr33ndata)
