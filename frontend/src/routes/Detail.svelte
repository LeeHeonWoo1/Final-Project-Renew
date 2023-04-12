<script>
    import fastapi from "../lib/api";
    import NavBar from "../components/NavBar.svelte";
    import Error from '../components/Error.svelte'
    import {is_login, username} from '../lib/store'
    import { Search, Button } from "flowbite-svelte";
    import { keyword } from "../lib/store";
    import { push, link } from "svelte-spa-router";
    
    export let params = {}
    
    let inform = {replies: []}
    let error = {detail: []}
    let video_id = params.video_id
    let content = ''
    let random_list = []
    let url = `/api/video/detail/${video_id}`

    function GetOneVideo(){
        fastapi('get', url, {}, (json) => {
            inform = json
        })
    }

    GetOneVideo()

    function GetRandomVideoList(){
        let url = "/api/video/random_list"
        fastapi('get', url, {}, (json)=>{
            random_list = json
        })
    }

    GetRandomVideoList()

    function postReply(event){
        event.preventDefault()
        let url = `/api/reply/create/${video_id}`
        let params = {
            username: $username,
            content: content
        }
        fastapi('post', url, params, (json)=>{
            content = ''
            error = {detail:[]}
            GetOneVideo()
            alert('댓글이 등록되었습니다.')
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
        <div id="comment_section">
            <Error error = {error}/>
                <strong><h3>{$username}</h3></strong>
                <form>
                <div class="w-full mb-4 border border-gray-200 rounded-lg bg-gray-50 dark:bg-gray-700 dark:border-gray-600">
                    <div class="px-4 py-2 bg-gary rounded-t-lg dark:bg-gray-800">
                        <label for="comment" class="sr-only">Your comment</label>
                        <textarea bind:value={content} id="comment" rows="4" class="w-full px-0 text-sm text-gray-900 bg-white border-0 dark:bg-gray-800 focus:ring-0 dark:text-white dark:placeholder-gray-400" placeholder="Write a comment..." required></textarea>
                    </div>
                    <div class="flex items-center justify-between px-3 py-2 border-t dark:border-gray-600">
                        {#if $is_login}
                            <button on:click = {postReply} type="submit" class="inline-flex items-center py-2.5 px-4 text-xs font-medium text-center text-white bg-blue-700 rounded-lg focus:ring-4 focus:ring-blue-200 dark:focus:ring-blue-900 hover:bg-blue-800">
                                댓글 등록
                            </button>
                        {/if}
                        <div class="flex pl-0 space-x-1 sm:pl-2">
                            <button type="button" class="inline-flex justify-center p-2 text-gray-500 rounded cursor-pointer hover:text-gray-900 hover:bg-gray-100 dark:text-gray-400 dark:hover:text-white dark:hover:bg-gray-600">
                                <svg aria-hidden="true" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M8 4a3 3 0 00-3 3v4a5 5 0 0010 0V7a1 1 0 112 0v4a7 7 0 11-14 0V7a5 5 0 0110 0v4a3 3 0 11-6 0V7a1 1 0 012 0v4a1 1 0 102 0V7a3 3 0 00-3-3z" clip-rule="evenodd"></path></svg>
                                <span class="sr-only">Attach file</span>
                            </button>
                            <button type="button" class="inline-flex justify-center p-2 text-gray-500 rounded cursor-pointer hover:text-gray-900 hover:bg-gray-100 dark:text-gray-400 dark:hover:text-white dark:hover:bg-gray-600">
                                <svg aria-hidden="true" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M5.05 4.05a7 7 0 119.9 9.9L10 18.9l-4.95-4.95a7 7 0 010-9.9zM10 11a2 2 0 100-4 2 2 0 000 4z" clip-rule="evenodd"></path></svg>
                                <span class="sr-only">Set location</span>
                            </button>
                            <button type="button" class="inline-flex justify-center p-2 text-gray-500 rounded cursor-pointer hover:text-gray-900 hover:bg-gray-100 dark:text-gray-400 dark:hover:text-white dark:hover:bg-gray-600">
                                <svg aria-hidden="true" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M4 3a2 2 0 00-2 2v10a2 2 0 002 2h12a2 2 0 002-2V5a2 2 0 00-2-2H4zm12 12H4l4-8 3 6 2-4 3 6z" clip-rule="evenodd"></path></svg>
                                <span class="sr-only">Upload image</span>
                            </button>
                        </div>
                    </div>
                </div>
                </form>
                <p class="ml-auto text-xs text-gray-500 dark:text-gray-400">남을 비방하는 내용은 삼가해주세요.</p>
            <ol class="large-numbers" style="margin-top: 30px;">
                <h2>{inform.replies.length}개의 댓글</h2>
                {#each inform.replies as reply}
                    <li>{reply.writer} : {reply.content}</li>
                {/each}
            </ol>
        </div>
    </main>
    <aside class="sub-videos">
        <h3 style="width: 380px; margin-bottom:20px;">more videos...</h3>
        {#each random_list as rand_video}
            <div class='singer' style="font-size: 14px;">{rand_video.singer}</div>
            <a use:link href='/detail/{rand_video.id}' on:click={()=>{window.location.reload()}}><img class='videos' src="{rand_video.src}" alt="{rand_video.singer}"></a>
        {/each}
    </aside>
    <footer>
        <h3 style="text-align: center;"> test text </h3>
    </footer>
</div>

<style>    
@import url(https://fonts.googleapis.com/css?family=Roboto+Slab:400,700);
ol.large-numbers {
  counter-reset:li; /* Initiate a counter */
  margin-left:0; /* Remove the default left margin */
  padding-left:0; /* Remove the default left padding */
  line-height: 1.25;
}
ol.large-numbers > li {
  position:relative; /* Create a positioning context */
  list-style:none; /* Disable the normal item numbering */
  margin: 1rem 0 1rem 2rem;
  padding: 0 0 0 1rem;
}
ol.large-numbers > li:before {
  font-family:'Roboto Slab', "Gill Sans", "Gill Sans MT", "Myriad Pro", "DejaVu Sans Condensed", Helvetica, Arial, sans-serif;
  content:counter(li); /* Use the counter as content */
  counter-increment:li; /* Increment the counter by 1 */
  /* Position and style the number */
  position:absolute;
  top: -0.3em; /* move numbers up or down as needed */
  left:-0.9em;
  width: 1em;
  text-align:center;
  -moz-box-sizing:border-box;
  -webkit-box-sizing:border-box;
  box-sizing:border-box;
  font-size: 2em;
  font-weight: bold;
  font-weight: 700;
  color: #A8CABA;
  text-shadow:
       3px 3px 0 #838689,
     -1px -1px 0 #838689,  
      1px -1px 0 #838689,
      -1px 1px 0 #838689,
       1px 1px 0 #838689;
}
ol.large-numbers li:hover:before {
  color: #EBE3AA;
}
#comment_section{
    margin-top: 50px;
}
    
#nav-bar {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
}

.container {
    font-family:'Roboto Slab', "Gill Sans", "Gill Sans MT", "Myriad Pro", "DejaVu Sans Condensed", Helvetica, Arial, sans-serif;
    margin-top: 100px;
    display: grid;
    grid-template-rows: repeat(auto, 200px);
    grid-template-columns: 1100px 20px 380px;
    grid-template-areas:
        "main aside aside1"
        "main aside aside1"
        "main aside aside1"
        "main aside aside1"
        ". . ."
        "footer footer footer";
    gap:20px;
}

h2{
    font-family:'Roboto Slab', "Gill Sans", "Gill Sans MT", "Myriad Pro", "DejaVu Sans Condensed", Helvetica, Arial, sans-serif;
    border:none;
    width:1100px;
    margin-top: 5px;
}


main { grid-area: main; margin-left: 0px; }
footer {grid-area: footer;}
aside {grid-area: aside1;}

</style>