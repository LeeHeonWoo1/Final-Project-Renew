<script>
    import { Table, TableBody, TableBodyCell, TableBodyRow, TableHead, TableHeadCell } from 'flowbite-svelte';
    import NavBar from '../../components/NavBar.svelte';
    import fastapi from '../../lib/api';
    import { link } from 'svelte-spa-router';
    import { username } from '../../lib/store';

    let articleList = []
    let url = "/api/board/article_list"
    fastapi('get', url, {writer:$username})

</script>

<div class="container">
    <header id="nav-bar">
        <NavBar/>
    </header>

    <main class="main-table">
        <Table shadow>
            <TableHead>
                <TableHeadCell>글 번호</TableHeadCell>
                <TableHeadCell>제목</TableHeadCell>
                <TableHeadCell>작성자</TableHeadCell>
                <TableHeadCell>작성일시</TableHeadCell>
                <TableHeadCell>조회수</TableHeadCell>
            </TableHead>
            <TableBody>
                <TableBodyRow>
                    <TableBodyCell>1</TableBodyCell>
                    <TableBodyCell>Apple MacBook Pro 17"</TableBodyCell>
                    <TableBodyCell>Sliver</TableBodyCell>
                    <TableBodyCell>Laptop</TableBodyCell>
                    <TableBodyCell>$2999</TableBodyCell>
                </TableBodyRow>
            </TableBody>
        </Table>
    </main>

    <a use:link href="/board/create">글쓰기</a>
</div>

<style>
    .main-table{
        position: relative;
        width: 1280px;
    }
</style>