<script>
    import fastapi from "../lib/api";
    import {link} from 'svelte-spa-router'
    import {Button} from 'flowbite-svelte'
    import NavBar from "../components/NavBar.svelte";
    import Error from '../components/Error.svelte'
    
    export let params = {}
    let inform = {replies: []}
    let error = {detail: []}
    let video_id = params.video_id
    let content = ''

    let url = `/api/video/detail/${video_id}`

    function GetOneVideo(){
        fastapi('get', url, {}, (json) => {
            inform = json
        })
    }

    GetOneVideo()

    function postReply(event){
        event.preventDefault()
        let url = `/api/reply/create/${video_id}`
        let params = {
            content: content
        }
        fastapi('post', url, params, (json)=>{
            content = ''
            GetOneVideo()
        }, (json_error)=>{
            error = json_error
        })
    }
</script>

<div class="container">
    <div id='nav-bar'>
        <NavBar/>
    </div>
    <main>
        <iframe  width="1100" height="600" src="{inform.youtube_url}?autoplay=0" title="YouTube video player" frameborder="0" 
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
        <h2>{inform.singer}</h2>
        <form method="post">
            <div id="reply">
                <Error error = {error}/>
                <textarea class="replies" bind:value={content}></textarea>
                <Button on:click={postReply}>댓글달기</Button>
            </div>
        </form>
        <ul class="comments">
            <h2>{inform.replies.length}개의 댓글</h2>
            {#each inform.replies as reply}
                <li>{reply.content}</li>
            {/each}
        </ul>
    </main>
</div>

<style>
#nav-bar {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
}

.container {
    margin-top: 100px;
    display: grid;
    grid-template-rows: repeat(4, 200px);
    grid-template-columns: 1100px 20px 380px;
    grid-template-areas:
        "main aside aside1"
        "main aside aside1"
        "main aside aside1"
        "main aside aside1";
    gap:20px;
}

h2{
    border:none;
    width:1100px;
    margin-top: 5px;
}

.replies{
    margin-top: 10px;
    width:1100px;
    resize:none;
    height: 45px;
}

main { grid-area: main; margin-left: 0px; }
</style>