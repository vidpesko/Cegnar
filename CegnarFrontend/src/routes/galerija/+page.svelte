<script>
    // Components
    import GalleryImage from "$lib/components/GalleryImage.svelte";
    import SiteHeader from "$lib/components/SiteHeader.svelte";

    export let data;
    $: page = data.page;
    $: categories = data.categories;
</script>


<svelte:head>
    <title>{page.title}</title>
</svelte:head>

<!-- Hero section -->
<SiteHeader src={page.hero_image.full_url} heading={page.heading} {data} />

<!-- Content -->
<section id="gallery" class="mt-10 px-10">
    <!-- Filters -->
    <h3 class="text-lg font-semibold mb-2">Izberite kategorijo:</h3>
    <div class="w-full flex gap-4 pb-4 mb-6 border-b-custom">
        {#each categories as category}
        <div class="p-4 border-custom rounded-2xl text-black uppercase text-xl bg-textPrimary">
            {category.name}
        </div>
        {/each}
    </div>

    <!-- Grid -->
    <div class="flex flex-wrap mb-10">
        {#each Array(3) as _, i}
        <div class="column">
            {#each page.gallery_images.slice(i).filter((_, index) => index % 3 === 0) as product}
            <GalleryImage fullHeight={false} url={product.image.full_url} model={product.category.name} description={product.image_description} />
            {/each}
        </div>
        {/each}
    </div>
</section>