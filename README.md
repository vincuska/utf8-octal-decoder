
# UTF-8 and UTF-8 to octal decoder

Have a file that is loaded with stuff like this?

```css
\57\x6d\141\151\x6e\57\x69\156\143\x6c\165\x64\x65\163\57\x70\x68\x70\57\141\160\x70\56\160\150\x70
```

Well I got you covered! 
This amazing tool not only decodes utf-8 but utf-8 in octal form!!!


## Features

 So if there's any wierd stuff like this:
+ `\x63\x6F\x6F\x6C`
+ `\143\157\157\154`
+ `\x63\x6F\157\154`
+ `\143\157\x6F\x6C`

#### It will output the word 'cool' 4 times!

And hey you maybe you are confused and thinking that "Where do I even find this stuff it's now even usefull... etc."

**Let me tell you a story...**

My very good friend of mine was "cracking" a php file and it had a bunch of encoded stuff. You have to pay for a license to decode those. So he of course asked `ME` for help. And that's how I made this tool!
## Run Locally

Clone the project

```batch
  git clone https://github.com/HyDra-55/utf8-octal-decoder
```

Go to the project directory

```batch
  cd utf8-octal-decoder
```

Install dependencies

```batch
  pip install -r requirements.txt
```

Start the program

```batch
  python decoder.py
```

