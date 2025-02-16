<script>
    // Image slider
    import { Splide, SplideSlide } from '@splidejs/svelte-splide';
    // Icons
    import CloseIcon from '~icons/material-symbols/cancel-outline-rounded';
    import missing from "../static/images/missing.png";

    export let product;
    export let closeModal;
</script>


<div class="fixed left-0 w-full top-0 h-dvh md:p-10 py-10 z-30 bg-background bg-opacity-90">
    <!-- Close btn -->
    <button class="text-white text-3xl absolute md:right-8 md:top-5 right-4 top-4" on:click={closeModal}>
        <CloseIcon />
    </button>

    <!-- Content -->
    <div class="flex flex-col md:flex-row md:gap-8 gap-4 items-center md:justify-center justify-evenly h-full">
        <!-- Images -->
        <Splide class="md:px-0 px-6 md:h-full md:w-1/2 h-1/2 w-full mt-10" aria-label="My Favorite Images" options={{
            perPage: 1,
            arrows: product.image.length > 1,
            gap: "1em",
            height: "100%",
            height: "calc(100vh - 5rem)",
            breakpoints: {
                768: {
                    // autoWidth: true,
                    autoHeight: true,
                    height: "calc(50vh - 5rem)",
                }
            }
        }}>
            {#if product.image.length !== 0}
            {#each product.image as image}
            <SplideSlide class="flex items-center justify-center rounded-lg h-full">
                <img src={image.full_image.full_url} alt={image.full_image.alt} class="mx-auto rounded-lg my-auto max-h-full" />
            </SplideSlide>
            {/each}
            {:else}
            <SplideSlide class="flex items-center justify-center rounded-2xl overflow-hidden">
                <img src={missing} alt="" class="mx-auto rounded-xl">
            </SplideSlide>
            {/if}
        </Splide>

        <!-- Text -->
        <div class="text-white md:text-start text-center flex flex-col justify-center md:w-1/2 md:h-full w-full h-1/2 px-2 md:px-0">
            <div class="">
                <h2 class="text-textPrimary font-heading text-4xl md:text-5xl">{product.name}</h2>
                <p class="text-lg mb-10">{@html product.image_description}</p>
                <a href="/kontakt?izdelek={product.id}" data-sveltekit-reload class="btn">Naroci tak noz</a>
            </div>
        </div>
    </div>
</div>