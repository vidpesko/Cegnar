<script>
    // Images
    import HeroVideo from "$lib/static/videos/cegnar-movie-small.mp4";
    import HandleImg from "$lib/static/images/handle3.png";
    import BladeImg from "$lib/static/images/blade.png";
    import WoodTextureImg from "$lib/static/images/texture3.jpg";
    import MyImg from "$lib/static/images/about2.jpg";
    import FireImg from "$lib/static/images/fire-texture2.jpg";
    // Icons
    import RightArrow from '~icons/material-symbols/arrow-forward-rounded'
    import IGIcon from '~icons/mdi/instagram';
    import FacebookIcon from '~icons/mdi/facebook-box';
    import EmailIcon from '~icons/mdi/email';
    // Components
    import FeatureCard from "$lib/components/FeatureCard.svelte";
    import GalleryImage from "$lib/components/GalleryImage.svelte";
    import Navbar from "$lib/components/Navbar.svelte";
    import HeroNavbar from "$lib/components/HeroNavbar.svelte";
    // Image slider
    import { Splide, SplideSlide } from '@splidejs/svelte-splide';
    // Other
    import { onMount } from "svelte";

    export let data;
    $: home = data.home;
    $: gallery = data.gallery;
    $: settings = data.settings;

    // Navbar logic
    let showNavbar = false;
    onMount(() => {
        // When on hero section hide navbar, when scrolled past hero section, show it
        let windowHeight = window.innerHeight;
        window.addEventListener("scroll", () => {
            let scrollPosition = window.scrollY;

            if (scrollPosition > windowHeight) {
                showNavbar = true;
            } else {
                showNavbar = false;
            }
        });
    });
</script>

<svelte:head>
    <title>{home.title}</title>
</svelte:head>

<!-- Navbar -->
<Navbar showNavbarOnInnit={showNavbar} />

<!-- Hero section -->
<section class="xl:h-screen bg-background md:p-4 p-2 flex xl:flex-row flex-col gap-4">
    <!-- Main image / video -->
    <div class="hero-main w-full xl:h-full md:h-[600px] rounded-2xl xl:basis-[70%] h-[80vh] shrink grow relative">
        <!-- Hero background video -->
        <video class="absolute w-full h-full object-cover rounded-2xl md:opacity-60 opacity-40 z-0" src={HeroVideo} loop autoplay muted playsinline>
            Your browser does not support video tag
        </video>

        <!-- Hero navbar -->
        <HeroNavbar logo={settings.logo.full_url} />

        <!-- Hero title -->
        <div class="absolute md:bottom-10 md:left-10 md:translate-x-0 md:translate-y-0 bottom-1/2 left-1/2 -translate-x-1/2 translate-y-1/2 md:w-full w-5/6 xl:text-start text-center">
            <h1 class="text-textPrimary md:text-8xl text-5xl font-heading">{@html home.heading}</h1>
            {#if home.hero_small_text}
            <p class="text-textSecondary text-lg">{home.hero_small_text}</p>
            {/if}
        </div>

        <!-- Social -->
        <div class="absolute bottom-0 right-0 bg-background pt-2 px-2 rounded-tl-xl">
            <ul class="text-white text-2xl flex gap-1">
                <li><a href={settings.instagram_url}><IGIcon /></a></li>
                <li><a href={settings.facebook_url}><FacebookIcon /></a></li>
                <li><a href="mailto:{settings.email}"><EmailIcon /></a></li>
            </ul>
        </div>
    </div>

    <!-- Links / "sidebar" -->
    <div class="flex xl:flex-col lg:max-xl:h-[180px] md:max-lg:h-[150px] xl:basis-[20%] gap-4 xl:shrink-0 xl:grow-0 2x xl:max-w-[300px] 2xl:max-w-[500px]">
        {#each home.hero_sidebar_links as link}
        <a href={link.destination} style="background-image: url('{link.image.full_url}');" class="hero-link bg-no-repeat bg-background bg-center bg-cover">
            <!-- Large screen sidebar link -->
            <div>
                <div>
                    {link.label}
                    <span>
                        <RightArrow />
                    </span>
                </div>
            </div>
            <!-- Mobile screen sidebar link -->
            <div class="bg-background">
                {link.label}
                <RightArrow class="text-lg" />
            </div>
        </a>
        {/each}
    </div>
</section>

<!-- CTA -->
<section class="py-16">
    <div class="md:w-4/6 w-5/6 mx-auto text-center">
        <h1 class="heading-underline">{home.cta_title}</h1>
        <p class="text-center mb-6">{@html home.cta_small_text}</p>
        <a href="/kontakt" class="btn btn-dark">{home.cta_btn_text}</a>
    </div>
</section>

<!-- Features -->
<section class="bg-background py-28">
    <!-- Cards -->
    <div class="md:mx-20 mx-2 2xl:mx-auto 2xl:w-3/4">
        {#each home.home_page_feature_card as card, i}
        <FeatureCard knifeImg={card.knife_image.full_url} textureImg={WoodTextureImg} heading={card.heading} description={card.description} buttonText={card.btn_label} flipped={Math.abs(i % 2) == 1}/>
        {/each}
    </div>
</section>

<!-- Gallery showcase -->
<section class="bg-background md:px-28 pb-20">
    <div class="">
        <!-- Title & description & show more btn -->
        <div class="text-center text-textSecondary mb-6">
            <h1 class="font-heading text-4xl text-textPrimary mb-1">{home.gallery_title}</h1>
            <p class="mb-8">{@html home.gallery_description}</p>
            <a href="/galerija" class="btn">{home.gallery_btn_label}</a>
        </div>

        <!-- Image slider -->
        <Splide class="md:px-0 px-6" aria-label="My Favorite Images" options={{
            perPage: 4,
            gap: "1em",
            autoWidth: true,
            height: "300px",
            breakpoints: {
                768: {
                    perPage: 1,
                }
            }
        }}>
            {#each gallery as image}
            <SplideSlide>
                <GalleryImage url={image.image.full_url} model={image.knife_model} description={image.image_description} />
            </SplideSlide>
            {/each}
        </Splide>
    </div>
</section>

<!-- About me -->
<section class="bg-background py-20 bg-contain bg-no-repeat bg-center" style="background-image: linear-gradient(0deg, rgba(0,0,0,0.8) 0%, rgba(0,0,0,0.8) 100%), url({FireImg});">
    <div class="flex md:flex-row flex-col md:px-28 px-10 md:justify-center items-center gap-8 md:text-start text-center">
        <!-- My image -->
        <img src={home.about_image.full_url} alt="Jaz" class="md:h-full h-80">

        <!-- About me text -->
        <div class="text-textSecondary md:w-3/6 my-auto">
            <div class="">
                <h2 class="font-heading text-4xl text-textPrimary">Moja zgodba</h2>
                <p class="mb-10">{@html home.about_description}</p>
                <a href="/zgodba" class="btn">Izvedi vec</a>
            </div>
        </div>
    </div>
</section>

<!-- Instagram posts -->
<section class="bg-white h-[50vh] text-center">
    <h1>Zadnje objave</h1>
</section>