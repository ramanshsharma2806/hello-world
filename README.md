# Hello World

Hi, so I saw a challenge in the now very popular Noob coder group founded by youtuber [Samuel Miller](https://www.youtube.com/c/SamMillerVlogs).

The challenge is quite simple - make the funniest way you can write a hello world program.

I don't know about funny, but this is sure to be one of the most overkill ways to write a hello world program.

## Methodology

Ever heard of the amazing way to make API's in Python - [Flask](https://flask.palletsprojects.com/en/1.1.x/).

I made two API's in Flask, one in the root directory of the server (no idea if this is what you call the ```route('/')```) and one to get a hello world response back.

You can see the API implementation in the [```API/```](https://github.com/ramanshsharma2806/hello-world/tree/main/API) folder.

The Flask API's were then hosted on a Heroku container and made live here - [hello-worldapi.herokuapp.com/](https://hello-worldapi.herokuapp.com/)

When the website is opened, the ```route('/')``` response can be seen.

Then an [```example.py```](https://github.com/ramanshsharma2806/hello-world/blob/main/example.py) was made where the API's would be called using a Python class system with as much complexity injected as can be done in an hour.


```python
>> python example.py

```
