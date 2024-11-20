<script>
    // Components
    import Hero from "$lib/components/Hero.svelte";
    import NavigationMenu from "$lib/components/NavigationMenu.svelte";
    // Icons
    import MdiCalendarBlankMultiple from '~icons/mdi/calendar-blank-multiple';
    import MdiKnife from '~icons/mdi/knife';
    import MdiClock from '~icons/mdi/clock';
    const icons = [MdiCalendarBlankMultiple, MdiKnife, MdiClock];

    export let data;
    $: page = data.page;
    $: settings = data.settings

    // Handle navigation menu
    let menuOpened = false;

    function openNavigationMenu() {
        document.body.style.overflow = "hidden";
        menuOpened = true;
    }

    function closeNavigationMenu() {
        document.body.style.overflow = "auto";
        menuOpened = false;
    }
</script>

<svelte:head>
    <title>{page.title} - {page.meta.parent.title}</title>
</svelte:head>

<!-- Menu modal -->
{#if menuOpened}
<NavigationMenu bind:menuOpened {closeNavigationMenu} />
{/if}

<Hero src={page.hero_image.full_url} heading={page.heading} {openNavigationMenu} {data}>
    <div class="h-full w-full text-textSecondary py-8 md:px-8 px-4 story-page-styling overflow-hidden" slot="content">
        <!-- Heading -->
        <h1 class="text-center font-heading text-3xl md:text-5xl text-textPrimary">{page.intro_heading}</h1>

        <!-- Intro -->
        <div class="text-center mt-4">
            {@html page.intro_text}
        </div>

        <!-- Facts section -->
        <div class="md:w-3/4 w-full mx-auto mt-10 flex md:gap-6 gap-2">
            {#each page.about_me_fact as fact, i}
            <div class="w-full border-custom text-center rounded-2xl px-2 py-6 flex flex-col  hover:border-textPrimary transition duration-200 hover:text-textPrimary">
                <svelte:component this={icons[i]} class="mx-auto mb-2 text-2xl" />
                <!-- Fact heading -->
                <p class="text-2xl font-sans font-bold mb-1">{fact.title}</p>
                <!-- Fact description -->
                <p>{fact.description}</p>
            </div>
            {/each}
        </div>

        <!-- Story -->
        <div class="mt-10">
            {@html page.story}
        </div>
    </div>
</Hero>
