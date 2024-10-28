<script>
    // Components
    import GalleryImage from "$lib/components/GalleryImage.svelte";
    import SiteHeader from "$lib/components/SiteHeader.svelte";
</script>

<SiteHeader site="galerija" />

<section id="gallery" class="min-h-screen py-10">
    <div class="h-full w-5/6 mx-auto flex flex-wrap" style="grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));">
        <div class="column">
            {#each Array(10) as _}
            <GalleryImage url="https://picsum.photos/500/300" />
            {/each}
        </div>
        <div class="column">
            {#each Array(10) as _}
            <GalleryImage url="https://picsum.photos/500/300" />
            {/each}
        </div>
        <div class="column">
            {#each Array(10) as _}
            <GalleryImage url="https://picsum.photos/500/300" />
            {/each}
        </div>
    </div>
</section>