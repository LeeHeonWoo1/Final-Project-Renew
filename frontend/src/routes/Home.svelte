<script>
    import fastapi from '../lib/api'
    import {link} from 'svelte-spa-router'
    import NavBar from '../components/NavBar.svelte';

    let video_list = []

    function get_video_list() {
        fastapi('get', '/api/video/list', {}, (json)=>{
            video_list = json
        })
    }

    get_video_list()
</script>

<NavBar />
<div style="margin-top:60px;" class='container'>
    {#each video_list as video}
        <div class='item'>
            <a use:link href='/detail/{video.id}'><img class='videos' src="{video.src}" alt="{video.singer}"></a>
            <div class='singer'>{video.singer}</div>
        </div>
    {/each}
</div>

<style>
    .container {
        display: grid;
        margin-left: auto;
        margin-right: auto;
        margin-top: auto;
        grid-template-columns: repeat(5, 1fr);
        gap: 20px;
    }

    .videos {
        size: 200px 200px;
    }

    .singer{
        font-size: 12px;
    }
</style>