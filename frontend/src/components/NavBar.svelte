<script>
  import { Navbar, NavBrand, NavLi, NavUl, NavHamburger, Dropdown, DropdownItem, Chevron, DropdownDivider, Search, Button} from 'flowbite-svelte'
  import {link, push} from 'svelte-spa-router'
  import { keyword, videoList } from '../lib/store';
  import { access_token, username, is_login, section } from "../lib/store"
  import dancey from '../assets/dancey.png'
  import fastapi from '../lib/api';

  function get_video_list() {
    fastapi('post', `/api/video/search`, {keyword:$keyword}, (json)=>{
      $videoList = json
      push('/')
    })
  }
</script>

<style>
  #nav-bar{
    position:relative;
    top: 0;
    right: 0;
    left: 0;
  }

  #logo{
    font-family:'Roboto Slab', "Gill Sans", "Gill Sans MT", "Myriad Pro", "DejaVu Sans Condensed", Helvetica, Arial, sans-serif;
  }

  #search-box{
    width:400px;
    top: 20px;
    left: 350px;
}
</style>

<div id="nav-bar">
  <Navbar let:hidden let:toggle>
    <NavBrand href="/">
      <img src="{dancey}" class="mr-3 h-6 sm:h-9" alt="Flowbite Logo"/>
      <span class="self-center whitespace-nowrap text-xl font-semibold dark:text-white" id="logo">
        Dancey
      </span>
    </NavBrand>
    <div class="flex gap-2" id="search-box">
      <Search bind:value={$keyword} size='md' class="flex gap-2 items-center" placeholder="곡 제목, 가수의 이름을 영어로 검색"/>
      <Button size='sm' on:click={get_video_list}>
        <svg class="w-5 h-5 mr-2 -ml-1" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
        Search
      </Button>
    </div>
    <NavHamburger on:click={toggle}/>
    <NavUl {hidden}>
      <NavLi active={true}><a use:link href='/board' on:click={(event)=>{
        event.preventDefault()
        window.location.reload()
        $section="게시판"
        }}>게시판</a></NavLi>
      <NavLi ><a use:link href='/service'>정확도 책정</a></NavLi>
      <NavLi ><a use:link href='/service'>보관함</a></NavLi>
      <NavLi ><a use:link href='/service'>포인트샵</a></NavLi>
      <Dropdown triggeredBy="#nav-menu1" class="w-44 z-20">
        <DropdownItem><a use:link href='/'>대시보드</a></DropdownItem>
        <DropdownItem>Settings</DropdownItem>
        <DropdownItem>Earnings</DropdownItem>
        <DropdownDivider />
        <DropdownItem><a use:link href='/sign_out'>회원탈퇴</a></DropdownItem>
      </Dropdown>
      <NavLi id="nav-menu1" class="cursor-pointer"><Chevron aligned>Dropdown</Chevron></NavLi>
      {#if $is_login}
        <h5>환영합니다. {$username}님.</h5>
        <a use:link href='/user-login'><button id='login-btn' on:click={() => {
          $access_token = ''
          $username = ''
          $is_login = false}}>로그아웃</button></a>
      {:else}
        <a use:link href='/user-login'><button id='login-btn'>로그인</button></a>
        <a use:link href='/sign_up'><button id='sign-up-btn'>회원가입</button></a>
      {/if}
    </NavUl>
  </Navbar>
</div>