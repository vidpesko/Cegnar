<script>
    // Images
    import HeroImg from "$lib/static/images/hero1.jpg";
    import HandleImg from "$lib/static/images/handle3.png";
    import BladeImg from "$lib/static/images/blade.png";
    import WoodTextureImg from "$lib/static/images/texture3.jpg";
    import MyImg from "$lib/static/images/about2.jpg";
    import FireImg from "$lib/static/images/fire-texture2.jpg";
    // Icons
    import RightArrow from '~icons/material-symbols-light/arrow-circle-right-outline-rounded';
    import IGIcon from '~icons/mdi/instagram';
    import FacebookIcon from '~icons/mdi/facebook-box';
    import EmailIcon from '~icons/mdi/email';
    // Components
    import FeatureCard from "$lib/components/FeatureCard.svelte";
    // Image slider
    import { Splide, SplideSlide } from '@splidejs/svelte-splide';
</script>

<!-- Hero section -->
<section class="xl:h-screen bg-background p-6 flex xl:flex-row flex-col gap-4">
    <!-- Main image / video -->
    <div class="hero-main w-full xl:h-full lg:h-[600px] rounded-2xl xl:basis-[70%] shrink grow bg-center relative" style="background-image: linear-gradient(0deg, rgba(0,0,0,0.7) 0%, rgba(255,255,255,0) 59%), url('{HeroImg}');">
        <!-- Hero navbar -->
        <div class="flex xl:justify-start xl:ms-10 xl:mt-10 lg:mt-4 lg:justify-center">
            <div class="inline-flex justify-center bg-background rounded-lg p-4 gap-4">
                <!-- Menu -->
                <div class="text-textPrimary font-2xl">
                    X
                </div>

                <!-- Logo -->
                <img src="https://framerusercontent.com/images/x0JzSofUJm2jTIMMg5jbgdRYVzU.webp" width="110px" class="object-contain" alt="logo">

                <!-- Links -->
                <ul class="inline-flex items-center gap-4 textPrimary">
                    <li class="hero-navbar-link">Galerija</li>
                    <li class="hero-navbar-link">Zgodba</li>
                    <li class="hero-navbar-link"><a href="/kontakt" class="border rounded p-2">Kontakt</a></li>
                </ul>
            </div>
        </div>
        
        <!-- Hero title -->
        <div class="absolute bottom-10 left-10 w-full xl:text-start text-center">
            <h1 class="text-textPrimary text-8xl font-heading">Kakovost</h1>
            <p class="text-textSecondary">Lorem ipsum dolor sit, amet consectetur adipisicing elit. Sed, ipsam?</p>
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
    <div class="flex xl:flex-col lg:max-xl:h-[250px] xl:basis-[30%] gap-4 xl:shrink-0 xl:grow-0 2x xl:max-w-[300px] 2xl:max-w-[500px]">
        <!-- Gallery -->
        <div class="hero-link" style="background-image: url('https://picsum.photos/200/300')">
            <div>
                <div>
                    Galerija
                    <RightArrow class="text-2xl" />
                </div>
            </div>
        </div>
    
        <!-- Contact -->
        <div class="hero-link" style="background-image: url('https://picsum.photos/200/300')">
            <div>
                <div>
                    Kontakt
                    <RightArrow class="text-2xl" />
                </div>
            </div>
        </div>
    
        <!-- Story -->
        <div class="hero-link" style="background-image: url('https://picsum.photos/200/300')">
            <div>
                <div>
                    Zgodba
                    <RightArrow class="text-2xl" />
                </div>
            </div>
        </div>
    </div>
</section>

<!-- CTA -->
<section class="bg-orange-500 h-[20vh]">
    <div class="flex flex-col justify-center items-center h-full">
        <h1>Poklici me!</h1>
        <a href="/kontakt" class="btn">Kontakt</a>
    </div>
</section>

<!-- Features -->
<section class="bg-background py-28">
    <!-- Cards -->
    <div class="mx-20">
        <FeatureCard knifeImg={HandleImg} textureImg={WoodTextureImg} heading="Izjemno oblikovanje" description="Lorem ipsum dolor sit amet consectetur adipisicing elit. Aliquid totam sunt facere omnis error fugiat?" buttonText="Izvedi več" />

        <FeatureCard knifeImg={BladeImg} textureImg={WoodTextureImg} heading="Personalizacija" description="Lorem ipsum dolor sit amet consectetur adipisicing elit. Aliquid totam sunt facere omnis error fugiat?" buttonText="Izvedi več" flipped />
    </div>
</section>

<!-- Gallery showcase -->
<section class="bg-background px-28 pb-20">
    <div class="">
        <!-- Title & description & show more btn -->
        <div class="flex flex-col items-center text-textSecondary gap-2 mb-6">
            <h1 class="font-heading text-4xl text-textPrimary">Zadnji izdelki</h1>
            <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Asperiores, ullam!</p>
            <a href="/galerija" class="btn">Poglej vse</a>
        </div>

        <!-- Image slider -->
        <Splide aria-label="My Favorite Images" options={{
            perPage: 3,
            gap: "1em",
            autoWidth: true,
        }}>
            {#each Array(5) as _}
            <SplideSlide>
                <img src="https://picsum.photos/300/300" alt="Slika 1"/>
            </SplideSlide>
            {/each}
            <SplideSlide>
                <img src="https://picsum.photos/500/300" alt="Slika 1"/>
            </SplideSlide>
        </Splide>
    </div>
</section>

<!-- About me -->
<section class="bg-background py-40 bg-contain bg-no-repeat bg-center" style="background-image: linear-gradient(0deg, rgba(0,0,0,0.8) 0%, rgba(0,0,0,0.8) 100%), url({FireImg});">
    <div class="flex px-28 justify-center gap-8">
        <!-- My image -->
        <img src={MyImg} alt="" width="300px">

        <!-- About me text -->
        <div class="text-textSecondary w-3/6 flex items-center">
            <div class="">
                <h2 class="font-heading text-4xl text-textPrimary">Moja zgodba</h2>
                <p class="mb-10">Lorem ipsum dolor sit amet consectetur adipisicing elit. Qui cumque sapiente totam eum sunt, ex doloremque repudiandae voluptate quisquam ipsam, veniam nostrum aut atque hic rerum labore perspiciatis quae. Veritatis.</p>
                <a href="/zgodba" class="btn">Izvedi vec</a>
            </div>
        </div>
    </div>
</section>