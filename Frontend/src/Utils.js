
export function getParam(param){
    var tmp;
    var items = window.location.search.substr(1).split('&');
    for (var i = 0; i < items.length; i++){
        tmp = items[i].split("=");
        if (tmp[0] === param) {
        return decodeURIComponent(tmp[1]);
      }
    }
}

export function handleErrors(response){
    if (!response){
        throw Error("Response object is null");
    }

    if (!response.ok) {
        throw Error(response.statusText);
    }

    return response;
}