<script>
  import Router from 'svelte-spa-router'
  import Home from './routes/Home.svelte'
  import Detail from './routes/Detail.svelte';
  import SignUp from './routes/user/sign_up.svelte';
  import Login from './routes/user/Login.svelte';
  import ChangePassword from './routes/user/ChangePassword.svelte';
  import FindId from './routes/user/FindID.svelte';
  import validate from './routes/valid/validate.svelte'
  import SignOut from './routes/user/SignOut.svelte';
  import Board from './routes/board/Board.svelte';
  import CreateArticle from './routes/board/CreateArticle.svelte';
  import ArticleDetail from './routes/board/ArticleDetail.svelte';

  const routes = {
    '/':Home,
    '/detail/:video_id':Detail,
    '/sign_up':SignUp,
    '/user-login':Login,
    '/change-password':ChangePassword,
    '/find-id':FindId,
    '/validate':validate,
    '/sign_out':SignOut,
    '/board':Board,
    '/board/create':CreateArticle,
    '/board/detail/:article_id':ArticleDetail,
  }
</script>

<Router {routes}/>