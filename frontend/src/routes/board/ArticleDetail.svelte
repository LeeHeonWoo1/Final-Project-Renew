<script>
    import { push, link } from "svelte-spa-router";
    import NavBar from "../../components/NavBar.svelte";
    import fastapi from "../../lib/api";
    import { user_nickname, page, section } from "../../lib/store";
    import { Button, Textarea, Toolbar, ToolbarGroup, ToolbarButton } from "flowbite-svelte";
    import {marked} from 'marked'

    export let params = {}
    let _id = params.article_id
    let article = {answers:[], content:''}
    let answers=''
    let url = `/api/board/get_one_article/${_id}`

    fastapi('get', url, {}, (json)=>{
        article = json
    })

    function ModArticle(){
      let url = `/api/board/modify/${_id}`
    }

    function DelArticle(){
      let url = `/api/board/delete_article/${_id}`

      let result = confirm('정말로 삭제하시겠습니까?')
      if (result == true){
        fastapi('delete', url, {}, (json)=>{
        alert('삭제 완료되었습니다.')
        push('/board')
      })
      }
    }

    function PostAnswer(){
      let url = `/api/answer/create_answer/${_id}`
      let params = {
        writer: $user_nickname,
        content: answers
      }

      fastapi('post', url, params, (res)=>{
        alert('댓글이 등록되었습니다.')
        answers = ''
        window.location.reload()
      })
    }

</script>

<div id="navigation_bar">
  <NavBar/>
</div>
<br><br><br>
<div id="wapper">
  <header>
    <p>{article.title}</p>
  </header>
  <section>
    <p>{article.section}</p>
    <article>
      <p>{@html marked.parse(article.content)}</p>
    </article>
  </section>
  <br><br><br>
  <div class="btn_container">
    <div class="btn">
        <Button disabled='{$user_nickname !== article.writer}' on:click={ModArticle}>수정</Button>
    </div>
    <div class="btn">
        <Button disabled='{$user_nickname !== article.writer}' on:click={DelArticle}>삭제</Button>
    </div>
    <div class="btn">
        <Button on:click={()=>{
          $page = 0
          push('/board')
        }}>목록으로</Button>
    </div>
</div>
<br><br><br>
  <footer>
    <div class="item">
      <form>
          <label for="editor" class="sr-only">Publish post</label>
          <Textarea bind:value={answers} id="editor" rows="8" class="mb-4" placeholder="댓글을 작성하세요. ">
            <Toolbar slot="header" embedded>
              <ToolbarGroup>
                <ToolbarButton name="Attach file"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6"><path stroke-linecap="round" stroke-linejoin="round" d="M18.375 12.739l-7.693 7.693a4.5 4.5 0 01-6.364-6.364l10.94-10.94A3 3 0 1119.5 7.372L8.552 18.32m.009-.01l-.01.01m5.699-9.941l-7.81 7.81a1.5 1.5 0 002.112 2.13" /></svg></ToolbarButton>
                <ToolbarButton name="Embed map"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6"><path stroke-linecap="round" stroke-linejoin="round" d="M15 10.5a3 3 0 11-6 0 3 3 0 016 0z" /><path stroke-linecap="round" stroke-linejoin="round" d="M19.5 10.5c0 7.142-7.5 11.25-7.5 11.25S4.5 17.642 4.5 10.5a7.5 7.5 0 1115 0z" /></svg></ToolbarButton>
                <ToolbarButton name="Upload image"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6"><path stroke-linecap="round" stroke-linejoin="round" d="M2.25 15.75l5.159-5.159a2.25 2.25 0 013.182 0l5.159 5.159m-1.5-1.5l1.409-1.409a2.25 2.25 0 013.182 0l2.909 2.909m-18 3.75h16.5a1.5 1.5 0 001.5-1.5V6a1.5 1.5 0 00-1.5-1.5H3.75A1.5 1.5 0 002.25 6v12a1.5 1.5 0 001.5 1.5zm10.5-11.25h.008v.008h-.008V8.25zm.375 0a.375.375 0 11-.75 0 .375.375 0 01.75 0z" /></svg></ToolbarButton>
              </ToolbarGroup>
              <ToolbarGroup>
                <ToolbarButton name="Format code"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6"><path stroke-linecap="round" stroke-linejoin="round" d="M17.25 6.75L22.5 12l-5.25 5.25m-10.5 0L1.5 12l5.25-5.25m7.5-3l-4.5 16.5" /></svg></ToolbarButton>
                <ToolbarButton name="Add emoji"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6"><path stroke-linecap="round" stroke-linejoin="round" d="M15.182 15.182a4.5 4.5 0 01-6.364 0M21 12a9 9 0 11-18 0 9 9 0 0118 0zM9.75 9.75c0 .414-.168.75-.375.75S9 10.164 9 9.75 9.168 9 9.375 9s.375.336.375.75zm-.375 0h.008v.015h-.008V9.75zm5.625 0c0 .414-.168.75-.375.75s-.375-.336-.375-.75.168-.75.375-.75.375.336.375.75zm-.375 0h.008v.015h-.008V9.75z" /></svg></ToolbarButton>
              </ToolbarGroup>
              <ToolbarButton name="send" slot="end"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6"><path stroke-linecap="round" stroke-linejoin="round" d="M6 12L3.269 3.126A59.768 59.768 0 0121.485 12 59.77 59.77 0 013.27 20.876L5.999 12zm0 0h7.5" /></svg></ToolbarButton>
            </Toolbar>
          </Textarea>
          <Button on:click={PostAnswer}>댓글 등록</Button>
        </form>
  </div>
  </footer>
  <br><br>
  <aside>
    <p>댓글</p>
    <ul id="replies">
      {#each article.answers as answer}
        <li>
          {answer.answer_writer} : {answer.answer}
        </li>
      {/each}
    </ul>
  </aside>
</div>

<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Serif+KR:wght@300&display=swap');

#navigation_bar{
  margin-top: 0px;
}

.btn_container{
  display: flex;
  flex-direction: row;
  justify-content: right;
  gap: 5px;
}

div#wapper {
    position: relative;
    display: flex;
    flex-direction: column;
		width: 1536px;
		text-align: left;
		min-height: 300px;
		margin: 0 auto;
	}

header{
  position: relative;
  font-size: 40px;
}

section{
  border: 1px solid #999;
  border-radius: 5px;
}

aside{
  border: 1px solid #999;
  border-radius: 5px;
}

header, footer, aside, section {
  margin: 5px;
  padding: 10px;
}
header {
  height: auto;
}

aside {
  height: auto;
}

footer {
  height: auto;
  position: relatiev;
  clear: both;
}

#replies{
  border: 1px solid #999;
  border-radius: 5px;
}
</style>