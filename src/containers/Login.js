import React, { Component } from "react";
import TextField from '@material-ui/core/TextField'
import "./Login.css"
import { Paper, Grid, Button, Switch, Box } from "@material-ui/core";
import axios from "axios";
import { CLIENT_ID, basicAuth } from "../helpers/constants";

export default class Login extends Component {

    constructor(props) {
        super(props);
        this.state = {
            username: '',
            pwd: '',
            keepLogged: false
        }
    }

    handleKeepLogin = (event) => {
        this.setState({
            keepLogged: event.target.checked
        });
    }

    handleDoLogin = () => {

        axios({
            method: 'get',
            url: '/api/access-token',
            headers: {
                clientId: CLIENT_ID,
                Authorization: basicAuth(),
                username: this.state.username,
                pwd: this.state.pwd
            }
        })
        .then((e) => console.log(e))
        .catch((e) => console.log(e))
    }

    handleInputChange = (inputName, event) => {
        this.setState({
            [inputName]: event.target.value
        });
    }

    isButtonEnabled = ({username, pwd}) => {
        console.log(username, pwd)
        if ((!username || !pwd) || (username.length === 0 || pwd.length === 0)) {
            return true;
        }

        return false;
    }


    render() {
        return (

            <Grid item xs={11}>
                <Paper>
                    <Box p={2}>
                        <Grid item xs={12}>
                            <TextField
                                id="name"
                                label="Username"
                                fullWidth={true}
                                value={this.state.username}
                                onChange={this.handleInputChange.bind(this, "username")}
                                required
                            />
                        </Grid>
                        <Grid item xs={12}>
                            <TextField
                                id="pwd"
                                label="Password"
                                type="password"
                                autoComplete="current-password"
                                fullWidth={true}
                                value={this.state.pwd}
                                onChange={this.handleInputChange.bind(this, "pwd")}
                                required
                            />
                        </Grid>
                        <Grid item xs={12}>
                            <Grid container>
                                <Grid item xs={12}>
                                    <Switch
                                        value={this.state.keepLogged}
                                        checked={this.state.keepLogged}
                                        label="Keep login?"
                                        onChange={this.handleKeepLogin}

                                    />
                                </Grid>
                                <Grid item xs={12}>
                                    <Button disabled={this.isButtonEnabled(this.state)} fullWidth={true} size="large" variant="contained" color="primary" onClick={this.handleDoLogin}>
                                        Login
                                    </Button>
                                </Grid>
                            </Grid>
                        </Grid>
                    </Box>
                </Paper>
            </Grid>

        );
    }
}

