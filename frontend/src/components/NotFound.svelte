<script>
 import { link, push } from "svelte-spa-router";
 import { keyword } from "../lib/store";
 import { Button } from "flowbite-svelte";

 function setKeyword(){
    $keyword = ''
    push('/')
 }
</script>

<section class="page_404">
	<div class="d">
		<div class="row">	
		<div class="col-sm-12 ">
		<div class="col-sm-10 col-sm-offset-1  text-center">
		<div class="four_zero_four_bg">
    </div>
		
		<div class="contant_box_404">
            <h3 class="h2">
            찾으시는 컨텐츠가 없어요 T.T
            </h3>
            
            <p>더 많은 자료를 준비하기 위해 노력하는 중입니다..!</p>
		
		    <Button on:click={setKeyword}>메인페이지로</Button>
        </div>
		</div>
		</div>
		</div>
	</div>
</section>
<style>
    
.page_404{ padding:40px 0; background:#fff; font-family: 'Arvo', serif;
}

.four_zero_four_bg{
 
 background-image: url(https://cdn.dribbble.com/users/285475/screenshots/2083086/dribbble_1.gif);
    height: 400px;
    background-position: center;
}

.link_404{			 
    color: #fff!important;
    padding: 10px 20px;
    background: #39ac31;
    margin: 20px 0;
    display: inline-block;
}
.contant_box_404{ margin-top:-50px;}
</style>