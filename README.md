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

In brief, if you want to classify Valyrian and Klingon for example, your corpus should look somehow as follows:

`/user/me/corpus/domain/klingon/file01.txt`
`/user/me/corpus/domain/klingon/file02.txt` 

`/user/me/corpus/domain/valyrian/ex12.xml`
`/user/me/corpus/domain/valyrian/ex13.xml`

As you can see, domain and filename can be anything, just the folders containing the example files should be named after the languages you want to classify. 

Finally, you need to specify the path to the training example in your code.

```python
from dysl.langid import LangID

l = LangID()
l.train(root='/user/me/corpus')

text = u'hello, world'

lang = l.classify(text)
print text, 'Language:', lang
```
## Adding New Samples to Your Training Data

You can add new training samples to your custom training-set. 
You do that on two stages.

To add a new text sample:
`l.add_training_sample(text=u'tlhIngan Hol Dajatlha?', lang='Klingon')
`l.add_training_sample(text=u'jIyajbe', lang='Klingon')

Then to save changes to disk:
`l.save_training_samples()`

Notice that this only works when using custom training-set, 
adding samples to builtin training-set is not permitted.

## Unknown Languages (_Experimantal_)

By default, we try to classify a given text as one of the languages dysl is trained on. However, by setting `unk=True` we allow dysl to return 'unk' when the given text is not in any of the languages it has seen before. 

`l = LangID(unk=True)` 

***

# Contacts
 
+ Name: [Tarek Amr](http://tarekamr.appspot.com/)
+ Twitter: [@gr33ndata](https://twitter.com/gr33ndata)
