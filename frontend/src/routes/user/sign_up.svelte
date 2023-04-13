<script>
import { push } from 'svelte-spa-router'
import fastapi from "../../lib/api"
import Error from '../../components/Error.svelte'

let error = {detail:[]}
let username = ''
let name = ''
let nickname = ''
let password1 = ''
let password2 = ''
let email = ''

function sign_up(event){
    event.preventDefault()
    let url = "/api/user/create"
    let params = {
      username: username,
      name: name,
      nickname: nickname,
      password1: password1,
      password2: password2,
      email: email
    }

    fastapi('post', url, params, (json) => {push('/user-login')}, (json_error)=>{error = json_error})
}
</script>

<body>
  <div class="signupFrm">
    <form action="" class="form">
      <h1 class="title">Sign up</h1>
      <Error error={error}/>
      
      <div class="inputContainer">
        <input type="text" class="input" placeholder="아이디" bind:value="{username}">
        <label for="" class="label">아이디</label>
      </div>
      
      <div class="inputContainer">
        <input type="text" class="input" placeholder="이름" bind:value="{name}">
        <label for="" class="label">이름</label>
      </div>

      <div class="inputContainer">
        <input type="text" class="input" placeholder="닉네임" bind:value="{nickname}">
        <label for="" class="label">닉네임</label>
      </div>
  
      <div class="inputContainer">
        <input type="password" class="input" placeholder="비밀번호" bind:value="{password1}">
        <label for="" class="label">비밀번호</label>
      </div>
  
      <div class="inputContainer">
        <input type="password" class="input" placeholder="2차 비밀번호" bind:value="{password2}">
        <label for="" class="label">비밀번호 확인</label>
      </div>
  
      <div class="inputContainer">
        <input type="text" class="input" placeholder="이메일" bind:value="{email}">
        <label for="" class="label">이메일</label>
      </div>
  
      <button type="submit" on:click="{sign_up}" class='submitBtn'>sign up!</button>
    </form>
  </div>
</body>

<style lang='scss'>
  @import '../css/sign_up.css';
</style>