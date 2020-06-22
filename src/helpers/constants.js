export const CLIENT_ID = "897DD9C9-F2CDB-CB4226245EC958AF";
export const CLIENT_SECRET = "BBC344BA-28463-6F838E84419B6B81";


export const basicAuth = () => {
    return btoa(CLIENT_ID + ":" + CLIENT_SECRET);
}
