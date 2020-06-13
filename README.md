#### Description:
  **Just a basic Python(Flask) application. Was curious and practising  using Flask during the quarantine**

## Set up and installation 
  **Prerequisite**
  - Python3.6 or higher version
  - Modern web browser
  **Installation Guide**
  To run this application, navigate to the command-prompt on windows pc or terminal on linuix nad run this commands:
  - `git clone https://github.com/lamechy/Watchlist.git`
  - `cd watchlist`
  *Create a virtual environment(named  virtual) inside the watchlist directory*
  - `python3.6 -m venv --without-pip virtual`
  *Activate the virtual environment inside the watchlist directory*
  - `source virtual/bin/activate`
  *Install the latest pip version*
  - `curl https://bootstrap.pypa.io/get-pip.py | python3`
  *Inside our virtual environment, install flask using pip*
  - `pip3 install flask`

  At this point, you're good run the application.
   ## Running the application
   To serve this application, run the below command 
  - `python3.6 run.py`
  *The application will serve at http://127.0.0.1:5000/ on your browser with an already URL NOT FOUND error. Don't worry, edit the URL address to  http://127.0.0.1:5000/movie/1234 and it will surely work upon reloading*