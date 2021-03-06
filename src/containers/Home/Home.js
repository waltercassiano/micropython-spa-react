import React, { Component } from "react";
import { Grid } from "@material-ui/core";
import { AppContextProvider } from "../AppContext";
import axios from "axios";
import { CONFIG } from "../../config";

class Home extends Component {

    constructor(props) {
        super(props);
        this.state = {

        }


        axios({
            method: 'get',
            url: CONFIG.BASE_URL_API + CONFIG.RESOURCE.CONFIG_WIFI,
            headers: {
                clientId: CONFIG.CLIENT_ID
            }
        })
        .then((e) => console.log(e))
        .catch((e) => console.log(e))

    }
    render() {
        return (
            <Grid item xs={11}>
                HOME
            </Grid>
        );
    }
}

export default function () {
    return <AppContextProvider.Consumer>
        {({ storeAction }) => <Home updateContext={storeAction} />}
    </AppContextProvider.Consumer>
}