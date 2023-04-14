<script>
    import NavBar from "../../components/NavBar.svelte";
    import fastapi from "../../lib/api";
    import moment from 'moment/min/moment-with-locales';
    moment.locale('ko')

    export let params = {}
    let _id = params.article_id
    let article = {}
    let url = `/api/board/get_one_article/${_id}`

    fastapi('get', url, {}, (json)=>{
        article = json
    })

</script>

<NavBar/>
<div class="container">
    <div class="item">{article.title}</div>
    <div class="item">{article.content}</div>
    <div class="item">{moment(article.write_date).format("YYYY년 MM월 DD일 a hh:mm")}</div>
    <div class="btn_container">
        <button class="btn">수정</button>
        <button class="btn">삭제</button>
    </div>
</div>

<style>
.container {
	/* display: flex; */
	display: inline-flex;
    flex-direction: column;
    justify-content: center;
    align-items: stretch;
    height: 600px;
    width: 1517px;
}

.item:nth-child(1) { flex-grow: 1; align-self: flex-center;}
.item:nth-child(2) { flex-grow: 2; }
.item:nth-child(3) { flex-grow: 1; }

.btn_container{
    display: flex;
    flex-direction: row;
}

.btn:nth-child(1){ flex-grow: 1;}
.btn:nth-child(2){ flex-grow: 1;}
</style>