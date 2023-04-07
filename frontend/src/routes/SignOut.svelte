<script>
    import NavBar from "../components/NavBar.svelte";
    import Error from "../components/Error.svelte";

    let error = {detail:[]}
    let db_name = ''
    let db_email = ''
    let db_password = ''

    function UserSignOut(){

    }
</script>

<NavBar/>

<div id="login" class='container'>
    <h1><strong>회원탈퇴</strong></h1>
    <h6>가입한 이름과 이메일을 입력해주세요.</h6>
    <Error error={error} />
    <form method="post">
        <fieldset>
        <p><input type="text" placeholder="이름" bind:value="{db_name}"></p>
        <p><input type="text" placeholder="이메일" bind:value="{db_email}"></p>
        <p><input type="text" placeholder="비밀번호" bind:value="{db_password}"></p>
        <p><input class='signout-btn' type="submit" value="회원탈퇴" on:click={UserSignOut}></p>
        </fieldset>
    </form>
</div>

<style>
    .signout-btn{
        background-color: red;
    }
</style>