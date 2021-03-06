import axios from "axios";
import { CONFIG } from "../config";

export const Interceptor = ({ storage }) => {
    axios.interceptors.request.use(async (config) => {

        if (!config.url.endsWith(CONFIG.RESOURCE.CONFIG_WIFI)) {
            return config;
        }
        const accessToken = storage.getItem("access_token");
        config.headers.access_token = accessToken;
        return config
    }, (error) => {
        // I cand handle a request with errors here
        return Promise.reject(error);
    });

    return null
}

