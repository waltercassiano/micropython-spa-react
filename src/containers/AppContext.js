import React, { Component } from "react";
import { withRouter } from "react-router-dom";

export const AppContextProvider = React.createContext();

class AppContext extends Component {

    state = {
        isLogged: false,
        access_token: null
    }
    componentDidMount() {
        this.hasLogged()
    }
    setItem = (key, item) => {
        localStorage.setItem(key, item)
    }

    getItem = (key) => {
        return localStorage.getItem(key);
    }

    updateState = (name, value, saveToStorage) => {
        if (saveToStorage) {
            this.setItem(name, value)
        }

        this.setState({
            [name]: value
        })
    }

    hasLogged() {
        if ( this.getItem("access_token")) {
            this.updateState("isLogged", true);
            this.props.history.push("/home")
        }
    }

    render() {
        return (
            <AppContextProvider.Provider
                value={{
                    storeState: this.state,
                    storeAction: this.updateState,
                    history: this.props.history,
                    storage: {
                        setItem: this.setItem,
                        getItem: this.getItem
                    }
                }}>
                {this.props.children}
            </AppContextProvider.Provider>
        )
    }
}

export default withRouter(AppContext);