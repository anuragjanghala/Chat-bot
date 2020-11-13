# Chat-bot
**Before starting main.py file you should install some tools**

Commands for installing python and pip are:
> sudo apt-get install python3

> sudo apt-get install python3-pip


Tools that we need for this project:
> pip3 install nltk

> pip3 install numpy

> pip3 install tflearn

> pip3 install tensorflow

If you are starting it for the first time or want to re-run the training process, you should put x in try block as shown below:
```
try:
    x
    model.load("model.tflearn")
except:
    model.fit(training, output, n_epoch=1000, batch_size=8, show_metric=True)
    model.save("model.tflearn")
```
then you can remove x once model is trained.

for running the file in terminal:
> python3 main.py

then in terminal it will look like this:
```
start talking with the bot (type quit to stop)!
You: hello
Hi there, how can I help?
You: whats your age
22 years young!
You: whats your name
You can call me django.
You: im here to buy something
I didn't get that, try again
You: buy something
I didn't get that, try again
You: whats on menu
I didn't get that, try again
You: whats on the menu
u should buy some books to read
You: quit
```
