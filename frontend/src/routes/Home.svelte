<script>
    import fastapi from '../lib/api'
    import {link} from 'svelte-spa-router'
    import NavBar from '../components/NavBar.svelte';
    import {keyword, videoList} from '../lib/store'
    import NotFound from '../components/NotFound.svelte';
    import { Search, Button } from 'flowbite-svelte';
</script>

<div class="main">
    <NavBar />
    <div style="margin-top:120px;" class='container'>
        {#if $videoList.length === 0}
            <div id="not-found">
                <NotFound/>
            </div>
        {:else if $videoList.length !== 0}
            {#each $videoList as video}
            <div class='item'>
                <a use:link href='/detail/{video.id}'><img class='videos' src="{video.src}" alt="{video.singer}"></a>
                <div class='singer'>{video.singer}</div>
            </div>
            {/each}
        {/if}
    </div>
</div>

<style>
.videos{
    border-radius: 5px;
}

#not-found{
    position:absolute;
    margin-top: -280px;
    margin-left: -180px;
}

.main{
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

.singer{
        font-size: 11px;
    }

@media only screen and (max-width: 1280px){
    .container {
    display: grid;
    margin: auto;
    margin-top: 150px;
    grid-template-columns: repeat(3, 1fr);
    gap: 10px;
    }

    .singer{
        font-size: 1px;
    }
}
</style>