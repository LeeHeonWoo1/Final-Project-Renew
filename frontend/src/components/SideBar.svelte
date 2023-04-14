<script>
    import { section, page, articleList} from '../lib/store';
    import { push } from 'svelte-spa-router';
    import fastapi from '../lib/api';

    let sections = [
        {id:1, label:'게시판'},
        {id:2, label:'공지 사항'},
        {id:3, label:'홍보 게시판'},
        {id:4, label:'크루 소개'},
        {id:5, label:'장르별 모집'},
        {id:6, label:'자유 게시판'},
        {id:7, label:'Shorts'},
    ]

    let size = 10
    let total = 0
    $: total_page = Math.ceil(total/size)

    function GetArticleList(_page, _section){
        let url = "/api/board/article_list"
        let params = {
            page: _page,
            size: size,
            section: _section
        }

        fastapi('get', url, params, (json)=>{
            $articleList = json.article_list
            $page = _page
            total = json.total
        })
    }

    GetArticleList($page, $section)
</script>

<aside>
    <div class="container">
        {#each sections as sec}
            <button on:click={()=>{
                $section = sec.label
                $page = 0
                GetArticleList($page, $section)
                push('/board')
                }} class="link text">{sec.label}</button>
        {/each}
        <div class="link text"></div>
        <div class="link text"></div>
        <div class="link text"></div>
        <div class="link text"></div>
        <div class="link text"></div>
        <div class="link text"></div>
    </div>
</aside>

<div id='pagination'>
    <ul>
        <li>
            <button class='page_item' on:click={()=>{GetArticleList(0, $section)}}>처음으로</button>
        </li>
        <li>
            <button class='page_item' disabled='{$page <= 0}' on:click={()=>{GetArticleList($page-1, $section)}}>&laquo;</button>
        </li>
            {#each Array(total_page) as _, loop_page}
                {#if loop_page >= $page-3 && loop_page <= $page+3}
                    <li>
                        <button class='page_item' class:active={loop_page === $page} on:click={()=>{GetArticleList(loop_page, $section)}}>{loop_page+1}</button>
                    </li>
                {/if}
            {/each}
        <li>
            <button class='page_item' disabled='{$page >= total_page-1}' on:click={()=>{GetArticleList($page+1, $section)}}>&raquo;</button>
        </li>
        <li>
            <button class='page_item' on:click={()=>{GetArticleList(total_page-1, $section)}}>마지막으로</button>
        </li>
    </ul>
</div>

<style> 
#pagination{
    margin-left: 570px;
    width: 800px;
}

#pagination button{
    float: left;
    padding: 8px 16px;
    text-decoration: none;
    transition: background-color .3s;
    border: 1px solid #ddd;
}

#pagination button.active {
  background-color: #2420ff;
  color: white;
  border: 1px solid #0400ff;
}

#pagination button:hover:not(.active) {background-color: #ddd;}

aside{
    grid-area: aside;
    margin-top: -30px;
}

.container{
   max-width:200px;
   background:rgba(0, 0, 0, 0.062);
   margin:40px auto;
   padding:10px 0px 20px 0px;
   border-radius:4px;
}

.link{
    font-size:16px;
    font-weight:300;
    text-align:center;
    position:relative;
    height:40px;
    line-height:40px;
    margin-top:10px;
    overflow:hidden;
    width:90%;
    margin-left:5%;
    cursor:pointer;
}
.link:after{
    content: '';
    position:absolute;
    width:80%;
    border-bottom:1px solid rgba(255, 255, 255, 0.808);
    bottom:50%;
    left:-100%;
    transition-delay: all 0.5s;
    transition: all 0.5s;
}
.link:hover:after{
    left:100%;
}
</style>