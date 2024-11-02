<script>
    // Components
    import HeroNavbar from "./HeroNavbar.svelte";

    export let src;
    export let heading;
    export let smallText;
</script>


<div class="pb-10 bg-background">
    <div class="w-full h-screen flex p-4 gap-4 bg-background">
        <!-- Main image -->
        <div class="w-[40%] h-full">
            <div class="hero-main w-full h-full rounded-2xl relative">
                <!-- Hero background video -->
                <img class="absolute w-full h-full object-cover rounded-2xl md:opacity-60 opacity-40 z-0" {src} alt="Hero" />
                
                <!-- Hero navbar -->
                <HeroNavbar />
                
                <!-- Hero title -->
                <div class="absolute md:bottom-10 w-full bottom-1/2 left-1/2 -translate-x-1/2 translate-y-1/2 text-start">
                    <h1 class="text-textPrimary md:text-7xl text-5xl font-heading">{@html heading}</h1>
                    {#if smallText}
                    <p class="text-textSecondary text-lg">{smallText}</p>
                    {/if}
                </div>
            </div>
        </div>
        <!-- Data -->
        <div class="w-[60%]">
            <slot name="content"></slot>
        </div>
    </div>
</div>