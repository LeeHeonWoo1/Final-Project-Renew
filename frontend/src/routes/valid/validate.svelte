<script>
    // validation before change password
    import Error from '../../components/Error.svelte'
    import {link, push} from 'svelte-spa-router'
    import fastapi from '../../lib/api';
    import { P } from 'flowbite-svelte';
    
    let error = {detail:[]}
    let username = ''
    let useremail = ''
    let input_number = ''
    let validNumber = ''
    
    function SendValidEmail(event){
        event.preventDefault()

        let url = '/api/user/validation'
        let params = {
            username: username,
            email:useremail
        }

        fastapi('post', url, params, (json)=>{
            alert(`${useremail}로 메일이 발송되었습니다.`)
            validNumber = json
        }, (json_error)=>{
            error = json_error
        })

    }
    function validateNumber(){
    if (parseInt(input_number) === parseInt(validNumber)){
            alert('인증되었습니다. 비밀번호 변경 페이지로 이동합니다.')
            push('/change-password')
        }
    else{
        alert('잘못된 인증번호입니다.')
    }
    }

</script>
        
<div id="login">
    <h1><strong>비밀번호 찾기</strong></h1>
    <h2>아이디, 이메일을 입력해주세요.</h2>
    <Error error={error} />
    <form method="post">
        <fieldset>
        <p><input type="text" placeholder="아이디" bind:value="{username}"></p>
        <p><input type="text" placeholder="이메일" bind:value="{useremail}"></p>
        <p><input type="submit" value="인증메일 발송" on:click={SendValidEmail}></p>

        </fieldset>
    </form>
</div>

<div id="valid">
    <h1><strong>인증번호 입력</strong></h1>
    <h2>인증번호를 입력해주세요.</h2>
    <fieldset>
    <p><input class='val_num_space' type="text" placeholder="인증번호" bind:value="{input_number}"></p>
    <button class='btn-commit' on:click = {validateNumber}>확인하기</button>

    </fieldset>
</div>

<style>
    @import '../css/login.css';
</style>