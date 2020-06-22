import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import AppContext, { AppContextProvider } from "./containers/AppContext";


ReactDOM.render(
  <React.StrictMode>
    <AppContext>
      <AppContextProvider.Consumer>
        { ( { isLogged }) => <App logged={isLogged} /> }
      </AppContextProvider.Consumer>
    </AppContext>
  </React.StrictMode >,
  document.getElementById('root')
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
// serviceWorker.unregister();
