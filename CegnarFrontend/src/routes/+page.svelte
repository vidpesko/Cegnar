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
    import CloseToMenuIcon from '~icons/line-md/close-to-menu-alt-transition'
    // Components
    import FeatureCard from "$lib/components/FeatureCard.svelte";
    import GalleryImage from "$lib/components/GalleryImage.svelte";
    // Image slider
    import { Splide, SplideSlide } from '@splidejs/svelte-splide';

    export let data;
    const home = data.home;
    const gallery = data.gallery;
</script>

<!-- Hero section -->
<section class="xl:h-screen bg-background md:p-4 p-2 flex xl:flex-row flex-col gap-4">
    <!-- Main image / video -->
    <div class="hero-main w-full xl:h-full md:h-[600px] rounded-2xl xl:basis-[70%] h-[80vh] shrink grow relative">
        <!-- Hero background video -->
        <video class="absolute w-full h-full object-cover rounded-2xl md:opacity-60 opacity-40 z-0" src={HeroVideo} loop autoplay muted>
            Your browser does not support video tag
        </video>

        <!-- Hero navbar -->
        <div class="xl:ms-10 xl:mt-10 mt-4 xl:left-0 xl:translate-x-0 left-1/2 -translate-x-1/2 z-20 absolute">
            <div class="flex md:gap-10 md:justify-between justify-center items-center bg-background rounded-lg p-4 gap-4">
                <!-- Menu -->
                <div class="text-textPrimary font-2xl border-[0.5px] p-1 rounded md:hidden">
                    <CloseToMenuIcon />
                </div>

                <!-- Logo -->
                <p class="text-white text-2xl">C</p>

                <!-- Links -->
                <ul class="md:inline-flex items-center gap-4 textPrimary hidden">
                    <li class="hero-navbar-link">Galerija</li>
                    <li class="hero-navbar-link">Zgodba</li>
                    <li class="hero-navbar-link"><a href="/kontakt" class="border rounded p-2">Kontakt</a></li>
                </ul>
                <div class="hero-navbar-link md:hidden">
                    <a href="/kontakt" class="border rounded p-2">Kontakt</a>
                </div>
            </div>
        </div>

        <!-- Hero title -->
        <div class="absolute md:bottom-10 md:left-10 md:translate-x-0 md:translate-y-0 bottom-1/2 left-1/2 -translate-x-1/2 translate-y-1/2 md:w-full w-5/6 xl:text-start text-center">
            <h1 class="text-textPrimary md:text-8xl text-5xl font-heading">{@html home.heading}</h1>
            <p class="text-textSecondary text-lg">{home.hero_small_text}</p>
        </div>

        <!-- Social -->
        <div class="absolute bottom-0 right-0 bg-background pt-2 px-2 rounded-tl-xl">
            <ul class="text-white text-2xl flex gap-1">
                <li><a href="https://www.instagram.com/cegnarblacksmithing/"><IGIcon /></a></li>
                <li><a href="/"><FacebookIcon /></a></li>
                <li><a href="/"><EmailIcon /></a></li>
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
    <div class="w-4/6 mx-auto text-center">
        <h1 class="text-background text-2xl font-heading text-center relative pb-2 mb-4 after:content-[''] after:bg-textPrimary after:w-10 after:h-2 after:absolute after:bottom-0 after:left-1/2 after:-translate-x-1/2 after:rounded">{home.cta_title}</h1>
        <p class="text-center mb-6">{@html home.cta_small_text}</p>
        <a href="/kontakt" class="btn btn-dark">{home.cta_btn_text}</a>
    </div>
</section>

<!-- Features -->
<section class="bg-background py-28">
    <!-- Cards -->
    <div class="mx-20">
        {#each home.home_page_feature_card as card, i}
        <FeatureCard knifeImg={card.knife_image.full_url} textureImg={WoodTextureImg} heading={card.heading} description={card.description} buttonText={card.btn_label} flipped={Math.abs(i % 2) == 1}/>
        {/each}
    </div>
</section>

<!-- Gallery showcase -->
<section class="bg-background px-28 pb-20">
    <div class="">
        <!-- Title & description & show more btn -->
        <div class="flex flex-col items-center text-textSecondary gap-2 mb-6">
            <h1 class="font-heading text-4xl text-textPrimary">{home.gallery_title}</h1>
            <p class="mb-2">{@html home.gallery_description}</p>
            <a href="/galerija" class="btn">{home.gallery_btn_label}</a>
        </div>

        <!-- Image slider -->
        <Splide aria-label="My Favorite Images" options={{
            perPage: 3,
            gap: "1em",
            autoWidth: true,
            height: "300px"
        }}>
            {#each gallery.gallery_images as image}
            <SplideSlide>
                <GalleryImage url={image.image.full_url} model={image.knife_model} description={image.image_description} />
            </SplideSlide>
            {/each}
        </Splide>
    </div>
</section>

<!-- About me -->
<section class="bg-background py-20 bg-contain bg-no-repeat bg-center" style="background-image: linear-gradient(0deg, rgba(0,0,0,0.8) 0%, rgba(0,0,0,0.8) 100%), url({FireImg});">
    <div class="md:flex md:px-28 px-10 md:justify-center gap-8">
        <!-- My image -->
        <img src={home.about_image.full_url} alt="Jaz">

        <!-- About me text -->
        <div class="text-textSecondary w-3/6 flex items-center">
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