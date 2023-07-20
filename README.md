## Hack GPT Dev Repo

### App Structure
```
.
├── app
│   ├── api             // Middleware
│   ├── backend         // Python backend (Where we run models) 
│   ├── client          // React Frontend (Where we hanle modle I/O)
│   ├── manage.py       // Script to run server
│   ├── media           // Images 
│   └── static          // Static Files like .html and .css
├── env                 // Virtual Environment
├── README.md           // This file
└── requirements.txt    // Python dependencies

11 directories, 5 files=
```
### Installation

Clone repo
`git clone git@github.com:JustinMeimar/hack-gpt-dev.git`

Navigate into repo
`cd hack-gpt-dev`

Make a virtual environment
`python -m venv env` 

Install dependencies
`pip install -r requirements.txt`

Run the server locally
`cd app && python manage.py runserver`