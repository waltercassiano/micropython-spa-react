console.log(process.env)
const getBaseUrl = ( ) => {
    if (process.env.REACT_APP_ESP_ENV_LIVE_RELOAD)
        return process.env.REACT_APP_ESP_HOST + "/api"
    return "http://" + window.location.hostname  +":3000/api";
}

export const CONFIG = {
    BASE_URL_API: getBaseUrl(),
    CLIENT_ID : "897DD9C9-F2CDB-CB4226245EC958AF",
    CLIENT_SECRET : "BBC344BA-28463-6F838E84419B6B81",
    RESOURCE: {
        ACCESS_TOKEN: "/access-token",
        CONFIG_WIFI: "/config/wifi"
    }
}
