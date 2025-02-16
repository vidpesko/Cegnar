<script>
    // Icons
    import CloseIcon from '~icons/mdi/close-circle-outline';
    // Components
    import GalleryImage from "$lib/components/GalleryImage.svelte";
    import SiteHeader from "$lib/components/SiteHeader.svelte";
    import GalleryModal from "$lib/components/GalleryModal.svelte";
    // API client
    import { getGallery } from "$lib/api/client";
    // Other
    import { page } from '$app/stores';

    export let data;
    $: pageData = data.page;
    $: gallery = data.gallery
    $: categories = data.categories;

    let categoryFilter = $page.url.searchParams.get("kategorija") || "";
    let galleryColumns = 3; // How many columns in row

    // Set columns per page based on browser width
    let browserWidth;
    $: if (browserWidth < 768) {
        galleryColumns = 2;
    } else {
        galleryColumns = 3;
    }


    async function filterProducts(category) {
        // If category is already selected, remove filter
        if (category === categoryFilter) {
            category = null;
        }
        // Fetch product with category
        if (category) {
            gallery = getGallery({category});
            categoryFilter = category;
        } else {
            gallery = getGallery({onlyImg: true});
            categoryFilter = "";
        }

        // Set url params
        const url = new URL(window.location.href);
        if (category) {
            // Set or update the 'category' parameter
            url.searchParams.set('kategorija', category);
        } else {
            // Delete param
            url.searchParams.delete('kategorija');
        }
        // Update the URL in the browser without reloading the page
        window.history.pushState({}, '', url);
    }

    // Open fullscreen modal
    let modalInfo = null;

    function openModal(product) {
        modalInfo = product;
        // Prevent scrolling
        document.body.style.overflow = "hidden";
    }

    function closeModal() {
        modalInfo = null;
        document.body.style.overflow = "";
    }
</script>

<!-- Bind to browser width -->
<svelte:window bind:innerWidth={browserWidth} />

<!-- Set title -->
<svelte:head>
    <title>{pageData.title}</title>
</svelte:head>

<!-- Fullscreen image modal -->
{#if modalInfo}
<GalleryModal product={modalInfo} {closeModal} />
{/if}

<!-- Hero section -->
<SiteHeader src={pageData.hero_image.full_url} heading={pageData.heading} intro={pageData.small_text} {data} />

<!-- Content -->
<section id="gallery" class="mt-10 px-4 md:px-10 max-w-[100rem] mx-auto">
    <!-- Filters -->
    <h3 class="text-lg font-semibold mb-2">Izberite kategorijo:</h3>
    <div class="w-full flex gap-4 justify-between pb-4 mb-6 border-b-custom">
        <!-- Filters -->
        <div class="flex gap-4">
            {#each categories as category}
            <button class:bg-textPrimary={categoryFilter == category.name} on:click={() => filterProducts(category.name)} class="p-3 border border-stone-400 rounded-2xl text-black hover:bg-stone-200 transition duration-200">
                {category.name}
            </button>
            {/each}
        </div>

        {#if categoryFilter}
        <!-- Remove Filters -->
        <button class="flex items-center gap-2 border border-stone-400 p-3 rounded-2xl" on:click={() => filterProducts(null)}>
            <CloseIcon class="text-2xl text-black" />
            Odstrani filtre
        </button>
        {/if}
    </div>

    <!-- Grid -->
    <!-- <div class="flex flex-wrap mb-10">
        {#key categoryFilter}
        {#await gallery}
            ...nalagam
        {:then gallery_images} 
            {#each Array(galleryColumns) as _, i}
            <div class="column last-of-type:pe-0 pe-2 w-1/2 flex-[50%] md:flex-[calc(100%_/_3)] md:max-w-[calc(100%_/_3)]">
                {#each gallery_images.slice(i).filter((_, index) => index % galleryColumns === 0) as product}
                <GalleryImage fullHeight={false} {product} {openModal} />
                {/each}
            </div>
            {/each}
        {/await}
        {/key}
    </div> -->
</section>