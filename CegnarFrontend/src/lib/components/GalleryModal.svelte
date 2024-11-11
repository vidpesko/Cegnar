<script>
    // Api
    import { getSpecificProduct } from "$lib/api/client";
    // Image slider
    import { Splide, SplideSlide } from '@splidejs/svelte-splide';
    // Icons
    import CloseIcon from '~icons/material-symbols/cancel-outline-rounded';
    // Other
    import { onMount } from "svelte";

    export let productId;
    export let closeModal;
    let dataPromise;

    onMount(() => {
        dataPromise = getSpecificProduct(productId);
        
        return closeModal;
    });
</script>


{#await dataPromise}
    ...nalagam
{:then data}
<div class="fixed left-0 w-full top-0 h-dvh p-10 z-30 bg-background bg-opacity-90">
    <!-- Close btn -->
    <button class="text-white text-3xl absolute right-8 top-5" on:click={closeModal}>
        <CloseIcon />
    </button>

    <!-- Content -->
    <div class="flex flex-col md:flex-row md:gap-8 gap-4 items-center md:justify-center justify-evenly h-full">
        <!-- Images -->
        <!-- {#if data.image.length > 1} -->
        <Splide class="md:px-0 px-6 md:h-full md:w-1/2 h-1/2" aria-label="My Favorite Images" options={{
            perPage: 1,
            arrows: data.image.length > 1,
            gap: "1em",
            height: "80vh",
            breakpoints: {
                768: {
                    // autoWidth: true,
                    autoHeight: true,
                    height: "50vh",
                }
            }
        }}>
            {#each data.image as image}
            <SplideSlide class="flex items-center justify-center rounded-2xl overflow-hidden">
                <img src={image.full_image.full_url} alt={image.full_image.alt} class="mx-auto rounded-2xl" />
            </SplideSlide>
            {/each}
        </Splide>
        <!-- {:else}
        <img src={data.image[0].full_image.full_url} alt={data.image[0].full_image.alt} class="mx-auto rounded-2xl md:max-h-full max-h-[50vh]" />
        {/if} -->

        <!-- Text -->
        <div class="text-white md:text-start text-center">
            <h2 class="text-textPrimary font-heading text-5xl">{data.name}</h2>
            <p class="text-lg mb-10">{@html data.description}</p>
            <a href="/kontakt?izdelek={productId}" class="btn">Naroci tak noz</a>
        </div>
    </div>
</div>
{/await}