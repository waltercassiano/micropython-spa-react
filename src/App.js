import React, { Fragment } from 'react';
import './App.css';
import AppBar from '@material-ui/core/AppBar'
import Toolbar from '@material-ui/core/Toolbar'
import Typography from '@material-ui/core/Typography'
import { Switch, Route, BrowserRouter as Router } from "react-router-dom";
import Login from './containers/Login';
import Grid from '@material-ui/core/Grid'
import IconButton from '@material-ui/core/IconButton';
import MenuIcon from '@material-ui/icons/Menu';


function App() {
  return (
    <Fragment>
      <AppBar position="fixed" color="primary">
        <Toolbar>
          <IconButton edge="start" color="inherit" aria-label="menu">
            <MenuIcon />
          </IconButton>
          <Typography variant="h6">
            IOT ESP32 | ESP8266
         </Typography>
        </Toolbar>
      </AppBar>

      <Grid
        container
        spacing={0}
        justify="center"
        alignItems="center"
        className="root-grid"

      >
        <Router>
          <Switch>
            <Route path="/">
              <Login />
            </Route>
          </Switch>
        </Router>
      </Grid>
    </Fragment>
  );
}

export default App;
