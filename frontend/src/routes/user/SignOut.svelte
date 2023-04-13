<script>
    import NavBar from "../../components/NavBar.svelte";
    import Error from "../../components/Error.svelte";
    import fastapi from "../../lib/api";
    import { push } from "svelte-spa-router";
    import { access_token, username, is_login } from "../../lib/store"

    let error = {detail:[]}
    let db_username = ''
    let db_email = ''
    let db_password = ''

    function UserSignOut(event){
        event.preventDefault()

        let url = '/api/user/sign_out'
        let params = {
            username: db_username,
            email: db_email,
            password: db_password
        }
        fastapi('delete', url, params, (json)=>{
            alert('회원 탈퇴가 완료되었습니다.')
            $access_token = ''
            $username = ''
            $is_login = false
            push('/')
        }, (json_error)=>{
            error = json_error
        })
    }
</script>

<NavBar/>
<div id="login" class='container'>
    <h1><strong>회원탈퇴</strong></h1>
    <h6>아래 정보를 입력해주세요.</h6>
    <Error error={error} />
    <form method="post">
        <fieldset>
        <p><input type="text" placeholder="아이디" bind:value="{db_username}"></p>
        <p><input type="text" placeholder="이메일" bind:value="{db_email}"></p>
        <p><input type="password" placeholder="비밀번호" bind:value="{db_password}"></p>
        <p><input class='signout-btn' type="submit" value="회원탈퇴" on:click={UserSignOut}></p>
        </fieldset>
    </form>
</div>

<style>
    .signout-btn{
        background-color: red;
    }
</style>