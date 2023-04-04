<script>
  import { Navbar, NavBrand, NavLi, NavUl, NavHamburger, Dropdown, DropdownItem, Chevron, DropdownDivider, Button } from 'flowbite-svelte'
  import {link} from 'svelte-spa-router'
  import { access_token, username, is_login } from "../lib/store"
</script>

<Navbar let:hidden let:toggle>
  <NavBrand href="/">
    <img
      src="https://flowbite.com/docs/images/logo.svg"
      class="mr-3 h-6 sm:h-9"
      alt="Flowbite Logo"
    />
    <span class="self-center whitespace-nowrap text-xl font-semibold dark:text-white">
      Dancey
    </span>
  </NavBrand>
  <NavHamburger on:click={toggle} />
  <NavUl {hidden}>
    <NavLi href="/" active={true}>Home</NavLi>
    <NavLi href="/services">Services</NavLi>
    <NavLi href="/pricing">Pricing</NavLi>
    <NavLi href="/contact">Contact</NavLi>
    <Dropdown triggeredBy="#nav-menu1" class="w-44 z-20">
      <DropdownItem>Dashboard</DropdownItem>
      <DropdownItem>Settings</DropdownItem>
      <DropdownItem>Earnings</DropdownItem>
      <DropdownDivider />
      <DropdownItem>Sign out</DropdownItem>
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