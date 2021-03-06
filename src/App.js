import React, { Fragment, Component } from 'react';
import './App.css';
import AppBar from '@material-ui/core/AppBar'
import Toolbar from '@material-ui/core/Toolbar'
import Typography from '@material-ui/core/Typography'
import { Route } from "react-router-dom";
import Login from './containers/Login/Login';
import Grid from '@material-ui/core/Grid'
import IconButton from '@material-ui/core/IconButton';
import MenuIcon from '@material-ui/icons/Menu';
import Home from './containers/Home/Home';

class App extends Component {

  isMenuActived = () => {
    if (!this.props.logged) {
      return;
    }


    return (
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
    )
  }

  render() {
    return (
      <Fragment>
        {this.isMenuActived()}

        <Grid
          container
          spacing={0}
          justify="center"
          alignItems="center"
          className="root-grid"

        >

              <Route path="/" exact component={Login} />
              <Route path="/home" component={Home} />

        </Grid>
      </Fragment>
    );
  }

}

export default App;
