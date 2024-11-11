<script>
    import { goto } from '$app/navigation';

    export let url;
    export let productId;
    export let name;
    export let model;
    export let description;
    export let fullHeight = true
    export let openModal;
</script>

<div class:h-full={fullHeight} class="relative w-full overflow-hidden">
    <img src={url} alt="" class="w-full object-center object-cover h-full max-h-[30rem] rounded">

    {#if model}
    <!-- svelte-ignore a11y_click_events_have_key_events -->
    <!-- svelte-ignore a11y_no_static_element_interactions -->
    <div on:click={() => openModal(productId)} class="cursor-pointer text-white absolute z-10 bottom-0 h-full w-full bg-opacity-70 text-center py-4 opacity-0" style="background: linear-gradient(180deg, rgba(0,0,0,0) 20%, rgba(0,0,0,0.8) 50%);">
        <div class="absolute bottom-[10%] text-center w-full">
            <h4 class="text-xl font-bold mb-2">{name}</h4>
            <p class="mb-8">{@html description}</p>
            <a href="/kontakt?izdelek={productId}" class="btn py-4 hidden md:inline-block">Naroci tak noz</a>
        </div>
    </div>
    {/if}
</div>

<style>
    div:hover > div:first-of-type {
        @apply md:block md:opacity-100 transition duration-300;
    }
</style>