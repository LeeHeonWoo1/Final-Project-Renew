<script>
  import Router from 'svelte-spa-router'
  import Home from './routes/Home.svelte'
  import SignUp from './routes/sign_up.svelte';
  import Login from './routes/Login.svelte';

  const routes = {
    '/':Home,
    '/sign_up':SignUp,
    '/user-login':Login,
  }
</script>

<Router {routes}/>