# Do you speak London?

Command line tool for naturla language identification, also known as langID. Currently supporting 4 languages only, English, Spanish, Portuguese and Arabic:

`$ python dysl.py Can you tell if this is in English?`

You can let dysl read from custom training data with your own set of languages. 

`$ python dysl.py --corpus /PATH/TO/TRAINING/DATA ¿Puede usted decir si esto es en español?`

You also can use the CLI to add more samples to your training data. 

`$ python dysl.py --corpus /PATH/TO/TRAINING/DATA --lang en Here you are some text in English to be add to your training data`

To show the currently installed version:

`$ python dysl.py --version`

For listing of all CLI options:

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

To add a new samples:

`l.add_training_sample(text=u'tlhIngan Hol Dajatlha?', lang='Klingon')`

`l.add_training_sample(text=u'jIyajbe', lang='Klingon')`

Then to save changes to disk:

`l.save_training_samples()`

_Note_: 

By default, a folder name generated from the current timestamp, `/batchTSYYMMDDHHMMSS` is used for the domain, and `file.txt` is used for sample files in language folders. To specify the domain folder name and file name, you can use the following command instead:

`l.save_training_samples(domain='MyDomain', filename='MyFile.txt')`

Notice that saving new sample data only works when using custom training-set, 
adding samples to builtin training-set is not permitted.

# Retrain When Modified

Let's say you are going to build a daemon that calls uses dysl. Normally, you would train dysl when starting then use that data for any further language classifications. 

What if some other process, or human, updates the training dataset during that? How will your daemon know that it neads to retrain again?

Well, in LangID, there is a method, `is_training_modified()`, that can tell you if the training data was modified after it was first trained on it or not:

`l.is_training_modified()`

It returns `True` if the data was modified, and `False` otherwise. Of course, when using the builtin dataset, it will always return `False` as it not allowed to be modified.

## Unknown Languages (_Experimantal_)

By default, we try to classify a given text as one of the languages dysl is trained on. However, by setting `unk=True` we allow dysl to return 'unk' when the given text is not in any of the languages it has seen before. 

`l = LangID(unk=True)` 

***

# Contribution

To contribute to dysl, first create an account on [github](http://github.com/). Once this is done, fork the [dysl repository]
(http://github.com/gr33ndata/dysl) to have you own repository,
clone it using 'git clone' on the computers where you want to work. Make
your changes in your clone, push them to your github account, test them
on several computer, and when you are happy with them, send a pull
request to the main repository.

***

# Contacts
 
+ Project Owner: [Tarek Amr](http://tarekamr.appspot.com/)
 
