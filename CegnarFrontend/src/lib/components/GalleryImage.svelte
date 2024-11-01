<script>
    export let url;
    export let model;
    export let description = "";
    export let fullHeight = true
</script>

<div class:h-full={fullHeight} class="relative w-full">
    <img src={url} alt="" class="w-full h-full object-center">

    <div class="text-white absolute z-10 bottom-0 h-full w-full bg-opacity-70 text-center py-4 opacity-0" style="background: linear-gradient(180deg, rgba(0,0,0,0) 20%, rgba(0,0,0,0.8) 50%);">
        <div class="absolute bottom-4 text-center w-full">
            <h4 class="text-xl font-bold">{model}</h4>
            
            <p class="mb-8">Rocno kovan loski noz</p>
            <a href="/" class="btn py-2">Poglej <b>"{model}"</b></a>
        </div>
    </div>
</div>

<style>
    div:hover > div:first-of-type {
        @apply block opacity-100 transition-all duration-300;
    }
</style>