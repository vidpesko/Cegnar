<script>
    // Components
    import Hero from "$lib/components/Hero.svelte";

    export let data;
    let page = data.page;
    let settings = data.settings
</script>

<svelte:head>
    <title>{page.title}</title>
</svelte:head>

<Hero src={page.hero_image.full_url} heading={page.heading}>
    <div class="h-full w-full text-textSecondary" slot="content">
        {@html page.story}
    </div>
</Hero>
