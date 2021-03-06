import axios from "axios";
import { CONFIG } from "../config";
import { basicAuth } from "../helpers/constants";

const restCall = (props) => {
    const { method, url, headers, params, body} = props
    let call = url;

    if (params) {
        call = call + new URLSearchParams(params).toString();
    }

    return axios({
        method,
        url: call,
        headers,
        body
     })
}

const defaultHeaders = {
    clientId: CONFIG.CLIENT_ID,
    Authorization: basicAuth(CONFIG.CLIENT_ID, CONFIG.CLIENT_SECRET)
}

export default class RestApi {

    static get = (props) => restCall({ method: "get", headers: defaultHeaders, ...props });

    static post = (props) => restCall({ method: "post", headers: defaultHeaders, ...props });

    static patch = (props) => restCall({ method: "patch", headers: defaultHeaders, ...props });

    static put = (props) => restCall({ method: "put", headers: defaultHeaders, ...props });
}