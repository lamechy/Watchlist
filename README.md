#### Description:
**This is a movie review website build using flask. This web application allows a user to find a movie, add a review to the movie and also add comments to reviews**

Check out the heroku deployed version of this application on this link ---> https://watch-list-01.herokuapp.com/ 
## Set up and installation 
**Prerequisite**
- Python3.6 or higher version
- Modern web browser
 
**Local Installation Guide**
To run this application locally, navigate to the command-prompt on windows pc or terminal in Linux OS and run this commands:

- `git clone -b branch_1 https://github.com/lamechy/Watchlist.git`
- `cd watchlist`

Once inside the `watchlist` directory, now we will have to create a virtual environment for our application by running the following command:
*Creating a virtual environment(named  virtual) inside the watchlist directory*
- `python3.6 -m venv --without-pip virtual`

*Activate the virtual environment inside the watchlist directory (always do this)*
- `source virtual/bin/activate`

Install the latest pip version
- `curl https://bootstrap.pypa.io/get-pip.py | python3`

Inside our virtual environment, install flask using pip
- `pip3 install flask`


## Running the application
To serve this application, run this command: 
- `./start.sh`

The application will serve at http://127.0.0.1:5000/ on your browser. 
Incase of a *moduleNotFound* consider having this installations
`pip install flask-wtf`
`pip install flask-bootstrap`

##  Technologies Used
* Python(Flask)
* JavaScript
* HTML
* CSS

### License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
