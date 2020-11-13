# Chat-bot
**before staring main.py file you should've have some pre-installed tools**

Commands for installing python and pip are:
> sudo apt-get install python3

> sudo apt-get install python3-pip


Tools that we need for this project:
> pip3 install nltk

> pip3 install numpy

> pip3 install tflearn

> pip3 install tensorflow

If you are starting it for the first time or want to rerun the training process, you should put x in try block as shown below:
```
try:
    x
    model.load("model.tflearn")
except:
    model.fit(training, output, n_epoch=1000, batch_size=8, show_metric=True)
    model.save("model.tflearn")
```
then you can remove x once model is trained.

cammand for running the file in terminal:
> python main.py
