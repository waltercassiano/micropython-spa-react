# Micropython - SPA React
IOT - Esp32 Micropython using a SPA - React
This project use [create-react-app - CRA](https://github.com/facebook/create-react-app)

# Requirements
- Nodes v10
- Yarn
- Python3
- [Micropyton](http://docs.micropython.org/en/latest/esp32/quickref.html)
- [Micropy cli](https://pypi.org/project/micropy-cli/)
- [Vscode Extension](https://marketplace.visualstudio.com/items?itemName=pycom.Pymakr)

# Project Structure
Folders:

- backend -> here are boot.py and main.py. This is the sync_folder to esp32.
- build -> production version, copied to backend folder when react build
- src -> Frontend React Application

# Commands
#### Command available on root to react:

- yarn install - Install npm dependencies
- yarn start - Start devlopment web server REACT
- yarn build - Build production version

#### Command to Micropy

Should use the Vscode Extension.
Before each upload you need build frontend.

### Frontend Live Reload
- Change to true CORS_ENABLED in main.py
-

### TODO

- Frontend Project
- API Endpoints
- Store config on board
- Build and Upload Application