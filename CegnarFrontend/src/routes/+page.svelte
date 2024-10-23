<script>
    // Images
    import HeroImg from "$lib/static/images/hero1.jpg";
    // Icons
    import RightArrow from '~icons/material-symbols-light/arrow-circle-right-outline-rounded';
    import IGIcon from '~icons/mdi/instagram';
    import FacebookIcon from '~icons/mdi/facebook-box';
    import EmailIcon from '~icons/mdi/email';
</script>

<!-- Hero section -->
<section class="xl:h-screen w-screen bg-background p-6 flex xl:flex-row flex-col gap-4">
    <!-- Main image / video -->
    <div class="hero-main w-full xl:h-full lg:h-[600px] rounded-2xl xl:basis-[70%] shrink grow bg-center relative" style="background-image: linear-gradient(0deg, rgba(0,0,0,0.7) 0%, rgba(255,255,255,0) 59%), url('{HeroImg}');">
        <!-- Hero navbar -->
        <div class="flex xl:justify-start xl:ms-10 xl:mt-10 lg:mt-4 lg:justify-center">
            <div class="inline-flex justify-center bg-background rounded-lg p-4 gap-4">
                <!-- Menu -->
                <div class="text-white font-2xl">
                    X
                </div>

                <!-- Logo -->
                <img src="https://framerusercontent.com/images/x0JzSofUJm2jTIMMg5jbgdRYVzU.webp" width="110px" class="object-contain" alt="logo">

                <!-- Links -->
                <ul class="inline-flex items-center gap-4">
                    <li class="hero-navbar-link">Galerija</li>
                    <li class="hero-navbar-link">Zgodba</li>
                    <li class="hero-navbar-link"><a href="/kontakt" class="border rounded p-2">Kontakt</a></li>
                </ul>
            </div>
        </div>
        
        <!-- Hero title -->
        <div class="absolute bottom-10 left-10 w-full xl:text-start text-center">
            <h1 class="text-white text-8xl font-heading">Kakovost</h1>
            <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Sed, ipsam?</p>
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


<section>

</section>