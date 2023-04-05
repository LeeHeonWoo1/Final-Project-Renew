<script>
import {link, push} from 'svelte-spa-router'
import fastapi from "../lib/api"
import Error from '../components/Error.svelte'
import { access_token, username, is_login } from "../lib/store"

let error = {detail:[]}
let login_username = ''
let login_password = ''

function login(event){
    event.preventDefault()
    let url = '/api/user/login'
    let params = {
        username: login_username,
        password: login_password,
    }

    fastapi('login', url, params, (json)=>{
        $access_token = json.access_token
        $username = json.username
        $is_login = true
        push('/')
    }, (json_error) => {
        error = json_error
    })
}

</script>

<div id="login">
    <h1><strong>환영합니다!</strong> 로그인을 진행해주세요.</h1>
    <form method="post">
      <fieldset>
        <Error error={error} />
        <p><input type="text" placeholder="Username" bind:value="{login_username}"></p>
        <p><input type="password" placeholder="Password" bind:value="{login_password}"></p>
        <p><a use:link href="/find-id">아이디 찾기/</a><a use:link href="/change-password">비밀번호 변경</a></p>
        <p><a use:link href="/sign_up">회원이 아니신가요?</a></p>
        <p><input type="submit" value="Login" on:click={login}></p>
      </fieldset>
    </form>
    <p><span class="btn-round">or</span></p>
    <p>
      <a class="facebook-before" use:link href='/'><span class="fontawesome-facebook"></span></a>
      <button class="facebook">Login Using Facbook</button>
    </p>
    <p>
      <a class="twitter-before" use:link href='/'><span class="fontawesome-twitter"></span></a>
      <button class="twitter">Login Using Twitter</button>
    </p>
</div>

<style>
    @import './css/login.css';
</style>