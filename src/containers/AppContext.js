import React, { Component } from "react";

export const AppContextProvider = React.createContext();

class AppContext extends Component {

    state = {
        isLogged: false
    }

    render() {
        return (
            <AppContextProvider.Provider value={this.state} >
                {this.props.children}
            </AppContextProvider.Provider>
        )
    }
}

export default AppContext;