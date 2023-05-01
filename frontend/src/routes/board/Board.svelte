<script>
    import { Table, TableBody, TableBodyCell, TableBodyRow, TableHead, TableHeadCell, Button, Search, Heading, PaginationItem } from 'flowbite-svelte';
    import NavBar from '../../components/NavBar.svelte';
    import { push, link } from 'svelte-spa-router';
    import SideBar from '../../components/SideBar.svelte';
    import { is_login, section, page, articleList } from '../../lib/store';
    import moment from 'moment/min/moment-with-locales';
    moment.locale('ko')


    function GotoPost(){
        if ($is_login){
                push('/board/create')
        }else{
                alert('로그인 후 이용해주세요')
                push('/user-login')
            }
        }
</script>

<div id="navigation-bar">
    <NavBar/>
</div>
<div class="container">
    <main class="main-table">
        <Heading tag="h1" class="mb-4" customSize="text-3xl font-extrabold  md:text-5xl lg:text-6xl">{$section}</Heading>
        <div align="right" id="sub_container">
            <Button on:click={GotoPost}>글쓰기</Button>
            <!-- <div id="search_box">
                <Search size="md" />
                    <Button class="!p-2.5">
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
                    </Button>
            </div> -->
        </div>
        <Table shadow>
            <TableHead>
                <TableHeadCell>글 번호</TableHeadCell>
                <TableHeadCell>제목</TableHeadCell>
                <TableHeadCell>작성자</TableHeadCell>
                <TableHeadCell>게시판</TableHeadCell>
                <TableHeadCell>작성일시</TableHeadCell>
            </TableHead>
            <TableBody>
                {#each $articleList as article}
                    <TableBodyRow>
                        <TableBodyCell>{article.id}</TableBodyCell>
                        <TableBodyCell><a use:link href='/board/detail/{article.id}'>{article.title}</a></TableBodyCell>
                        <TableBodyCell>{article.writer}</TableBodyCell>
                        <TableBodyCell>{article.section}</TableBodyCell>
                        <TableBodyCell>{moment(article.write_date).format("YYYY년 MM월 DD일 a hh:mm")}</TableBodyCell>
                    </TableBodyRow>
                {/each}
            </TableBody>
        </Table>
    </main>
    <SideBar/>
</div>

<style>
    #navigation-bar{
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
    }

    .container{
        display: grid;
        position: relative;
        margin-left: -110px;
        margin-top: 50px;
        grid-template-columns: 300px 1136px;
        grid-template-areas: 
        "aside main"
        "aside main";
    }

    main{grid-area: main;}

    .main-table{
        position: relative;
        width: 1136px;
    }

    #sub_container{
        position:relative;
        width: 1136px;
        margin-bottom: 10px;
        align-self: right;
    }

    #search_box{
        position: relative;
        margin-left: 0px;
        height: 40px;
    }
</style>