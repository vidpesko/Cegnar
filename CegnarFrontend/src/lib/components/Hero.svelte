<script>
    // Components
    import HeroNavbar from "./HeroNavbar.svelte";

    export let data;
    $: settings = data.settings;

    export let src;
    export let heading;
    export let smallText;
</script>


<div class="pb-10 bg-background overscroll-auto">
    <div class="w-full h-full flex lg:flex-row flex-col p-4 gap-4 bg-background">
        <!-- Main image -->
        <div class="lg:w-[40%] h-full">
            <div class="hero-main w-full lg:h-[calc(100vh-2rem)] h-[40vh] rounded-2xl relative">
                <!-- Hero background video -->
                <img class="absolute w-full h-full object-cover rounded-2xl md:opacity-60 opacity-40 z-0" {src} alt="Hero" />
                
                <!-- Hero navbar -->
                <HeroNavbar logo={settings.logo.full_url} additionalClasses="lg:ms-5 lg:mt-10 lg:left-0 lg:translate-x-0" />
                
                <!-- Hero title -->
                <div class="absolute lg:bottom-10 lg:left-10 lg:translate-y-0 lg:translate-x-0 w-full bottom-1/3 left-1/2 -translate-x-1/2 translate-y-1/2 lg:text-start text-center">
                    <h1 class="text-textPrimary lg:text-5xl xl:text-7xl md:text-7xl text-5xl font-heading">{@html heading}</h1>
                    {#if smallText}
                    <p class="text-textSecondary text-lg">{smallText}</p>
                    {/if}
                </div>
            </div>
        </div>
        <!-- Data -->
        <div class="lg:w-[60%]">
            <slot name="content"></slot>
        </div>
    </div>
</div>