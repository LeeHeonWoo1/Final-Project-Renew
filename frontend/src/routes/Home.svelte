<script>
    import fastapi from '../lib/api'
    import {link} from 'svelte-spa-router'
    import NavBar from '../components/NavBar.svelte';
    import {keyword} from '../lib/store'
    import NotFound from '../components/NotFound.svelte';
    import { Search, Button } from 'flowbite-svelte';

    let video_list = []

    function get_video_list() {
        fastapi('post', `/api/video/search`, {keyword:$keyword}, (json)=>{
            video_list = json
        })
    }
    get_video_list()
</script>

<div class="col">
    <div class="nav-bar">
        <NavBar />
    </div>
    <div class="flex gap-2" id="search-box">
        <Search bind:value={$keyword} size='md' class="flex gap-2 items-center" placeholder="곡 제목 or 가수의 이름을 영어로 검색하세요"/>
        <Button size='sm' on:click={get_video_list}>
        <svg class="w-5 h-5 mr-2 -ml-1" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
        Search
        </Button>
    </div>
    <div style="margin-top:120px;" class='container'>
        {#if video_list.length === 0}
            <div id="not-found">
                <NotFound/>
            </div>
        {:else if video_list.length !== 0}
            {#each video_list as video}
            <div class='item'>
                <a use:link href='/detail/{video.id}'><img class='videos' src="{video.src}" alt="{video.singer}"></a>
                <div class='singer'>{video.singer}</div>
            </div>
            {/each}
        {/if}
    </div>
</div>

<style>
#not-found{
    position:absolute;
    margin-top: -280px;
    margin-left: -180px;
}
.nav-bar{
    position:fixed;
    top:0;
    left:0;
    right:0;
}
.col{
    font-family:'Roboto Slab', "Gill Sans", "Gill Sans MT", "Myriad Pro", "DejaVu Sans Condensed", Helvetica, Arial, sans-serif;
}
.container {
    display: grid;
    margin-left: auto;
    margin-right: auto;
    margin-top: 150px;
    grid-template-columns: repeat(5, 1fr);
    gap: 20px;
}

.videos {
    size: 200px 200px;
}

.singer{
    font-size: 12px;
}

#search-box{
    position:fixed;
    width:600px;
    top: 20px;
    left: 350px;
}
</style>