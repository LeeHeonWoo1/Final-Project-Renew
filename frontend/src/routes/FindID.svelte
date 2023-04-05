<script>
    import Error from '../components/Error.svelte'
    import {link} from 'svelte-spa-router'
    import fastapi from '../lib/api';
    import { username } from '../lib/store';
    
    let error = {detail:[]}
    let db_username = ''
    let db_email = ''

    function getEmail(event){
        event.preventDefault()
    
        fastapi('post', '/api/user/user-email', {email:db_email}, (json)=>{
            alert('아이디는 ' + json.username + ' 입니다.')
        })
    }
</script>
        
    <div id="login">
        <h1><strong>ID찾기</strong></h1>
        <h2>이메일을 입력해주세요.</h2>
        <Error error={error} />
        <form method="post">
            <fieldset>
            <p><input type="text" placeholder="email" bind:value="{db_email}"></p>
            <p><a use:link href="/user-login">로그인 화면으로</a></p>
            <p><input type="submit" value="조회하기" on:click={getEmail}></p>
            </fieldset>
        </form>
    </div>
    
    <style>
        @import './css/login.css';
    </style>