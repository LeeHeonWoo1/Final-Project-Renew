<script>
import Error from '../components/Error.svelte'
import {push} from 'svelte-spa-router'
import fastapi from '../lib/api';
import { username } from '../lib/store';

let error = {detail:[]}
let change_username = ''
let change_email = ''
let change_password1 = ''
let change_password2 = ''

function ChangePassword(event){
    event.preventDefault()
    
    let url = '/api/user/change-password'
    let params = {
        username: change_username,
        email: change_email,
        password1:change_password1,
        password2:change_password2
    }
    
    fastapi('put', url, params, (json)=>{
        alert('비밀번호가 변경되었습니다.')
        push('/user-login')
    }, (json_error)=>{error = json_error})
    }

</script>
    
<div id="login">
    <h1><strong>비밀번호를 변경합니다.</strong></h1>
    <Error error={error} />
    <form method="post">
        <fieldset>
        <p><input type="text" placeholder="Username" bind:value="{change_username}"></p>
        <p><input type="text" placeholder="email" bind:value="{change_email}"></p>
        <p><input type="password" placeholder="비밀번호" bind:value="{change_password1}"></p>
        <p><input type="password" placeholder="비밀번호 확인" bind:value="{change_password2}"></p>
        
        <p><input type="submit" value="변경하기" on:click={ChangePassword}></p>
        </fieldset>
    </form>
</div>

<style>
    @import './css/login.css';
</style>