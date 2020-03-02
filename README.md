# Title

**Chi_Gallery**

## Description 

Chinchillah's Gallery(Chi_Gallery) is a personal gallery application that displays my photos for other people to see just as one of the way of building social intelligence.! You can visit the live site on ''/ 

### Author 

**Anthony Muli**

**mulianthony561@gmail.com**

### Features 

As a user of the web application you will be able to: 
See all posted photos
View photos by location
See each photo’s description and location on hover.
Be able to copy a photo’s url to the clipboard
Click on view image to expand a photo
Search for a photo by category e.g. outdoor, photoshoot 

### Specifications 
| Behavior | Input | Output | 
| -------- | ----- | ------ |
| View all posted photos | Hover over a photo | Shown details about the photo 
| Details about the photo | Click on Copy Link | Pop up that shows that the image link has been copied appears | 
| Details about the photo | Click on View Image | Photo expands | 
| Search in the search field | Input keywords to be searched then press ENTER | Search page is loaded and displays with the searched results | 

#### Getting started 
Prerequisites 
python3.6
virtual environment
pip 
Cloning 
In your terminal: 
$ git clone https://github.com/antomuli/Chi_Gallery.git
$ cd Chi_Gallery

#### Running the Application 

Install virtual environment using $ python3.6 -m venv virtual
Activate virtual environment using $ source virtual/bin/activate
Download pip in our environment using $ curl https://bootstrap.pypa.io/get-pip.py | python
Install all the dependencies from the requirements.txt file by running python3.6 pip install -r requirements.txt
Create a database and edit the database configurations in settings.py to your own credentials.
Make migrations 
$ python manage.py makemigrations photos
$ python3.6 manage.py migrate 
 To run the application, in your terminal: 
$ python3.6 manage.py runserver

#### Testing the Application 

To run the tests for the class file: 
$ python3.6 manage.py test photos

#### CODEBEAT

[![codebeat badge](https://codebeat.co/badges/8dd34843-e158-4631-b105-fcffde89d879)](https://codebeat.co/projects/github-com-antomuli-chi_gallery-master)

###### Technologies Used 
Python3.6Chinchillah's Gallery(Chi_Gallery) is a personal gallery application that displays my photos for other people to see just as one of the way of building social intelligence.! You can visit the live site on **'https://whispering-temple-04935.herokuapp.com'** 

Django
HTML
Bootstrap 
This application is developed using Python3.6, Django, HTML and Bootstrap 

###### Support and Team 
Anthony Muli
Slack Me! @Anthony Muli 

###### LICENSE AND COPY RIGHT INFO.
MIT License

Copyright (c) 2020 Chi_Gallery-Anthony

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), 
to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, 
and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, 
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

