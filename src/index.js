import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import AppContext, { AppContextProvider } from "./containers/AppContext";
import { BrowserRouter as Router } from "react-router-dom";
import { Interceptor } from './helpers/Interceptor';
import { createServer } from "miragejs"
createServer({
  routes() {
    this.namespace = "api"
    this.get("/access-token", () =>  ({"access_token": "12222"}))
    this.get("/config/wifi", () =>  ({"access_token": "12222"}))
  }
})

ReactDOM.render(
  <React.StrictMode>
    <Router>
      <AppContext>
        <AppContextProvider.Consumer>
          {({ storeState, storage }) => (
            <React.Fragment>
              <Interceptor storage={storage} />
              <App logged={storeState.isLogged} />
            </React.Fragment>

          )}
        </AppContextProvider.Consumer>
      </AppContext>
    </Router>
  </React.StrictMode >,
  document.getElementById('root')
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
// serviceWorker.unregister();
