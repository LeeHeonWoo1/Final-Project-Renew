import qs from 'qs'

const fastapi = (operation, url, params, success_callback, failure_callback) => {
    let method = operation
    let content_type = 'application/json'
    let body = JSON.stringify(params)

    if(operation === 'login') {
        method = 'post'
        content_type = 'application/x-www-form-urlencoded'
        // OAuth2의 content type은 위에 있는 content_type이다. 원래의 타입에서 OAuth2가 요구하는 방향으로 고쳐주는 qs를 이용해서 body를 수정한다.
        body = qs.stringify(params)
    }

    let _url = import.meta.env.VITE_SERVER_URL + url
    if (method === 'get'){
        _url += '?' + new URLSearchParams(params)
    }

    let options = {
        method: method,
        headers: {
            "Content-Type":content_type
        }
    }

    if (method !== 'get'){
        options['body'] = body
    }

    fetch(_url, options).then(res=>{
        if (res.status === 204){
            if(success_callback){
                success_callback()
            }return
        }

        res.json().then(json=>{

            if (res.status >= 200 && res.status < 300) {
                if (success_callback) {
                    success_callback(json)
                }
            }else{
                if (failure_callback){
                    failure_callback(json)
                }else{
                    alert(JSON.stringify(json))
                }
            }
        }).catch(error => {
            console.log(error)
        })
    })
}

export default fastapi;