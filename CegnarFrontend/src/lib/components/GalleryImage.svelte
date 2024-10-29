<script>
    export let url;
    export let model;
    export let description = "";
</script>

<div class="relative h-full w-full">
    <img src={url} alt="" class="w-full h-full object-center">

    <div class="text-white absolute z-10 bottom-0 h-full w-full bg-opacity-70 text-center py-4 hidden" style="background: linear-gradient(180deg, rgba(0,0,0,0) 20%, rgba(0,0,0,0.8) 50%);">
        <div class="absolute bottom-4 text-center w-full">
            <h4 class="text-xl font-bold">{model}</h4>
            <p class="mb-8">Rocno kovan loski noz</p>
            <a href="/" class="btn py-2">Poglej <b>"{model}"</b></a>
        </div>
    </div>
</div>

<style>
    div:hover > div {
        @apply block;
    }
</style>