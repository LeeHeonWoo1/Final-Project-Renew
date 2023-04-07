<script>
  import Router from 'svelte-spa-router'
  import Home from './routes/Home.svelte'
  import SignUp from './routes/sign_up.svelte';
  import Login from './routes/Login.svelte';
  import ChangePassword from './routes/ChangePassword.svelte';
  import FindId from './routes/FindID.svelte';
  import validate from './routes/valid/validate.svelte'
  import SignOut from './routes/SignOut.svelte';

  const routes = {
    '/':Home,
    '/sign_up':SignUp,
    '/user-login':Login,
    '/change-password':ChangePassword,
    '/find-id':FindId,
    '/validate':validate,
    '/sign_out':SignOut,
  }
</script>

<Router {routes}/>