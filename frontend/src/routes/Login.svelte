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
    <h1><strong>Welcome.</strong> Please login.</h1>
    <form action="#" method="post">
      <fieldset>
        <Error error={error} />
        <p><input type="text" placeholder="Username" bind:value="{login_username}"></p>
        <p><input type="password" placeholder="Password" bind:value="{login_password}"></p>
        <p><a use:link href="/">Forgot Password?</a></p>
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