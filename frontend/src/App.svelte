<script>
  import Router from 'svelte-spa-router'
  import Home from './routes/Home.svelte'
  import SignUp from './routes/sign_up.svelte';
  import Login from './routes/Login.svelte';
  import FindPassword from './routes/FindPassword.svelte';
  import FindId from './routes/FindID.svelte';

  const routes = {
    '/':Home,
    '/sign_up':SignUp,
    '/user-login':Login,
    '/change-password':FindPassword,
    '/find-id':FindId,
  }
</script>

<Router {routes}/>