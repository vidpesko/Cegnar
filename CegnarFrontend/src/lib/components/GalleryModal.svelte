<script>
    // Image slider
    import { Splide, SplideSlide } from '@splidejs/svelte-splide';
    // Icons
    import CloseIcon from '~icons/material-symbols/cancel-outline-rounded';

    export let images;
    export let model;
    export let description;
    export let closeModal;
</script>


<div class="fixed left-0 w-full top-0 h-dvh p-10 z-30 bg-background bg-opacity-90">
    <!-- Close btn -->
    <button class="text-white text-3xl absolute right-8 top-5" on:click={closeModal}>
        <CloseIcon />
    </button>
    <!-- Content -->
    <div class="flex flex-col md:flex-row md:gap-8 gap-4 items-center md:justify-center justify-evenly h-full">
        <!-- Images -->
        {#if images.length > 1}
        <Splide class="md:px-0 px-6 md:h-full md:w-1/2 h-1/2" aria-label="My Favorite Images" options={{
            perPage: 1,
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
            {#each images as image}
            <SplideSlide class="flex items-center justify-center rounded-2xl overflow-hidden">
                <img src={image.full_image.full_url} alt={image.full_image.alt} class="mx-auto rounded-2xl" />
            </SplideSlide>
            {/each}
        </Splide>
        {:else}
        <img src={images[0].full_image.full_url} alt={images[0].full_image.alt} class="mx-auto rounded-2xl md:max-h-full max-h-[50vh]" />
        {/if}
        <!-- <img {src} alt="" class="rounded-2xl h-full"> -->
        <!-- Text -->
        <div class="text-white md:text-start text-center">
            <h2 class="text-textPrimary font-heading text-5xl">{model}</h2>
            <p class="text-lg mb-10">{@html description}</p>
            <a href="/kontakt?izdelek={model}" class="btn">Naroci tak noz</a>
        </div>
    </div>
</div>