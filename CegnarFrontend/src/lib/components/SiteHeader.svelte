<script>
    // Components
    import HeroNavbar from "./HeroNavbar.svelte";

    export let data;
    $: settings = data.settings;

    export let src;
    export let heading;
    export let intro;
</script>


<div class="md:h-[50vh] h-[30vh] relative p-4 bg-background">
    <!-- Hero image -->
    <img {src} alt="Slika galerije" class="w-full h-full object-cover rounded-2xl opacity-70">

    <!-- Hero navbar -->
    <HeroNavbar logo={settings.logo.full_url} additionalClasses="absolute top-8 left-1/2 -translate-x-1/2 xl:left-1/2 xl:translate-x-[-50%] xl:ms-[0px] xl:mt-[0px]" />

    <div class="absolute top-1/2 left-1/2 -translate-x-1/2 md:translate-y-0 translate-y-0 text-textSecondary text-center">
        <h1 class="text-textPrimary md:text-6xl text-4xl uppercase font-heading">{heading}</h1>
        <p>{intro}</p>
    </div>
</div>