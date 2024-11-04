<script>
    // Components
    import Hero from "$lib/components/Hero.svelte";

    export let data;
    let page = data.about;
    let settings = data.settings
</script>


<Hero src="https://picsum.photos/200/300" heading="Zgodba">
    <div class="h-full w-full text-textSecondary" slot="content">
            {@html page.story}
    </div>
</Hero>