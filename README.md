# dependencyservice
Serve up SpaCy Dependency Trees

## Install

You will need Python 3.6 (I used the async support) and SpaCy with the English language module.
Requirements are aiohttp and spacy (obviously) and spacy's english language. I'll add a requirements.txt when I can get the English language module included in there (currently because I use "en" in the code you need admin permissions to install it.)

## Run

The service currently runs on port 9001. Try something like:

```
http://localhost:9001/dependency?q=how%20about%20this%20for%20a%20demo
```


