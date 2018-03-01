# Dungeons and Dragons name generator
The name is pretty self explanatory, I guess. This is a project for generating new
dungeons and dragons character names. I decided that a fun way to do this was to 
use an LSTM char-rnn and train it on data from [this site](http://www.dnd.kismetrose.com/).
Don't use keras as much as tensorflow, so writing this was made a lot easier when having
[this project](https://github.com/ekzhang/char-rnn-keras) as a reference. 

## Installation
Things you'll need <br />
- Python (should work on any version >=2.7 .... hopefully)
<br />
To install run `pip install -r requirements.txt` or `pip3 install -r requirements.txt`

## How to use
In order to run, simply call `python generate.py` <br />
The generator comes with a few extra arguments in order to specify certain constraints you put on generation.<br />
With this generator you can specify three things:
- `--seed` is the starting character(s) you'd like the generator to use when making a name. If you leave this empty, the generator will choose a random capital letter to start every name it generates.
- `--numnames` is the number of names you'd like to generate, if you want to generate a batch.
- `--maxlen` this is the constraint on maximum length of a name. I find it's better not to touch this, but included it as an option anyways.
<br />
Here's one more example for using all of the above arguments: `python generate.py --seed J --numnames 10 --maxlen 10` <br />
This sample will make 10 names starting with the letter J and will cut them off at a max of 10 characters long

### Disclaimer
Not all names are guaranteed to be unique at the moment, sorry.
