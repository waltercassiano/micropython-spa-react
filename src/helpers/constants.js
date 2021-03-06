export const basicAuth = (key, value) => {
    return btoa(key + ":" + value);
}