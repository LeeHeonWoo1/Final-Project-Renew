<script>
  import { Textarea, Toolbar, ToolbarGroup, ToolbarButton, Button, Chevron, Dropdown, DropdownItem, Input, ButtonGroup, Heading, P, Span } from 'flowbite-svelte'
  import NavBar from '../../components/NavBar.svelte';
  import { board_option, user_nickname } from '../../lib/store';
  import fastapi from '../../lib/api';
  import { push } from 'svelte-spa-router';

  let dropdown_options = [
    {id:1, text:'홍보 게시판'},
    {id:2, text:'크루 소개'},
    {id:3, text:'장르별 모집'},
    {id:4, text:'자유 게시판'},
    {id:5, text:'Shorts'}
  ]

  let _content=""
  let _title=""
  
  function CreateArticle(event){
    event.preventDefault();
    let url = "/api/board/create_article"
    let params = {
      title: _title,
      content: _content,
      writer: $user_nickname,
      section: $board_option
    }

    fastapi('post', url, params, (json)=>{
      alert('게시글이 등록되었습니다.')
      push('/board')
    })
    
  }
</script>

<div class="container">
  <div id="navigation_bar">
    <NavBar/>
  </div>
  <main id="create_article">
    <Heading tag="h1" class="mb-4" customSize="text-3xl font-extrabold  md:text-5xl lg:text-6xl">게시글 작성</Heading>
    <P>게시판 선택 후 제목과 내용을 작성해주세요.</P>
    <form method='post'>
      <ButtonGroup class="w-full">
        <Button placeholder="선택" class="flex-shrink-0 text-gray-900 bg-gray-100 border border-gray-300 dark:border-gray-700 dark:text-white hover:bg-gray-200 focus:ring-gray-300 dark:bg-gray-600 dark:hover:bg-gray-700 dark:focus:ring-gray-800">
          <Chevron>{$board_option}</Chevron>
        </Button>
        <Dropdown>
          {#each dropdown_options as option}
            <DropdownItem on:click="{()=>{
                $board_option = option.text
            }}">{option.text}</DropdownItem>
          {/each}
        </Dropdown>
        <Input placeholder="제목" bind:value={_title} />
      </ButtonGroup>
      <div id="editor">
        <Textarea id="editor" rows="8" class="mb-4" placeholder="부적절한 내용은 확인 후 삭제처리 될 수 있음을 알려드립니다." bind:value={_content}>
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
          </Toolbar>
        </Textarea>
        <div id="post-btn">
          <Button on:click={(event)=>{
            CreateArticle(event)
            $board_option=""}}>작성완료</Button>
        </div>
      </div>
    </form>
  </main>
</div>

<style>
  #navigation_bar{
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
  }

  .container{
    display: grid;
    position: relative;
    margin-left: -210px;
    margin-top: -10px;
    grid-template-columns: 300px 1136px;
    grid-template-areas: 
    "aside main"
    "aside main";
  }

  main{
    grid-area: main;
    margin-top: 18px;
  }

  #editor{
    margin-top: 30px;
  }

  #post-btn{
    margin-left: 1040px;
    margin-top: 135px;
  }

</style>