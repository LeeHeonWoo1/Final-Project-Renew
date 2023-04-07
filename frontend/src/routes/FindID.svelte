<script>
    import Error from '../components/Error.svelte'
    import {link} from 'svelte-spa-router'
    import fastapi from '../lib/api';
    
    let error = {detail:[]}
    let db_name = ''
    let db_email = ''

    function getEmail(event){
        event.preventDefault()
    
        fastapi('post', '/api/user/user-email', {name:db_name, email:db_email}, (json)=>{
            alert(`${db_email}로 아이디를 전송했습니다.`)
        }, (json_error)=>{
            error = json_error
        })
    }
</script>
        
<div id="login">
    <h1><strong>ID찾기</strong></h1>
    <h6>가입한 이름과 이메일을 입력해주세요.</h6>
    <Error error={error} />
    <form method="post">
        <fieldset>
        <p><input type="text" placeholder="이름" bind:value="{db_name}"></p>
        <p><input type="text" placeholder="이메일" bind:value="{db_email}"></p>
        <p><a use:link href="/user-login">로그인 화면으로</a></p>
        <p><input type="submit" value="조회하기" on:click={getEmail}></p>
        </fieldset>
    </form>
</div>
    
    <style>
        @import './css/login.css';
    </style>